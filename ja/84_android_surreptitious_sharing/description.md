
このアクティビティは `android.intent.action.SEND`または
`android.intent.action.SEND_MULTIPLE`は、ファイルスキームをデータURI`（file：// ...） `としてパラメータとして受け取ります。 非公開のアプリケーションのプライベートファイルを参照するURIを設定する可能性があり、適切なサニティーチェックが行われない場合、参照されたファイルを取得するために使用される可能性があります。