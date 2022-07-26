import contextlib
import os.path
import random
import sys
import time
import webbrowser

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import requests

from Main_Window import Ui_Form

Name_Collection = (
    "雷", "雪", "風", "沃", "亞", "卡", "烏", "音", "白", "瑟", "特", "嵐", "凱", "狐", "魯", "爾", "天", "吉", "斯", "路", "歐", "犬", "小",
    "克", "幻", "狼", "洛", "雨", "星", "靈", "阿", "羽", "夢", "焰", "貓", "利", "木", "太", "姆", "恩", "哈", "谷", "墨", "冰", "喵", "摩",
    "拉", "龍", "提", "空", "秋", "萊", "比", "冬", "夜", "蒼", "伊", "達", "王", "柴", "豹", "藍", "石", "川", "痕", "虎", "尼", "汪", "波",
    "狸", "塔", "艾", "烈", "迪", "諾", "獅", "灰", "瑞", "德", "光", "獺", "格", "倫", "松", "寒", "安", "力", "兔", "米", "恆", "賽", "水",
    "赤", "楓", "光", "紅", "納", "熊", "海", "影"
)


def name_gen():
    if random.randint(0, 999999) in {603683, 603691, 603718}:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    name_len = random.randint(1, 4)
    return "".join(random.choice(Name_Collection) for _ in range(name_len))


def background1_click(event=None):
    webbrowser.open(
        r"https://www.facebook.com/permalink.php?story_fbid=pfbid0YiQiizZzkcjohTWamS9jy3KSLKeKR8UCbvVVFNBRJb1ndni5YTP3YpurJ9nJ53Ntl&id=106417180993143&__cft__[0]=AZV9kZ3A1ksh12TlCZvMAas1J2KZDtVRbH-zXDlqCJUhJadkjZxLcbzH0nrGlub_v7JMDP-8JvAXimBYdmqEVV-YQcLvuzu_34FxCZhecsg8i1pNPYppNKdPnCGiW1Ns83SIwdNCeq8RDO5IyQh1PivsRyZrZXIDnniPDEYxLn-uTA&__tn__=%2CO%2CP-R"
    )


def background2_click(event=None):
    webbrowser.open(
        r"https://www.facebook.com/permalink.php?story_fbid=pfbid02Hd6BWd7JH8YiZhGUmu8FY38tSnrXczperjvxc4D4pb2uxVWfzv3SmKxKi3mDLvpBl&id=106417180993143&__cft__[0]=AZUNK7TSJNWx4xFuWeYV77J5B80sYKtpQDv6F4zHKWyBnO3pCql1v1lVHQRzGPGGv0G3l75s3mi9o5h7XZYw01fwfcMlSoCNCNfOTWMhZxAIhLh9wuqAZygxmcfTrfS_v6_Tat2-NANj0PSMcZl8OZArjinTordl_3sWrxyCbLC56Q&__tn__=%2CO%2CP-R"
    )


def background3_click(event=None):
    webbrowser.open(
        r"https://www.facebook.com/permalink.php?story_fbid=pfbid02DRzMhBzHFGBzseUBrYJ5U5HHvwKwHB5GrreAUhBQ3y8e5eFCXHuL54pz2dBgMzdWl&id=106417180993143&__cft__[0]=AZUNEORVS609d5Fnd41BrjMsH6dCWIjHqLrwfSw-uIvxrwWuG5fvjjO08URFyT8XJF7ntEUsTnip0Z5c2ajuJ_or-aKVkUfQyGudbrEzd2rf9_fObxn1BFBFUJEwcCdsxq8nxJYDJt-_HhvpVxbfo0VC&__tn__=%2CO%2CP-R"
    )


current_rel = "v1.2.1"


