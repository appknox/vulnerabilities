
NSUserDefaultsは暗号化されずにバイナリフォーマットでplistに保存され、あなたのアプリのディレクトリに保存されます。どんなユーザでも編集、閲覧、共有、移動などやりたいことを何でもできます。そのため、もし何らかの機密情報がNSUserDefaultsに保存されるなら、それは誤った手に届き、個人利用される可能性があります。