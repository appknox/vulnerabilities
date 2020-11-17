
The following is a good network security configuration:

    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <base-config cleartextTrafficPermitted="false">
            <trust-anchors>
                <certificates src="..."/>
                ...
            </trust-anchors>
        </base-config>

        <domain-config cleartextTrafficPermitted="false">
            <domain>android.com</domain>
            ...
            <trust-anchors>
                <certificates src="..."/>
                ...
            </trust-anchors>
            <pin-set>
                <pin digest="...">...</pin>
                ...
            </pin-set>
        </domain-config>
        ...
    </network-security-config>
