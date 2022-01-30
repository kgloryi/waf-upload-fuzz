import re

class funcs:
    def URL(data):
        for x in range(len(data)):
            if(data[x] == '--url'):
                url = data[x+1]
                break
            else:
                pass
        return url

    def zhengze(data):
        guize = re.compile('<form.+enctype="multipart/form-data">[\d\D]+</form>')
        if(guize.findall(data)):
            shuju1 = guize.findall(data)[0]
            guize = re.compile('<input.+>')
            if(guize.findall(shuju1)):
                shuju2 = guize.findall(shuju1)
                bianliangming = [] #文件上传变量名
                bianliangming2 = [] #提交按钮变量名
                bianliangming3 = [] #杂项变量名
                zhenghe = {}
                guize = re.compile('name="\w*"|name=\'\w*\'')
                guize2 = re.compile('value="\w*"|value=\'\w*\'')
                guize3 = re.compile('[^.]value="\w*"|[^.]value=\'\w*\'')
                for x in shuju2:
                    if('type="file"' in x or 'type=\'file\'' in x):
                        bianliangming.append(guize.findall(x)[0])
                    elif(('type="submit"' in x or 'type=\'submit\'' in x) and 'value=' in x):
                        bianliangming2.append(guize.findall(x)[0])
                        bianliangming2.append(guize3.findall(x)[0])
                    else:
                        try:
                            bianliangming3.append(guize.findall(x)[0])
                            if (guize3.findall(x)):
                                bianliangming3.append(guize3.findall(x)[0])
                            else:
                                pass
                        except:
                            pass
                if(len(bianliangming)==0):
                    print('''
                    未检测到文件上传代码.
                    ''')
                    exit(1)
                zhenghe['上传变量名'] = bianliangming
                zhenghe['提交按钮变量名'] = bianliangming2
                zhenghe['杂项变量名'] = bianliangming3
                return zhenghe
            else:
                return '未检测到文件上传代码.'
        else:
            return '未检测到文件上传代码.'