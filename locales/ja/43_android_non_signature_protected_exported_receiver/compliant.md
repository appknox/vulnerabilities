
自分のアプリケーション間だけでデータを共有するためにブロードキャストレシーバを使用している場合は、「android：protectionLevel」属性を使用することをお勧めします。
署名のパーミッションはユーザの確認を必要としないため、データにアクセスするアプリケーションが同じ鍵で署名されている場合、より良いユーザエクスペリエンスとブロードキャストレシーバへのアクセスがより制御されたものになります。
