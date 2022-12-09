from bs4 import BeautifulSoup
def trans(type1,file_name):
    result_list=[]
    f=open(file_name,"r",encoding='utf-8')
    time = []
    context = []
    if type1 == '字幕':
        time_start = []
        time_over = []
        buffer_form = []  # 每一个部分的文本的缓存列表
        count_txt = 0  # 每一个部分的文本的缓冲计数器
        for each_line in f:
            if count_txt == 4:
                time_start.append(buffer_form[1][0:12])
                time_over.append(buffer_form[1][-13:])
                context.append(buffer_form[2])
                buffer_form.clear()
                count_txt = 0
            # 记录每个部分文本和计数器
            buffer_form.append(each_line)
            count_txt += 1
        result_list=[time_start,time_over,context]
    else:
        xml_s = f.read()
        xml_soup = BeautifulSoup(xml_s, 'xml')
        optional = type1
        optional_node = ''
        user = []
        if optional == '弹幕':
            optional_node = 'd'
        elif optional == 'sc':
            optional_node = 'sc'
        elif optional == '礼物':
            optional_node = 'gift'
        money =[]
        Duration =[]
        Giftcount = []
        text_buffer = xml_soup.find_all(optional_node)
        for each_node in text_buffer:
            if optional_node == 'd':
                time.append(each_node.attrs['p'].split('.')[0]+'.'+each_node.attrs['p'].split('.')[1][:3])
                context.append(each_node.string)
                user.append(each_node.attrs['user'])
            elif optional_node== 'sc':
                time.append(each_node.attrs['ts'] )
                context.append(each_node.string)
                user.append(each_node.attrs['user'])
                money.append(each_node.attrs['price'])
                Duration.append(each_node.attrs['time'])
            elif optional_node == 'gift':
                time.append(each_node.attrs['ts'] )
                context.append(each_node.attrs['giftname'])
                user.append(each_node.attrs['user'])
                Giftcount.append(each_node.attrs['giftcount'])
        if optional_node == 'd':
            result_list = [time,context,user]
        elif optional_node == 'sc':
            result_list = [time,context,user,money,Duration]
        elif optional_node == 'gift':
            result_list = [time,context,user,Giftcount]
    f.close()
    return result_list