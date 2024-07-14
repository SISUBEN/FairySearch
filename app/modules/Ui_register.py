# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(1275, 718)
        Register.setMinimumSize(QSize(1275, 718))
        Register.setMaximumSize(QSize(1275, 718))
        Register.setStyleSheet(u"background-color: #061c3e;background-image: url(:/images/images/hdd.png)")
        self.layoutWidget = QWidget(Register)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 350, 451, 191))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.username = QLabel(self.layoutWidget)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(40, 0))
        self.username.setMaximumSize(QSize(40, 20))
        self.username.setStyleSheet(u"color: white;background-color:white;")
        self.username.setTextFormat(Qt.RichText)
        self.username.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.username)

        self.username_4 = QLineEdit(self.layoutWidget)
        self.username_4.setObjectName(u"username_4")
        self.username_4.setStyleSheet(u"color: white;background:#061c3e;")

        self.horizontalLayout.addWidget(self.username_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username_2 = QLabel(self.layoutWidget)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setMinimumSize(QSize(40, 0))
        self.username_2.setMaximumSize(QSize(40, 20))
        self.username_2.setStyleSheet(u"color: white;background-color:white;")
        self.username_2.setTextFormat(Qt.RichText)
        self.username_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.username_2)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"color: white;background:#061c3e;")

        self.horizontalLayout_2.addWidget(self.password)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username_3 = QLabel(self.layoutWidget)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setMaximumSize(QSize(16777215, 20))
        self.username_3.setStyleSheet(u"color: white;background-color:white;")
        self.username_3.setTextFormat(Qt.RichText)
        self.username_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.username_3)

        self.password2 = QLineEdit(self.layoutWidget)
        self.password2.setObjectName(u"password2")
        self.password2.setStyleSheet(u"color: white;background:#061c3e;")

        self.horizontalLayout_3.addWidget(self.password2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color:white;background:#061c3e;")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Register", None))
        self.username.setText(QCoreApplication.translate("Register", u"\u7528\u6237\u540d\uff1a", None))
        self.username_2.setText(QCoreApplication.translate("Register", u"\u5bc6      \u7801\uff1a", None))
        self.username_3.setText(QCoreApplication.translate("Register", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Register", u"Reg", None))
    # retranslateUi

