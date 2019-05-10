
アプリケーションをリリースする前に、android:debuggable 属性が false に設定されていることを確認してください。:

    <application
        ...
        android:debuggable="false" >
        ...
    </application>

いくつかの開発環境（Eclipse/ADTおよびAntを含む）は、インクリメンタルビルドまたはデバッギングビルドのために、android:debuggable を自動的に true にしますが、リリースビルドでは false に設定されることに注意してください。
