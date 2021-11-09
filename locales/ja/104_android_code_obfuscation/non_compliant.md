使用すると難読化に失敗する proguard-rules.pro 行の例:

-dontobfuscate


もし proguard も難読化もいずれも使用されていない場合は、Java バイトコードからソースコードを再現することが出来る無料の Java デコンパイラを使用することも可能です。

広く使用されているデコンパイラの一例として以下が挙げられます。

Bytecode Viewer- Java 8 jar およびAndroid APK をリバースエンジニアリングするセットです（デコンパイラ、エディタ、デバッガその他）
CFR - Javaのデコンパイラです。
JDGui - こちらも Java のデコンパイラです。
Fernflower - Java のデコンパイラです。
JadX - APK ファイル、DEX ファイルをデコンパイルするためのツールです。