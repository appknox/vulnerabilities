
SSLスタックに脆弱性のあるアプリケーションがないことを確認してください。
脆弱性のあるアプリケーションがある場合、ベンダーがリリースした関連修正プログラムを適用していることを確認してください（利用可能な場合）。

RSA暗号化モードは非常にリスクがあるため、安全な対策としてはこれらを無効化することのみです。また、これらの暗号化モードは前方秘匿性に欠けます。
したがって、予防措置として、SSL スタックの TLS_RSA 暗号スイート (ただし、DHE または ECDHE が名前に含まれているものを除く)をすべて無効にすることを強く推奨します。
