import sys
import random
import time

import PySide6.QtWidgets
import PySide6.QtCore
import PySide6.QtGui

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
    name_len = random.randint(1, 4)
    name = ""
    for i in range(name_len):
        name += random.choice(Name_Collection)
    return name


class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.GenNameBtn.clicked.connect(self.GenName)

    def GenName(self):
        name = f"     {name_gen()}    "
        msg = PySide6.QtWidgets.QMessageBox
        """
        msg.setStyleSheet(
            ".QMessageBox{background:rgba(30,30,10,255);color:#fff}QLabel{background:transparent;color:#fff}")
        """
        msg.information(self, "你的名字", name)

    def keyPressEvent(self, event):  # 設定鍵盤按鍵映射
        super(MainWindow, self)
        if event.key() in (PySide6.QtCore.Qt.Key_Space, PySide6.QtCore.Qt.Key_Enter):
            self.GenName()
        elif event.key() == PySide6.QtCore.Qt.Key_Escape:
            self.close()


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
