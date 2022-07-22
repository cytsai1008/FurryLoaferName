# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
    QPixmap,
)
from PySide6.QtWidgets import QLabel, QPushButton

if getattr(sys, "frozen", False):  # Running as compiled
    running_dir = sys._MEIPASS + "/image/"  # Same path name than pyinstaller option
else:
    running_dir = "./"  # Path name when run with Python interpreter


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(720, 420)
        Form.setMinimumSize(QSize(720, 420))
        Form.setMaximumSize(QSize(720, 420))
        self.Banner = QLabel(Form)
        self.Banner.setObjectName("Banner")
        self.Banner.setGeometry(QRect(10, 10, 701, 291))
        self.Banner.setPixmap(QPixmap(f"{running_dir}Banner2.png"))
        self.Banner.setAlignment(Qt.AlignCenter)
        self.GenNameBtn = QPushButton(Form)
        self.GenNameBtn.setObjectName("GenNameBtn")
        self.GenNameBtn.setGeometry(QRect(10, 320, 701, 81))
        font = QFont()
        font.setPointSize(25)
        self.GenNameBtn.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "\u7378\u5708\u96f7\u5305\u540d\u7a31\u7522\u751f\u5668", None
            )
        )
        self.Banner.setText("")
        self.GenNameBtn.setText(
            QCoreApplication.translate(
                "Form", "\u7522\u751f\u4e00\u500b\u96f7\u5305\u540d", None
            )
        )

    # retranslateUi
