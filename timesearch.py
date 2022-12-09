# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timesearch.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,  QtWidgets
from main import *

class Ui_time_search(object):
    # 初始化

    def setupUi(self, time_search):
        # 窗口设置
        time_search.setObjectName("time_search")
        # time_search.resize(505, 300)
        # 开始搜索按钮
        self.start_pushButton = QtWidgets.QPushButton(time_search)
        self.start_pushButton.setGeometry(QtCore.QRect(170, 230, 150, 46))
        self.start_pushButton.setObjectName("start_pushButton")
        # 布局设置
        self.layoutWidget = QtWidgets.QWidget(time_search)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 416, 176))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # 搜索类型标签
        self.type_label = QtWidgets.QLabel(self.layoutWidget)
        self.type_label.setObjectName("type_label")
        self.gridLayout.addWidget(self.type_label, 0, 0, 1, 1)
        # 搜索类型下拉框
        self.search_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.search_comboBox.setObjectName("search_comboBox")
        self.gridLayout.addWidget(self.search_comboBox, 0, 1, 1, 1)
        # 设置下拉选项
        self.search_comboBox.addItems(['弹幕','sc','字幕','礼物'])
        # 文件选择按钮
        self.file_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.file_pushButton.setObjectName("file_pushButton")
        self.gridLayout.addWidget(self.file_pushButton, 1, 0, 1, 1)
        # 文件路径显示文本框
        self.file_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.file_LineEdit.setObjectName("file_label")
        self.gridLayout.addWidget(self.file_LineEdit, 1, 1, 1, 1)
        # 设置文本框只读
        self.file_LineEdit.setReadOnly(True)
        # 查找词标签
        self.word_label = QtWidgets.QLabel(self.layoutWidget)
        self.word_label.setObjectName("word_label")
        self.gridLayout.addWidget(self.word_label, 2, 0, 1, 1)
        # 查找词输入框
        self.word_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.word_lineEdit.setObjectName("word_lineEdit")
        self.gridLayout.addWidget(self.word_lineEdit, 2, 1, 1, 1)
        # 设置查找词的输入方式
        self.word_lineEdit.setPlaceholderText("请用空格隔开查找词")
        # 聚合时间时长标签
        self.sum_label = QtWidgets.QLabel(self.layoutWidget)
        self.sum_label.setObjectName("sum_label")
        self.gridLayout.addWidget(self.sum_label, 3, 0, 1, 1)
        # 聚合时间计数器
        self.sum_SpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.sum_SpinBox.setObjectName("sum_doubleSpinBox")
        self.gridLayout.addWidget(self.sum_SpinBox, 3, 1, 1, 1)
        # 设置范围
        self.sum_SpinBox.setMinimum(1)
        self.sum_SpinBox.setMaximum(120)
        # 设置单位
        self.sum_SpinBox.setSuffix(' s')
        # 设置默认时间
        self.sum_SpinBox.setValue(10)

        # 设置对应的回调函数
        self.retranslateUi(time_search)
        # 设置文件选择绑定槽
        self.file_pushButton.clicked.connect(self.msg)
        # 根据情况设置聚合时间
        self.search_comboBox.currentTextChanged.connect(self.sum_time)
        QtCore.QMetaObject.connectSlotsByName(time_search)



    # 设置对应内容的文字内容
    def retranslateUi(self, time_search):
        _translate = QtCore.QCoreApplication.translate
        time_search.setWindowTitle(_translate("time_search", "时间戳聚合查找"))
        self.start_pushButton.setText(_translate("time_search", "开始查找"))
        self.type_label.setText(_translate("time_search", "查找类型"))
        self.file_pushButton.setText(_translate("time_search", "文件选择"))
        self.file_LineEdit.setText(_translate("time_search", ""))
        self.word_label.setText(_translate("time_search", "查找词"))
        self.sum_label.setText(_translate("time_search", "聚合时间"))

    # 自定义函数
    # 文件选择
    def msg(self):
        type = self.search_comboBox.currentText()
        if type == "字幕":
            file_type = 'SRT File(*.srt)'
        else:
            file_type = 'xml File(*.xml)'
        fielenme, filetype = QtWidgets.QFileDialog.getOpenFileName(None,"请选择要添加的文件",'C:/',file_type)
        self.file_LineEdit.setText(fielenme)

    # 默认聚合时间选择函数
    def sum_time(self):
        type = self.search_comboBox.currentText()
        if type == "字幕":
            self.sum_SpinBox.setValue(60)
        else:
            self.sum_SpinBox.setValue(10)
