
使用すると難読化に失敗する proguard-rules.pro 行の例:

    -dontobfuscate


もし proguard も難読化もいずれも使用されていない場合は、Java バイトコードからソースコードを再現することが出来る無料の Java デコンパイラを使用することも可能です。

広く使用されているデコンパイラの一例として以下が挙げられます。

- [Bytecode Viewer](https://bytecodeviewer.com) - Java 8 jar およびAndroid APK をリバースエンジニアリングするセットです（デコンパイラ、エディタ、デバッガその他）
- [CFR](http://www.benf.org/other/cfr/) - Javaのデコンパイラです。
- [JDGui](http://jd.benow.ca/) - こちらも Java のデコンパイラです。
- [Fernflower](https://github.com/fesh0r/fernflower) - Java のデコンパイラです。
- [JadX](https://github.com/skylot/jadx) - APK ファイル、DEX ファイルをデコンパイルするためのツールです。
