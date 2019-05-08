
**パスワードの場合**、scrypt、bcrypt、PBKDF2など意図的に遅いハッシュ構造を使用する必要があります。slted SHA-2は、ほとんどの汎用ハッシュのように高速ですので、十分ではありません。([パスワードを安全にハッシュする方法](https://security.stackexchange.com/questions/211/how-to-securely-hash-passwords))

**ファイルの完全性の場合**、現在の最良のソリューションはSHA-2です（SHA-256）。SHA-3が標準化されると同様に良い選択となります。
