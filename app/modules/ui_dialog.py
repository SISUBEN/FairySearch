# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from app.assets import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(840, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(840, 630))
        Dialog.setMaximumSize(QSize(840, 630))
        Dialog.setStyleSheet(u"QDialog#Dialog {\n"
"    border-image: url(:/images/images/background.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.leftSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonLayout.addItem(self.leftSpacer)

        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy1)
        self.okButton.setMinimumSize(QSize(200, 0))
        self.okButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    /*width: 500px;*/\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")

        self.buttonLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy1.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy1)
        self.cancelButton.setMinimumSize(QSize(200, 0))
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")

        self.buttonLayout.addWidget(self.cancelButton)

        self.rightSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonLayout.addItem(self.rightSpacer)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"{text}", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

