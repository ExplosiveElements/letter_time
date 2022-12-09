# 通过读取ssr-> txt的文件中查找对应的文字片段而导出对应的时间戳
"""
1. 读取文件
1.1 输入需要查找的类型（包括：字幕）
1.2 输入需要查找的文件
1.3 读取对应文件
2. 输入需要查找的文字内容
2.1 同时查找3个词
3. 进行自动化查找对应的内容
3.1 进行同时查找1.0版本,针对3个词进行同一匹配
4. 输出对应的内容的时间戳
4.1 时间戳聚合
4.2 输出对应的文件
"""

def zimu_time(search_letter_list,file_name,sum_time):
    # 1.0 读取本项目中的文件
    f =  open(file_name,"r",encoding='utf-8')
    # 2.1 同时查找3个词。
    pp_list = search_letter_list # 查找词列表
    pp_num = len(pp_list) # 要查找词的数量
    pp_num_list = [0 for a in range(pp_num)] # 对应匹配词数量计数
    buffer_form = [] # 每一个部分的文本的缓存列表
    count_txt = 0 # 每一个部分的文本的缓冲计数器
    # 每个搜索关键词对应的时间戳缓存合集
    buffer_search = []
    for search_num in range(pp_num):
        buffer_search.append([])
    # 3.1 进行同时查找1.0版本,针对3个词进行同一匹配
    for each_line in f:
        if count_txt == 4:
            for pp_num_s in range(pp_num):
                if pp_list[pp_num_s] in buffer_form[2]:
                    buffer_search[pp_num_s].append(buffer_form[1])
                    pp_num_list[pp_num_s] += 1
            buffer_form.clear()
            count_txt = 0
        # 记录每个部分文本和计数器
        buffer_form.append(each_line)
        count_txt += 1
    # 4.输出对应的内容的时间戳即对应内容
    # 4.1 时间戳聚合
    time_stamp_list = time_stamp_polymerization(pp_num,pp_num_list, buffer_search,sum_time)
    #print(time_stamp_list)
    # print(buffer_search,pp_num_list)
    #4.2 输出对应的文件
    print('\n查找完成\n结果在result文件夹中。\n文件名为：字幕_‘查找词’_‘匹配数量’')
    return time_stamp_list

# 4.1 时间戳聚合函数
def time_stamp_polymerization(search_number,search_count,buffer_search,sum_time):
    time_polymerization_mark_list = []
    for letter_number in range(search_number):
        time_polymerization_mark = [0 for a in range(search_count[letter_number])]
        time_polymerization_mark_list.append(time_polymerization_mark)
        # 对字幕时间戳格式处理以及聚合标记
    for letter_number in range(search_number):
        # 对字幕的时间戳处理
        buffer_time = [[], []]
        buffer_mark_count =1
        for timestamp_str in buffer_search[letter_number]:
            timestamp_start = int(timestamp_str[0:2]) * 3600 + int(timestamp_str[3:5]) * 60 + int(timestamp_str[6:8])
            timestamp_end = int(timestamp_str[-13:-11]) * 3600 + int(timestamp_str[-10:-8]) * 60 + int(
                timestamp_str[-7:-5])
            #print(timestamp_start,timestamp_end)
            buffer_time[0].append(timestamp_start)
            buffer_time[1].append(timestamp_end)
        # 字幕时间戳聚合标签标注
        buffer_time_count = len(buffer_time[0])
        # print(buffer_time[0][0],buffer_time[0][1])
        if buffer_time_count>=2:
            for x in range(1,buffer_time_count):
                if buffer_time[0][x] - buffer_time[1][x-1] < sum_time:
                    # print(buffer_time[1][x-1])
                    time_polymerization_mark_list[letter_number][x-1] = buffer_mark_count
                    time_polymerization_mark_list[letter_number][x] = buffer_mark_count
                    # print(buffer_mark_count)
                else:
                    buffer_mark_count += 1
    # 对字幕时间戳进行聚合
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
                tamp_str = buffer_search[letter_number][v[0]][0:12] + '-->' + buffer_search[letter_number][v[-1]][-13:-2]
                time_stamp_list[letter_number].append(tamp_str)
                time_stamp_list[letter_number].append(str(len(v))+'\n')
    return time_stamp_list

if __name__ == '__main__':
    pass

