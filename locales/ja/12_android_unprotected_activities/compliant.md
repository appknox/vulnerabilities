
この準拠ソリューションでは、アクティビティはエクスポートされません。

    <activity
        android:configChanges="keyboard|keyboardHidden|orientation"
        android:name=".media.yfrog.YfrogUploadDialog"
        android:theme="@style/ VulnerableTheme.Dialog"
        android:windowSoftInputMode="stateAlwaysHidden"
        android:exported="false">
    </activity>

AndroidManifest.xmlファイル内のactivityタグに対してandroid:exported="false"を宣言することにより、アクティビティは同じアプリケーション内、または同じユーザIDのアプリケーションからのインテントのみを受け入れるように制限されます。

    public void onCreate(Bundle arg5) {
        super.onCreate(arg5);
        ...
        ComponentName v0 = this.getCallingActivity();
        if (v0 == null) {
            this.finish();
        } else if (!jp.r246.twicca.equals(v0.getPackageName())) {
            this.finish();
        } else {
            this.a = this.getIntent().getData();
            if (this.a == null) {
                this.finish();
            }
            ...
        }
    }

Android開発者は、任意にパッケージ名を選択できるため、異なるアプリケーション開発者は同じパッケージ名を選択できました。したがって、通常はアクティビティの呼び出し元を検証するためにパッケージ名を使用することは推奨されません。推奨されている代案は、パッケージ名の代わりに開発者の証明書を確認することです。

しかし、以下の事実を考慮すると、Twiccaのソリューションは、論理的でエクスプロイトに対して安全である可能性があります。:

- 特定のパッケージ名を持つ1つのアプリのみがGoogle Playに存在することができます。
- もしユーザがパッケージ名が既にデバイス上に存在するアプリケーションをインストールしようとすると、インストールが失敗するか、以前にインストールされたアプリケーションを上書きします。

