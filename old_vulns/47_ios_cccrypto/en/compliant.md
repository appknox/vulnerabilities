In CBC-mode, each 16-byte encryption influences the next 16-byte encryption. It's also the default. The problem is about block 0. It is a random block -1 which is the IV.

This is listed as optional in `CCCrypt()` which is confusing because it isn't really optional in CBC mode. If it is not provided, then it'll automatically generate an all-0 IV. That throws away significant protection on the first block. IV is just 16 random bytes.

The method returns the encrypted data (nil for error), and returns the IV, salt and error by reference.

    NSData *iv;
    NSData *salt;
    NSError *error;
    NSData *encryptedData = [RNCryptManager encryptedDataForData:plaintextData
                                                        password:password
                                                              iv:&iv
                                                            salt:&salt
                                                           error:&error];

Example implementation

    #import <CommonCrypto/CommonCryptor.h>
    #import <CommonCrypto/CommonKeyDerivation.h>

    NSString * const
    kRNCryptManagerErrorDomain = @"net.robnapier.RNCryptManager";

    const CCAlgorithm kAlgorithm = kCCAlgorithmAES128;
    const NSUInteger kAlgorithmKeySize = kCCKeySizeAES128;
    const NSUInteger kAlgorithmBlockSize = kCCBlockSizeAES128;
    const NSUInteger kAlgorithmIVSize = kCCBlockSizeAES128;
    const NSUInteger kPBKDFSaltSize = 8;
    const NSUInteger kPBKDFRounds = 10000;  // ~80ms on an iPhone 4

    + (NSData *)encryptedDataForData:(NSData *)data
                            password:(NSString *)password
                                  iv:(NSData )iv
                                salt:(NSData )salt
                               error:(NSError )error {
      NSAssert(iv, @"IV must not be NULL");
      NSAssert(salt, @"salt must not be NULL");

      *iv = [self randomDataOfLength:kAlgorithmIVSize];
      *salt = [self randomDataOfLength:kPBKDFSaltSize];

      NSData *key = [self AESKeyForPassword:password salt:*salt];

      size_t outLength;
      NSMutableData *
      cipherData = [NSMutableData dataWithLength:data.length +
                    kAlgorithmBlockSize];

      CCCryptorStatus
      result = CCCrypt(kCCEncrypt, // operation
                       kAlgorithm, // Algorithm
                       kCCOptionPKCS7Padding, // options
                       key.bytes, // key
                       key.length, // keylength
                       (*iv).bytes,// iv
                       data.bytes, // dataIn
                       data.length, // dataInLength,
                       cipherData.mutableBytes, // dataOut
                       cipherData.length, // dataOutAvailable
                       &outLength); // dataOutMoved

      if (result == kCCSuccess) {
        cipherData.length = outLength;
      }
      else {
        if (error) {
          *error = [NSError errorWithDomain:kRNCryptManagerErrorDomain
                                       code:result
                                   userInfo:nil];
        }
        return nil;
      }

      return cipherData;
    }

    + (NSData *)randomDataOfLength:(size_t)length {
      NSMutableData *data = [NSMutableData dataWithLength:length];

      int result = SecRandomCopyBytes(kSecRandomDefault,
                                      length,
                                      data.mutableBytes);
      NSAssert(result == 0, @"Unable to generate random bytes: %
                d", errno);

      return data;
    }

    // Replace this with a 10,000 hash calls if you don't have CCKeyDerivationPBKDF
    + (NSData *)AESKeyForPassword:(NSString *)password
                             salt:(NSData *)salt {
      NSMutableData *
      derivedKey = [NSMutableData dataWithLength:kAlgorithmKeySize];

      int
      result = CCKeyDerivationPBKDF(kCCPBKDF2,            // algorithm
                                    password.UTF8String,  // password
                                    [password lengthOfBytesUsingEncoding:NSUTF8StringEncoding],  // passwordLength
                                    salt.bytes,           // salt
                                    salt.length,          // saltLen
                                    kCCPRFHmacAlgSHA1,    // PRF
                                    kPBKDFRounds,         // rounds
                                    derivedKey.mutableBytes, // derivedKey
                                    derivedKey.length); // derivedKeyLen

      // Do not log password here
      NSAssert(result == kCCSuccess, @"Unable to create AES key for password: %
               d", result);

      return derivedKey;
    }
