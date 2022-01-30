from Globals.globals import funcs
from peizhi.paqu import Paqu
class Option:
    def __init__(self,shuju):
        self.shuju = shuju

    def mokuai(self):
        return self.papage()

    def papage(self):
        url = funcs.URL(self.shuju)
        Pagedata = Paqu(url)
        jieshou = Pagedata.paqu()
        if(jieshou == '未检测到文件上传代码.'):
            print('''
            Put version=> 1.0 -_-
            未检测到文件上传代码.''')
            exit(1)
        else:
            return jieshou

    def File(self):
        print(self.shuju)
