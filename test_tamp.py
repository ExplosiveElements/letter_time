import timesearch,transsearch
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from main import *
from PyQt5 import QtCore

# 查找窗口
class time_search_window(QWidget,timesearch.Ui_time_search):
    # 设置查找结果的传递信号
    search_result = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(505, 300)
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.retranslateUi(self)
        # 设置开始查找按钮绑定搜索结果窗口展示函数
        self.start_pushButton.clicked.connect(self.time_out)

    # 查找参数传递函数
    def time_out(self):
        type1 = self.search_comboBox.currentText()
        wordlist = self.word_lineEdit.text().split()
        sumtime = self.sum_SpinBox.value()
        file_name = self.file_LineEdit.text()
        # 开始搜索
        time_stamp_list,wordlist,searchtype = search_start(type1, wordlist, sumtime, file_name)
        stamp_html(time_stamp_list, wordlist, searchtype)

# 转化窗口
class trans_window(QWidget,transsearch.Ui_trans):
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(507, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win1 = time_search_window()
    win2= trans_window()
    win1.show()
    win2.show()
    sys.exit(app.exec_())