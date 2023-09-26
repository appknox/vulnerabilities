
NSExceptionRequiresForwardSecrecy キーは、iOS アプリの App Transport Security (ATS) 構成の一部です。 
これは、PFS (Perfect Forward Secrecy) 要件をオーバーライドするかどうかを示します。 
デフォルト値は true に設定されており、受け入れられる暗号は、Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) 
キー交換を通じて PFS をサポートする暗号に制限されます。 
PFS を使用すると、攻撃者が暗号化に使用される秘密キーを取得した場合でも、過去の通信セッションを遡って復号化することができなくなります。
