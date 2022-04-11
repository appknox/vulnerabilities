基本構成やドメイン構成でcleartextTrafficPermittedをTrueに設定している場合に問題がとなります。src が "user" に設定されている場合、ユーザーは自分の証明書をデバイスにインストールすることができ、アプリはその証明書をピン留めされた証明書の代わりに使用できる可能性があります。

<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" />
        </trust-anchors>
    </base-config>
</network-security-config>


debug-overrides を追加すると、デバッグ証明書が公開され、アプリケーションに対する 中間者攻撃に使用される可能性があります。


<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="@raw/debug_cas"/>
        </trust-anchors>
    </debug-overrides>
</network-security-config>