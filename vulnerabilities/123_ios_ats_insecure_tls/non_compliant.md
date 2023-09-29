
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <false/>

        <key>NSExceptionDomains</key>
        <dict>
            <key>example.com</key>
            <dict>
                <key>NSExceptionMinimumTLSVersion</key>
                <string>TLSv1.0</string>
            </dict>
        </dict>
    </dict>
