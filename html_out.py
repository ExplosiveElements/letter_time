"""
# 组装html内容
# 输出html内容
# 打开对应网页
"""
import os
import html_context
def search_html(file_name,search_type,result_list):# 顺序为 时间、内容、（用户名）、（金额、持续时间）、（礼物数量）
    contextlen = len(result_list[0])
    data = """var data = ["""
    columns=''
    if search_type== '字幕':
        columns = """var columns = [{
                            field: 'Timestart',
                            title: '起始时间'
                        }, {
                            field: 'Timeover',
                            title: '终止时间'
                        },{
                            field: 'context',
                            title: '字幕内容'
                        }, ];"""
        for i in range(contextlen):

            data += """{
                        Timestart:'""" + result_list[0][i] + """',Timeover:'"""+result_list[1][i][:-1]+"""',context:" """ + result_list[2][i][:-1] + """ ",},"""
        data += """];"""
    elif search_type == '弹幕':
        columns = """var columns = [{
                                    field: 'Timepoint',
                                    title: '时间点'
                                }, {
                                    field: 'context',
                                    title: '弹幕内容'
                                }, {
                                    field: 'user',
                                    title: '用户名'
                                }, ];"""
        for i in range(contextlen):
            result_list[1][i] = repr(result_list[1][i])
            data += """{
                                Timepoint:'""" + result_list[0][i] + """',context:""" + result_list[1][i]+""",user:'""" + result_list[2][i]+ """',},"""
        data += """];"""
    elif search_type == 'sc':
        columns = """var columns = [{
                                           field: 'Timepoint',
                                           title: '时间点'
                                       }, {
                                           field: 'context',
                                           title: 'sc内容'
                                       }, {
                                           field: 'user',
                                           title: '用户名'
                                       }, {
                                           field: 'money',
                                           title: '金额'
                                       },{
                                           field: 'Duration',
                                           title: '持续时间'
                                       },];"""
        for i in range(contextlen):
            if result_list[1][i]== None:
                result_list[1][i]=''
            elif "\n" in result_list[1][i]:
                result_list[1][i] = result_list[1][i].replace('\n',' ')
            #print(result_list[0][i],result_list[1][i],result_list[2][i],result_list[3][i],result_list[4][i])
            data += """{
                                       Timepoint:'""" + result_list[0][i] + """',context:"""+ '"'+ result_list[1][i]+'"' + """,user:'""" + result_list[2][i] + """',money:'""" + result_list[3][i] +"""',Duration:'""" + result_list[4][i] +"""',},"""
        data += """];"""
    elif search_type == '礼物':
        columns = """var columns = [{
                                            field: 'Timepoint',
                                            title: '时间点'
                                        }, {
                                            field: 'context',
                                            title: '礼物名称'
                                        }, {
                                            field: 'user',
                                            title: '用户名'
                                        },{
                                            field: 'Giftcount',
                                            title: '礼物数量'
                                        }, ];"""
        for i in range(contextlen):
            data += """{
                                        Timepoint:'""" + result_list[0][i] + """',context:""" + '"'+ result_list[1][i]+'"' + """,user:'""" + result_list[2][i] +"""',Giftcount:'""" + result_list[3][i] + """',},"""
        data += """];"""
    file1 = file_name.split('/')[-1].split('.')[0]
    title = file1+'_'+search_type
    html = html_context.html_1 + title +html_context.html_2+columns+data+html_context.html_3
    if search_type == '字幕':
        html += html_context.html_6+html_context.html_5
    else:
        html += html_context.html_4+html_context.html_5
    if  os.path.exists(file1):
        pass
    else:
        os.makedirs(file1)
    f_result = open(file1+'/' + title + '.html', 'w', encoding='utf-8')
    f_result.writelines(html)
    f_result.close()

def stamp_html(time_stamp_list,wordlist,searchtype):
    columns = """var columns = [{
                    field: 'TimeInterval',
                    title: '时间区间'
                }, {
                    field: 'times',
                    title: '所含查找词次数'
                }, ];"""
    search_num = len(wordlist)
    for i in range(search_num):
        title = searchtype +'_'+ wordlist[i]+'_'+"""时间聚合结果展示"""
        data = """var data = ["""
        time_len = len(time_stamp_list[i])
        for time_count in range(0,time_len,2):
            data +="""{
            TimeInterval:'"""+ time_stamp_list[i][time_count]+"""',times:"""+time_stamp_list[i][time_count+1]+""",},"""
        data +="""];"""
        html = html_context.html_1 + title +html_context.html_2+columns+data+html_context.html_3
        if os.path.exists('result'):
            pass
        else:
            os.makedirs('result')
        f_result = open('result/'+title+'.html','w',encoding='utf-8')
        f_result.writelines(html)
        f_result.close()

if __name__ == '__main__':
    pass
