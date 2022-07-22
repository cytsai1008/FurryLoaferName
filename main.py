import random
import sys
import time
import webbrowser

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from Main_Window import Ui_Form

Name_Collection = (
    "雷",
    "雪",
    "風",
    "沃",
    "亞",
    "卡",
    "烏",
    "音",
    "白",
    "瑟",
    "特",
    "嵐",
    "凱",
    "狐",
    "魯",
    "爾",
    "天",
    "吉",
    "斯",
    "路",
    "歐",
    "犬",
    "小",
    "克",
    "幻",
    "狼",
    "洛",
    "雨",
    "星",
    "靈",
    "阿",
    "羽",
    "夢",
    "焰",
    "貓",
    "利",
    "木",
    "太",
    "姆",
    "恩",
    "哈",
    "谷",
    "墨",
    "冰",
    "喵",
    "摩",
    "拉",
    "龍",
    "提",
    "空",
)


def name_gen():
    if random.randint(0, 999999) in (603683, 603691):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    name_len = random.randint(1, 4)
    name = ""
    for i in range(name_len):
        name += random.choice(Name_Collection)
    return name


def background1_click(event=None):
    webbrowser.open(
        r"https://www.facebook.com/permalink.php?story_fbid=pfbid0YiQiizZzkcjohTWamS9jy3KSLKeKR8UCbvVVFNBRJb1ndni5YTP3YpurJ9nJ53Ntl&id=106417180993143&__cft__[0]=AZV9kZ3A1ksh12TlCZvMAas1J2KZDtVRbH-zXDlqCJUhJadkjZxLcbzH0nrGlub_v7JMDP-8JvAXimBYdmqEVV-YQcLvuzu_34FxCZhecsg8i1pNPYppNKdPnCGiW1Ns83SIwdNCeq8RDO5IyQh1PivsRyZrZXIDnniPDEYxLn-uTA&__tn__=%2CO%2CP-R"
    )


def background2_click(event=None):
    webbrowser.open(
        "https://www.facebook.com/permalink.php?story_fbid=pfbid02Hd6BWd7JH8YiZhGUmu8FY38tSnrXczperjvxc4D4pb2uxVWfzv3SmKxKi3mDLvpBl&id=106417180993143&__cft__[0]=AZUNK7TSJNWx4xFuWeYV77J5B80sYKtpQDv6F4zHKWyBnO3pCql1v1lVHQRzGPGGv0G3l75s3mi9o5h7XZYw01fwfcMlSoCNCNfOTWMhZxAIhLh9wuqAZygxmcfTrfS_v6_Tat2-NANj0PSMcZl8OZArjinTordl_3sWrxyCbLC56Q&__tn__=%2CO%2CP-R"
    )


if getattr(sys, "frozen", False):  # Running as compiled
    running_dir = sys._MEIPASS + "/image/"  # Same path name than pyinstaller option
else:
    running_dir = "./"  # Path name when run with Python interpreter


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

    def bg_update1(self):
        self.ui.Banner.setPixmap(PySide6.QtGui.QPixmap(f"{running_dir}banner2.png"))
        self.ui.Banner.mousePressEvent = self.background_click_class1
        PySide6.QtCore.QTimer.singleShot(5000, self.bg_update2)

    def bg_update2(self):
        self.ui.Banner.setPixmap(PySide6.QtGui.QPixmap(f"{running_dir}banner6.png"))
        self.ui.Banner.mousePressEvent = self.background_click_class2
        PySide6.QtCore.QTimer.singleShot(5000, self.bg_update1)


if __name__ == "__main__":
    if getattr(sys, "frozen", False):  # Running as compiled
        running_dir = sys._MEIPASS + "/image/"  # Same path name than pyinstaller option
    else:
        running_dir = "./"  # Path name when run with Python interpreter
    app = PySide6.QtWidgets.QApplication()
    if random.randint(0, 1) == 0:
        pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner3.png")
    else:
        pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner7.png")
    splash = PySide6.QtWidgets.QSplashScreen(pixmap)
    splash.show()
    splash.showMessage(
        "準備好成為雷包了嗎", PySide6.QtCore.Qt.AlignBottom, PySide6.QtCore.Qt.white
    )
    time.sleep(2)
    app.processEvents()
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec())
