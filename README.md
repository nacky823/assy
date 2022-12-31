# ROS2 通信による対話型クイズパッケージ

端末から標準入力を受け取り、ROS2のデータ通信を使用して、
クイズを楽しむパッケージです。

[![test](https://github.com/nacky823/assy/actions/workflows/test.yml/badge.svg)](https://github.com/nacky823/assy/actions/workflows/test.yml)

* client.py
    * 標準入力から文字を受け取り、対話形式でクイズを進行します。
    クライアントとして times.py, quiz.py と通信を行います。

* times.py
    * 現在の時間を所得します。サーバーとして client.py と通信を行います。

* quiz.py
    * クイズを送信します。サーバーとして client.py と通信を行います。

* ass.launch.py
    * times.py と quiz.py を起動するローンチファイルです。

* pub.py
    * 0から1秒毎にカウントアップする数字をパブリッシュするノードです。

* sub.py
    * pub.py からカウントアップされた数字をサブスクライブするノードです。

* cnt.launch.py
    * pub.py と sub.py を起動するローンチファイルです。

## 動作確認済みの環境

* OS : Ubuntu 22.04.1 LTS

* Software :

    ROS2 humble

    Python 3.10.6

## インストール

※ ROS2 のインストール方法については記述しない。

```
$ cd ~/ros2_ws/src/

$ git clone git@github.com:nacky823/assy.git
```

ビルド＆ソースまで済ませておく。

```
$ cd ~/ros2_ws/

$ colcon build

$ source ~/.bashrc
```

## 使用方法

### クイズプログラム

1. ass.launch.py を起動。

```
$ ros2 launch assy ass.launch.py
```

2. 別の新しい端末で client.py を起動。

この端末で対話的にプログラムを進行する。

```
$ ros2 run assy client
```

3. キーボードからコマンドを入力します。

```
こんばんは。

現在の時刻は 21:38 です。

ご要望をお伺いします。

以下の表を参考に、キーボードからコマンドを入力してください。

###===============================================================###

・クイズ X : 「x」を入力した後、「Enter」を入力してください。

・クイズ Y : 「y」を入力した後、「Enter」を入力してください。

・クイズ Z : 「z」を入力した後、「Enter」を入力してください。

###===============================================================###

Please input here :
```

> 起動する時刻によって挨拶が変わるようになっています。

4. クイズに挑戦します。同様にキーボードからコマンドを入力します。

```
###==============================================================###

電車に乗っているとき、自分は座っていて、
近くにご老人が立っている場合、どの行動が正解でしょう？

「za」: 席をお譲りする。
「zb」: 気になるが、声をかける勇気はない。
「zc」: 眠い。寝よう。

「za」「zb」「zc」から一つを入力し、「Enter」を入力してください。

###==============================================================###

Please input here :
```

5. 続けて実行するかを選択します。同様にキーボードからコマンドを入力します。

```
Please input here : n


###==============================================================###

全てのプログラムを終了しました。

ご使用頂きありがとうございます。

###==============================================================###


現在の時刻は 21:58 です。

ゆっくり休んでくださいね (*^ ^*)
```

> 今回は「n」を入力しましたが、「y」を入力すると 3. に戻って繰り返し実行します。
> 時間帯によって可愛く挨拶してくれます。

### カウントプログラム

1. cnt.launch.py を起動。

```
$ ros2 launch assy cnt.launch.py
```

2. カウントアップされていることを確認。

```
[sub-1] [INFO] [1672489806.015519800] [sub]: Count second : 0 [s]
[sub-1] [INFO] [1672489807.008195800] [sub]: Count second : 1 [s]
[sub-1] [INFO] [1672489808.007895400] [sub]: Count second : 2 [s]
[sub-1] [INFO] [1672489809.007844300] [sub]: Count second : 3 [s]
[sub-1] [INFO] [1672489810.007338400] [sub]: Count second : 4 [s]
[sub-1] [INFO] [1672489811.007033900] [sub]: Count second : 5 [s]
[sub-1] [INFO] [1672489812.007284700] [sub]: Count second : 6 [s]
```


## ライセンス

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

© 2022 NAGAKI Yuki
