
正規表現を使ったサービス拒否（ReDoS）はサービス拒否攻撃であり、ほとんどの正規表現の実装が非常にゆっくりと動作する（入力サイズに指数関数的に関係する）極端な状況に達する可能性があるという点を利用しています。攻撃者は、正規表現を使用しているプログラムにこれらの極端な状況を入力させ、それにより非常に長い時間ハングする可能性があります。