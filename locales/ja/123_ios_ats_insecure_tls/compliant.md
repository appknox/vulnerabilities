
「NSExceptionMinimumTLSVersion」が設定されていない場合、デフォルトは安全とみなされている TLSv1.2 になります。 
明示的に設定する場合は、TLSv1.2 または TLSv1.3 に設定する必要があります。

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
