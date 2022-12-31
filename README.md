# 対話型ROS2パッケージ

端末から標準入力を受け取り、ROS2のデータ通信を使用して、
クイズを楽しむパッケージです。

* client.py
    標準入力から文字を受け取り、対話形式でクイズを進行する
    ノードです。

* times.py
    現在の時間を送信するノードです。

* quiz.py
    クイズを送信するノードです。

* ass.launch.py
    times.py と quiz.py を起動するローンチファイルです。

* pub.py
    0から1秒毎にカウントアップする数字をパブリッシュするノードです。

* sub.py
    pub.py からカウントアップされた数字をサブスクライブするノードです。

* cnt.launch.py
    pub.py と sub.py を起動するローンチファイルです。

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

1. 別の端末で client.py を起動。

この端末で対話的にプログラムを進行する。

```
$ ros2 run assy client
```

1. 




### カウントプログラム

1. cnt.launch.py を起動。

```
$ ros2 launch assy cnt.launch.py
```

1. カウントアップされていることを確認。





## ライセンス

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

© 2022 NAGAKI Yuki
