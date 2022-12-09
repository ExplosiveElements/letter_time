# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transsearch.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
class Ui_trans(object):
    def setupUi(self, trans):
        trans.setObjectName("trans")
        #trans.resize(507, 300)

        self.pushButton_2 = QtWidgets.QPushButton(trans)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 190, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")

        self.widget = QtWidgets.QWidget(trans)
        self.widget.setGeometry(QtCore.QRect(40, 40, 431, 131))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        # 设置下拉选项
        self.comboBox.addItems(['弹幕', 'sc', '字幕', '礼物'])

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.LineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.LineEdit_2.setText("")
        self.LineEdit_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)
        # 设置只读
        self.LineEdit_2.setReadOnly(True)

        self.retranslateUi(trans)
        # 设置文件选择绑定槽
        self.pushButton.clicked.connect(self.msg)
        # 设置开始转化绑定槽
        self.pushButton_2.clicked.connect(self.start_trans)
        QtCore.QMetaObject.connectSlotsByName(trans)


    def retranslateUi(self, t):
        _translate = QtCore.QCoreApplication.translate
        t.setWindowTitle(_translate("trans", "文件转化"))
        self.pushButton_2.setText(_translate("trans", "开始转化"))
        self.label.setText(_translate("trans", " 转化类型"))
        self.pushButton.setText(_translate("trans", "文件选择"))

    # 自定义函数
    # 文件选择
    def msg(self):
        type = self.comboBox.currentText()
        if type == "字幕":
            file_type = 'SRT File(*.srt)'
        else:
            file_type = 'xml File(*.xml)'
        fielenme, filetype = QtWidgets.QFileDialog.getOpenFileName(None, "请选择要添加的文件", 'C:/', file_type)
        self.LineEdit_2.setText(fielenme)

    # 开始转化函数
    def start_trans(self):
        # 获取参数
        type1 = self.comboBox.currentText()
        file_name = self.LineEdit_2.text()
        # 开始查找
        result_list=trans(type1,file_name)
        search_html(file_name,type1,result_list)

