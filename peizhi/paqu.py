import requests
import re,os
from Globals.globals import funcs

class Paqu:
    def __init__(self,url):
        self.url = url

    def paqu(self):
        try:
            page = requests.get(self.url)
            ip = open(os.getcwd()+'\\cache\\'+'ip.txt','w+')
            ip.write(self.url)
            ip.close()
        except:
            print('''
            确保url地址无误!
            ''')
            exit(1)
        huoqu = funcs.zhengze(page.text)
        return huoqu