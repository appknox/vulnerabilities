
通常、 <code>ipa</code> ファイルはランタイム時にカーネルの mach loader によって復号化されます。
もしバイナリが暗号化あるいは otool を使用しているのが容易に分からない場合のバイナリが暗号化されている場所の一例は以下の通りです。：

    # otool -l OTHER_BINARY | grep -A 4 LC_ENCRYPTION_INFO
           cmd LC_ENCRYPTION_INFO
       cmdsize 20
      cryptoff 16384
     cryptsize 10502144
     cryptid   1

- ASLR
    - 通常、バイナリは `PIE`フラグを使用してコンパイルされます。
- スタックスマッシング保護
    - iOSアプリケーションは通常、 `[stack canaries]（）`を使用します。
    - したがって、バイナリの中に特定のシンボルがあるはずです。
       （ 例：`_stack_chk_guard`や` _stack_chk_fail`）
- 自動リファレンスカウティング
    - このオプションは、コンパイラオプションを有効にすることで使用できるようになります。
      `Objective-C自動参照カウント`
    - このオプションで構築されたバイナリには、以下のシンボルを含むようにしてください。
      `_objc_release`、` _obj_autorelease`、 `_obj_storeStrong`、`_obj_retain`

