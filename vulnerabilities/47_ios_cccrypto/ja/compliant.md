initialization vector (IV) は紛らわしい存在です。CBCモードでは、各16バイトの暗号化が次の16バイト暗号化に影響し、 これもデフォルトです。問題はブロック0についてです。これはIVであるランダムブロック-1です。

これは `CCCrypt()` にオプションとしてリストされていますが、CBCモードでは実際にはオプションではないので混乱が生じます。提供されていない場合、自動的にall-0 IVが生成されます。 それは最初のブロックに大きな保護を捨てます。 IVはちょうど16のランダムバイトです。このメソッドは、暗号化されたデータ（エラーの場合はnil）を返し、参照によってIV、ソルト、およびエラーを返します。

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
