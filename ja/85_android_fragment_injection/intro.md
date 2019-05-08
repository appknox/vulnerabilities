
Android SDKは、開発者がユーザーに[`Preferences activity`](https://developer.android.com/reference/android/preference/PreferenceActivity.html)を提示する方法を提供し、この抽象クラスを拡張してニーズに合わせることができます。
この抽象クラスは、特に次のふたつのインテントで受け取った余分なデータフィールドを解析します。
`PreferenceActivity.EXTRA_SHOW_FRAGMENT(:android:show_fragment)` and
`PreferenceActivity.EXTRA_SHOW_FRAGMENT_ARGUMENTS(:android:show_fragment_arguments)`
最初のフィールドには `Fragment`クラス名が含まれ、2番目のフィールドには` Fragment`に渡された入力バンドルが含まれていることが望まれます。

`PreferenceActivity`がフラグメントをロードするためにリフレクションを使用することで、パッケージまたはAndroid SDKの中に任意のクラスをロードすることにつながります。 ロードされたクラスは、このアクティビティをエクスポートするアプリケーションのコンテキストで実行されます。
