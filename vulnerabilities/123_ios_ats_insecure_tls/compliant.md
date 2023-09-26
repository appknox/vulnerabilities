
"NSExceptionMinimumTLSVersion" if not set, defaults to TLSv1.2 which is considered safe.
If it is set explicitly, it should be set to TLSv1.2 or TLSv1.3.

    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <false/>

        <key>NSExceptionDomains</key>
        <dict>
            <key>example.com</key>
            <dict>
                <key>NSExceptionMinimumTLSVersion</key>
                <string>TLSv1.3</string>
            </dict>
        </dict>
    </dict>
