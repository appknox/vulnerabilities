脆弱性のある実装には、通常、以下に示すようなコードが含まれています:

    LAContext *context = [[LAContext alloc] init];
    NSError *error = nil;
    NSString *reason = @"Please authenticate using TouchID.";

    if ([context canEvaluatePolicy:LAPolicyDeviceOwnerAuthenticationWithBiometrics error:&error]) {
    [context evaluatePolicy:LAPolicyDeviceOwnerAuthenticationWithBiometrics
        localizedReason:reason
            reply:^(BOOL success, NSError *error) {
                if (success) {
                    NSLog(@"Auth was OK");
                }
                else {
                    //You should do better handling of error here
                    NSLog(@"Error received: %d", error);
                }
        }];
    }
    else {
    NSLog(@"Can not evaluate Touch ID");
    }