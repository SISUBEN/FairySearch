# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from .assets import resources_rc

class Ui_Registor(object):
    def setupUi(self, Registor):
        if not Registor.objectName():
            Registor.setObjectName(u"Registor")
        Registor.resize(1388, 879)
        Registor.setMinimumSize(QSize(1388, 879))
        Registor.setMaximumSize(QSize(1388, 879))
        Registor.setStyleSheet(u"QWidget#Registor {\n"
"	background-image: url(:/images/images/reg.png);\n"
"    background-position: center;\n"
"}")
        self.layoutWidget = QWidget(Registor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QRect(430, 460, 551, 261))
        self.layoutWidget.setMinimumSize(QSize(0, 0))
        self.layoutWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.username_2 = QLineEdit(self.layoutWidget)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setEnabled(True)
        self.username_2.setMinimumSize(QSize(0, 0))
        self.username_2.setMaximumSize(QSize(16777215, 16777215))
        self.username_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /* color: rgb(41, 41, 41); */\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.verticalLayout_2.addWidget(self.username_2)

        self.password_3 = QLineEdit(self.layoutWidget)
        self.password_3.setObjectName(u"password_3")
        self.password_3.setEnabled(True)
        self.password_3.setMinimumSize(QSize(0, 0))
        self.password_3.setMaximumSize(QSize(16777215, 16777215))
        self.password_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")
        self.password_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_3)

        self.password_4 = QLineEdit(self.layoutWidget)
        self.password_4.setObjectName(u"password_4")
        self.password_4.setEnabled(True)
        self.password_4.setMinimumSize(QSize(0, 0))
        self.password_4.setMaximumSize(QSize(16777215, 16777215))
        self.password_4.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")
        self.password_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.register_btn_2 = QPushButton(self.layoutWidget)
        self.register_btn_2.setObjectName(u"register_btn_2")
        self.register_btn_2.setEnabled(True)
        self.register_btn_2.setMinimumSize(QSize(0, 0))
        self.register_btn_2.setMaximumSize(QSize(281, 61))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.register_btn_2.setFont(font)
        self.register_btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")
        self.register_btn_2.setCheckable(False)
        self.register_btn_2.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.register_btn_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Registor)

        QMetaObject.connectSlotsByName(Registor)
    # setupUi

    def retranslateUi(self, Registor):
        Registor.setWindowTitle(QCoreApplication.translate("Registor", u"Form", None))
        self.username_2.setText("")
        self.username_2.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.password_3.setText("")
        self.password_3.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.password_4.setText("")
        self.password_4.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801", None))
        self.register_btn_2.setText(QCoreApplication.translate("Registor", u"\u6ce8\u518c", None))
    # retranslateUi

