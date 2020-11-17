
If you have set the base configuration or domain configuration with
cleartextTrafficPermitted to True then it is a problem.
If the `src` is set to `"user"` then, a user can install his own certificate
in the device and the app will use that instead of the pinned certificate.

    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <base-config cleartextTrafficPermitted="true">
            <trust-anchors>
                <certificates src="system" />
                <certificates src="user" />
            </trust-anchors>
        </base-config>
    </network-security-config>

Adding a debug-overrides can expose your debug certificate which can be used to
perform MITM attack on your application.

    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <debug-overrides>
            <trust-anchors>
                <certificates src="@raw/debug_cas"/>
            </trust-anchors>
        </debug-overrides>
    </network-security-config>
