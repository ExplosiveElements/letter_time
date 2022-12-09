"""
程序后台主函数
作为总的函数的聚合，并转到对应的函数进行处理
"""
# 模块的引入
import dammu,zimu
from html_out import *
from trans import *

# 后台函数
def search_start(searchtype,wordlist,sumtime,file_name):
    if searchtype == '字幕':
        time_stamp_list = zimu.zimu_time(wordlist,file_name,sumtime)
    else:
        time_stamp_list= dammu.danmu_time(wordlist, searchtype, file_name,sumtime)
    return time_stamp_list,wordlist,searchtype

def test():
    type1 = "sc"
    file_name ="D:/录播/22673512-扇宝/录制-扇宝-22673512-20221119-【涂鸦回】总之我们画画看.xml"
    result_list = trans(type1, file_name)
    search_html(file_name, type1, result_list)

if __name__ == '__main__':
    test()

