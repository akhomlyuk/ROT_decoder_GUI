# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowsXljoda.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextEdit,
    QWidget)
import resources

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(460, 135)
        font = QFont()
        font.setFamilies([u"Ubuntu Medium"])
        font.setPointSize(14)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/res/main.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.000000000000000)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.picture_label = QLabel(Form)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setGeometry(QRect(10, 10, 120, 120))
        self.picture_label.setMinimumSize(QSize(100, 100))
        self.picture_label.setMaximumSize(QSize(500, 500))
        self.picture_label.setStyleSheet(u"")
        self.picture_label.setPixmap(QPixmap(u":/icons/res/ex.jpg"))
        self.picture_label.setScaledContents(True)
        self.year = QLabel(Form)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(390, 110, 71, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 110, 81, 24))
        self.link_tg = QLabel(Form)
        self.link_tg.setObjectName(u"link_tg")
        self.link_tg.setGeometry(QRect(180, 60, 91, 42))
        self.link_tg.setOpenExternalLinks(True)
        self.icon_gh = QLabel(Form)
        self.icon_gh.setObjectName(u"icon_gh")
        self.icon_gh.setGeometry(QRect(140, 10, 31, 51))
        self.icon_gh.setPixmap(QPixmap(u":/icons/res/gh.svg"))
        self.icon_tg = QLabel(Form)
        self.icon_tg.setObjectName(u"icon_tg")
        self.icon_tg.setGeometry(QRect(140, 60, 31, 41))
        self.icon_tg.setPixmap(QPixmap(u":/icons/res/tg.svg"))
        self.icon_tg.setScaledContents(False)
        self.link_gh = QLabel(Form)
        self.link_gh.setObjectName(u"link_gh")
        self.link_gh.setGeometry(QRect(180, 20, 91, 42))
        self.link_gh.setOpenExternalLinks(True)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(300, 20, 151, 81))
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"About", None))
        self.picture_label.setText("")
        self.year.setText(QCoreApplication.translate("Form", u"\u00a9 2023", None))
        self.label.setText(QCoreApplication.translate("Form", u"Exited3n", None))
        self.link_tg.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a style=\"text-decoration: none; color: #090\" href=\"https://t.me/exited3n\">Telegram</span></a></p></body></html>", None))
        self.icon_gh.setText("")
        self.icon_tg.setText("")
        self.link_gh.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a style=\"text-decoration: none; color: #090\" href=\"https://github.com/akhomlyuk/ROT_decoder_GUI\">Sources</span></a></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Medium'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PySide6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Material design icons</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;"
                        "\">Coco Line icons</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Qt Designer</span></p></body></html>", None))
    # retranslateUi

