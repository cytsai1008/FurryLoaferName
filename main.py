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
)


def name_gen():
    if random.randint(0, 999999) == 603683:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    name_len = random.randint(1, 4)
    name = ""
    for i in range(name_len):
        name += random.choice(Name_Collection)
    return name


def background_click(event):
    webbrowser.open(
        r"https://www.facebook.com/permalink.php?story_fbid=pfbid0YiQiizZzkcjohTWamS9jy3KSLKeKR8UCbvVVFNBRJb1ndni5YTP3YpurJ9nJ53Ntl&id=106417180993143&__cft__[0]=AZV9kZ3A1ksh12TlCZvMAas1J2KZDtVRbH-zXDlqCJUhJadkjZxLcbzH0nrGlub_v7JMDP-8JvAXimBYdmqEVV-YQcLvuzu_34FxCZhecsg8i1pNPYppNKdPnCGiW1Ns83SIwdNCeq8RDO5IyQh1PivsRyZrZXIDnniPDEYxLn-uTA&__tn__=%2CO%2CP-R"
    )


class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GenNameBtn.clicked.connect(self.name_gen_class)
        self.ui.Banner.mousePressEvent = self.background_click_class

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

    def background_click_class(self, event):
        PySide6.QtWidgets.QMessageBox.information(self, "隱藏功能", "即將開啟原貼文")
        background_click(event)


if __name__ == "__main__":
    if getattr(sys, "frozen", False):  # Running as compiled
        running_dir = sys._MEIPASS + "/image/"  # Same path name than pyinstaller option
    else:
        running_dir = "./"  # Path name when run with Python interpreter
    app = PySide6.QtWidgets.QApplication()
    pixmap = PySide6.QtGui.QPixmap(f"{running_dir}Banner3.png")
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
