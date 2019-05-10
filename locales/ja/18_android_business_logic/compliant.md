
<p> 次のようなものはチェックと適切な修正をしてください。 </p> <ul> <li>クライアントサイドではなくサーバーサイドのOTPへのチェック</li> <li>次のような同じ承認トークンではなく、適切な認証を使用してください。<b>Authorization: Basic aW50ZXJhY3Rpb25vbmU6bW9iaTEyMw==</b> which translates to: <b>interactionone:mobi123</b></li> <li>mobi123 のようなパスワードを絶対に使用しないでください。</li> </ul>
