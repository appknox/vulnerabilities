
 この非準拠のコード例は、アクティビティを他のアプリケーションにエクスポートするアプリケーションのAndroidManifest.xmlファイルを示していますが、機密性の高いアクティビティへのアクセスを制限しません。: 

    <activity
        android:configChanges="keyboard|keyboardHidden|orientation"
        android:name=".media.yfrog.YfrogUploadDialog"
        android:theme="@style/Vulnerable.Dialog"
        android:windowSoftInputMode="stateAlwaysHidden">
        <intent-filter android:icon="@drawable/yfrog_icon" android:label="@string/YFROG">
            <action android:name="jp.co.vulnerable.ACTION_UPLOAD" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="image/*" />
            <data android:mimeType="video/*" />
        </intent-filter>
    </activity>

`android：name`はこのアクティビティを実装するクラスの名前を参照します。 パッケージの名前は `jp.co.vulnerable`なので、このアクティビティを実装するクラスの完全修飾名は ` jp.co.vulnerable.media.yfrog.YfrogUploadDialog` です。 インテントフィルタが定義されているため、このアクティビティは他のアプリケーションにエクスポートされます。

