# 通过读取录播机生成的xml文件搜索对应弹幕、super chat词输出对应时间戳文件
# 模块的引入
from bs4 import BeautifulSoup

def danmu_time(search_letter_list, type_name, file_name,sum_time):
    # 1.0 读取本项目中的文件 （本阶段最终版）
    with  open(file_name,"r",encoding='utf-8') as f:
        xml_s = f.read()
    xml_soup = BeautifulSoup(xml_s,'xml')
    # 2.1 选择查找内
    pp_list = search_letter_list  # 查找词列表
    pp_num = len(pp_list)  # 要查找词的数量
    pp_num_list = [0 for a in range(pp_num)]  # 对应匹配词数量计数
    # 每个搜索关键词对应的时间戳缓存合集
    buffer_search = []
    for search_num in range(pp_num):
        buffer_search.append([])
    # 查找内容的选择
    optional = type_name
    optional_node = ''
    if optional == '弹幕':
        optional_node = 'd'
    elif optional == 'sc':
        optional_node = 'sc'
    elif optional == '礼物':
        optional_node = 'gift'
    # 3.1 进行同时查找1.0版本,针对3个词进行同一匹配 （阶段最终版）
    text_buffer = xml_soup.find_all(optional_node) # 对应寻找内容的缓存
    # 进行查找
    for each_node in text_buffer:
        for pp_num_s in range(pp_num):
            if optional_node in ['d','sc']:
                if pp_list[pp_num_s] in each_node.string:
                    if optional_node == 'd':
                        buffer_search[pp_num_s].append(each_node.attrs['p']+"\n")
                    else:
                        buffer_search[pp_num_s].append(each_node.attrs['ts']+"\n")
                    pp_num_list[pp_num_s] += 1  # 匹配计数
            elif optional_node == 'gift':
                if pp_list[pp_num_s] in each_node.attrs['giftname']:
                    buffer_search[pp_num_s].append(each_node.attrs['ts'] + "\n")
                    pp_num_list[pp_num_s] += 1 # 匹配计数
    # 4.输出对应的内容的时间戳
    # 4.1 时间戳聚合
    time_stamp_list = time_stamp_polymerization(pp_num, pp_num_list, buffer_search,sum_time)
    print('\n查找完成\n结果在result文件夹中。\n文件名为：'+optional+'_'+'‘查找词’_‘匹配数量’')
    f.close()
    return time_stamp_list

# 4.1 时间戳聚合函数
def time_stamp_polymerization(search_number,search_count,buffer_search,sum_time):
    time_polymerization_mark_list = []
    for letter_number in range(search_number):
        time_polymerization_mark = [0 for a in range(search_count[letter_number])]
        time_polymerization_mark_list.append(time_polymerization_mark)
        # 对弹幕、gift和sc时间戳格式处理以及聚合标记
    for letter_number in range(search_number):
        buffer_mark_count =1
        # 弹幕、sc，gift时间戳聚合标签标注
        buffer_time_count = search_count[letter_number]
        # print(buffer_time[0][0],buffer_time[0][1])
        if buffer_time_count>=2:
            for x in range(1,buffer_time_count):
                if float(buffer_search[letter_number][x].split('.')[0])-float(buffer_search[letter_number][x-1].split('.')[0]) < sum_time:# 此处用于控制窗口，下个版本改进的地方
                    # print(buffer_time[1][x-1])
                    time_polymerization_mark_list[letter_number][x-1] = buffer_mark_count
                    time_polymerization_mark_list[letter_number][x] = buffer_mark_count
                    # print(buffer_mark_count)
                else:
                    buffer_mark_count += 1
    # 对弹幕、sc，gift幕时间戳进行聚合
    # print(time_polymerization_mark_list)
    time_stamp_list = [[] for a in range(search_number)]
    for letter_number in range(search_number):
        result = {}
        for index,kw in enumerate(time_polymerization_mark_list[letter_number]):
            if kw not in result.keys():
                result[kw] = [index]
            else:
                result.get(kw).append(index)
        for k,v in result.items():
            if (len(v) != 1)&(k!=0):
                start_tamp = buffer_search[letter_number][v[0]].split('.')[0]
                end_tamp = buffer_search[letter_number][v[-1]].split('.')[0]
                time_start_str = str(int(start_tamp)//3600)+':'+str(int(start_tamp)//60%60)+':'+str(int(start_tamp)%60)
                time_end_str = str(int(end_tamp)//3600)+':'+str(int(end_tamp)//60%60)+':'+str(int(end_tamp)%60)
                tamp_str = time_start_str + '-->' + time_end_str
                time_stamp_list[letter_number].append(tamp_str)
                time_stamp_list[letter_number].append(str(len(v)))
    return time_stamp_list


if __name__ == '__main__':
    pass