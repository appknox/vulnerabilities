
<p>   CCCryptor の使用で、 AES, 3DES のような異なるアルゴリズムと RC4, DES などのようなハードコアセキュリティサイファーを使用して対称的な暗号化を実行するための CCCryptorCreate, CCCryptorUpdate, CCCryptorFinal (あるいは単に CCCrypt() one-shot 機能) のような共通範囲の機能を使用することが出来ます。    </p><p>Appleは暗号をECBとCBCモードでサポートしています。幸運にも、開発者はAPIがCBC（Cipher Block Chainingモード）にデフォルト設定されているので、ECBを使って明白に間違いを証明する必要があります。
おそらく「IV」と呼ばれるものがうまくいかないでしょう。
AppleはCommon Crypto APIのマニュアルページを書くときに頭字語「IV」を "Ignorance Vector"に翻訳したと思われますが、実際には最初の暗号テキストブロックの初期化に使用する "Initialization Vector"を読むべきです。 </p>
