import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class TimeClient():
    def __init__(self, nh):
        self.res_cnt = 0
        self.cli = nh.create_client(Spawn, "/times")

    def request(self):
        while not self.cli.wait_for_service(timeout_sec=1.0):
            print("waitting for service...")
        req = Spawn.Request()
        req.name = "now"
        self.future = self.cli.call_async(req)

    def response(self, nh):
        while rclpy.ok():
            rclpy.spin_once(nh)
            if self.future.done():
                try:
                    self.res = self.future.result()
                    self.res_cnt += 1
                except:
                    nh.get_logger().info("failed to response.")
                else:
                    self.greet()
                break

    def greet(self):
        res_txt = self.res.name.split(",")
        hour = int(res_txt[1])
        if self.res_cnt == 1:
            if hour >= 4 and hour <= 9:
                print("おはようございます。")
            elif hour >= 10 and hour <= 17:
                print("こんにちは。")
            elif hour >= 18 and hour <= 23:
                print("こんばんは。")
            elif hour >= 0 and hour <= 3:
                print("こんばんは。")
                print("夜更かしですか？（笑）")
            print("現在の時刻は", res_txt[0], "です。")
        elif self.res_cnt == 2:
            print("現在の時刻は", res_txt[0], "です。")
            if hour >= 4 and hour <= 9:
                print("素敵な一日になりますように ( ^ ^ )")
            elif hour >= 10 and hour <= 17:
                print("また遊びに来てくださいね ( ^-^ )/ ")
            elif hour >= 18 and hour <= 23:
                print("ゆっくり休んでくださいね (*^ ^*)")
            elif hour >= 0 and hour <= 3:
                print("早く寝ましょう！（笑）")
                print("ゆっくり休んでくださいね (*^ ^*)")


class SelectClient():
    def __init__(self, nh):
        self.repeat = 1
        self.end_failure = 1
        self.selection_failure = 1
        self.sel = nh.create_client(Spawn, "/select")

    def intro_txt(self):
        print("以下の表を参考に、キーボードからコマンドを入力してください。")
        print("\n###=====================================================###\n")
        print("・ゲーム１ :")
        print("    「p」を入力した後、「Enter」を押してください。")
        print("\n###=====================================================###\n")
        print("Please input here : ", end="")

    def input_key(self):
        print("\n")
        if self.key == "p":
            print("選択肢１が選択されました。")
        else:
            print(self.key, "は選択肢にありません。")
            print("再度入力をお願いします。")
            self.selection_failure = 1

    def select(self):
        self.end_failure = 1
        print("ご要望をお伺いします。")
        print(self.selection_failure)
        while self.selection_failure == 1:
            self.selection_failure = 0
            self.intro_txt()
            self.key = input()
            self.input_key()
        while not self.sel.wait_for_service(timeout_sec=1.0):
            print("waitting for service...")

    def request(self):
        req = Spawn.Request()
        req.name = self.key
        self.future = self.sel.call_async(req)

    def response(self, nh):
        while rclpy.ok():
            rclpy.spin_once(nh)
            if self.future.done():
                try:
                    self.res = self.future.result()
                except:
                    nh.get_logger().info("failed to response.")
                else:
                    print(self.res.name)
                break

    def end(self, nh):
        while self.end_failure == 1:
            print("続けて使用しますか？")
            print("続けて使用する場合は「y」")
            print("終了する場合は「n」")
            print("を入力してください。")
            self.end_failure = 0
            print("Please input here : ", end="")
            end_key = input()
            if end_key == "y":
                self.repeat = 1
                self.selection_failure = 1
            elif end_key == "n":
                self.key = "ending_password_hogehoge_soiya"
                self.request()
                self.response(nh)
                self.repeat = 0
            else:
                self.end_failure = 1

def main():
    rclpy.init()
    node = Node("client")
    time = TimeClient(node)
    time.request()
    time.response(node)
    select = SelectClient(node)

    while select.repeat == 1:
        select.select()
        select.request()
        select.response(node)
        select.end(node)

    time.request()
    time.response(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