class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GenNameBtn.clicked.connect(self.name_gen_class)
        self.ui.Banner.mousePressEvent = self.background_click_class1
        self.ui.Banner.setScaledContents(True)
        self.ui.Banner.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        self.ui.Banner.setSizePolicy(
            PySide6.QtWidgets.QSizePolicy.Expanding,
            PySide6.QtWidgets.QSizePolicy.Expanding,
        )
        self.ui.VersionTag.setAlignment(PySide6.QtCore.Qt.AlignRight)
        self.ui.VersionTag.setText(f"版本: {current_rel}")
        self.gh_api_rel_check()
        bg_timer = PySide6.QtCore.QTimer()
        bg_timer.timeout.connect(self.bg_update1())
        bg_timer.start(5000)

    def name_gen_class(self):
        name = f"     {name_gen()}    "
        msg = PySide6.QtWidgets.QMessageBox
        """
        msg.setStyleSheet(
            ".QMessageBox{background:rgba(30,30,10,255);color:#fff}QLabel{background:transparent;color:#fff}")
        """
        msg.information(self, "你的名字", name)

    def keyPressEvent(self, event):  # 設定鍵盤按鍵映射
        super(MainWindow, self)
        if event.key() == PySide6.QtCore.Qt.Key_Space:
            self.name_gen_class()
        elif event.key() == PySide6.QtCore.Qt.Key_Escape:
            self.close()

    def background_click_class1(self, event):
        PySide6.QtWidgets.QMessageBox.information(self, "隱藏功能", "即將開啟原貼文")
        background1_click(event)

    def background_click_class2(self, event):
        PySide6.QtWidgets.QMessageBox.information(self, "隱藏功能", "即將開啟原貼文")
        background2_click(event)

    def background_click_class3(self, event):
        PySide6.QtWidgets.QMessageBox.information(self, "隱藏功能", "即將開啟原貼文")
        background3_click(event)

    def bg_update1(self):
        self.ui.Banner.setPixmap(PySide6.QtGui.QPixmap(f"{running_dir}banner2.png"))
        self.ui.Banner.mousePressEvent = self.background_click_class1
        PySide6.QtCore.QTimer.singleShot(5000, self.bg_update2)

    def bg_update2(self):
        self.ui.Banner.setPixmap(PySide6.QtGui.QPixmap(f"{running_dir}banner6.png"))
        self.ui.Banner.mousePressEvent = self.background_click_class2
        PySide6.QtCore.QTimer.singleShot(5000, self.bg_update3)

    def bg_update3(self):
        self.ui.Banner.setPixmap(PySide6.QtGui.QPixmap(f"{running_dir}banner8.png"))
        self.ui.Banner.mousePressEvent = self.background_click_class3
        PySide6.QtCore.QTimer.singleShot(5000, self.bg_update1)

    def gh_api_rel_check(self):
        with contextlib.suppress(Exception):
            rel_res = requests.get("https://api.github.com/repos/cytsai1008/FurryLoaferName/releases").json()

            if rel_res[0]["tag_name"] != current_rel:
                msg_window = PySide6.QtWidgets.QMessageBox.question(self, "更新通知",
                                                                    f"有新版本可以下載，目前版本為 {current_rel}，最新版本為 {rel_res[0]['tag_name']}")

                if msg_window == PySide6.QtWidgets.QMessageBox.Yes:
                    webbrowser.open(rel_res[0]["html_url"])
                    sys.exit(0)


if __name__ == "__main__":
    if (sys.argv[0]).find(".py") == -1:
        if os.path.exists(f"{sys.argv[0]}/image"):
            running_dir = f"{os.path.dirname(sys.argv[0])}/image/"
        else:
            running_dir = f"{os.path.dirname(__file__)}/image/"
    else:
        running_dir = "./image/"
    app = PySide6.QtWidgets.QApplication()
    if random.randint(0, 2) == 0:
        pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner3.png")
        msg = "準備好成為雷包了嗎"
    elif random.randint(0, 2) == 1:
        pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner7.png")
        msg = "嗚嗚你們不要再更新了啦QAQ"
    else:
        pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner9.png")
        msg = "哭阿怎麼又更新了"
    splash = PySide6.QtWidgets.QSplashScreen(pixmap)
    splash.show()
    splash.showMessage(msg, PySide6.QtCore.Qt.AlignBottom, PySide6.QtCore.Qt.white)
    time.sleep(2)
    app.processEvents()
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec())
