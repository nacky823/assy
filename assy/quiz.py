import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class SelectService():
    def __init__(self, nh):
        self.repeat = 1
        self.quest()
        self.ans()
        nh.create_service(Spawn, "/select", self.cb)

    def cb(self, req, res):    
        if req.name == "tests":
            res.name = "skip to input"
        elif req.name == "z":
            res.name = self.qz
        elif req.name == "y":
            res.name = self.qy
        elif req.name == "x":
            res.name = self.qx

        elif req.name == "za":
            res.name = self.za
        elif req.name == "zb":
            res.name = self.zb
        elif req.name == "zc":
            res.name = self.zc
        elif req.name == "ya":
            res.name = self.ya
        elif req.name == "yb":
            res.name = self.yb
        elif req.name == "yc":
            res.name = self.yc
        elif req.name == "xa":
            res.name = self.xa
        elif req.name == "xb":
            res.name = self.xb
        elif req.name == "xc":
            res.name = self.xc

        elif req.name == "ending":
            res.name = "全てのプログラムを終了しました。\n\nご使用頂きありがとうございます。"
            self.repeat = 0
        else:
            res.name = "Unable to meet request."

        return res

    def quest(self):
        self.qz = "電車に乗っているとき、自分は座っていて、\n近くにご老人が立っている場合、どの行動が正解でしょう？"
        self.qy = "リュックサックのチャックが全開の人を見たとき、\nどの行動が正解でしょう？"
        self.qx = "締め切りが明日だという事を、布団に入ってから気づいた場合、\nどの行動をとるのが正解でしょう？"

    def ans(self):
        self.za = "正解だと思います。優しいですね( ^ ^ )"#"席をお譲りする。"
        self.zb = "正解だと思います。私もこの選択をしそうです。\n人の世いと難しや。"#"気になるが、声をかける勇気はない。"
        self.zc = "大正解だと思います。毎日お疲れ様です。\nたっぷり寝ましょう。"#"眠い。寝よう。"
        self.ya = "はい。不正解です。かなりやばい行動なのでやめましょう。"#"全力で閉めてあげる。"
        self.yb = "はい。不正解です。全力に負けず劣らずのやばさですね。\n思いとどまりましょう。"#"こっそり閉めてあげる。"
        self.yc = "正解だと思います。私も同じ意見なので気が合いますね。\nえ、選択肢がひどかった？ はて何のことでしょう。"#"気になるが、声をかける勇気がない。"
        self.xa = "正解だと思います。素直で素敵な性格だと思います。"#"泣く。"
        self.xb = "そう、何もなかった。何もなかったのだ。"#"よし。何もなかった。"
        self.xc = "正解だと思います。\n朝が怖いですね、想像するのもいやなので、\n私はこの辺で失礼します。"#"ZZZ..."

def main():
    rclpy.init()
    node = Node("quiz")
    service = SelectService(node)
    while service.repeat == 1:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

