import switch

class Start:
    def __init__(self,shuju):
        self.shuju = shuju
        if(str(type(shuju)) == "<class 'dict'>"):
            jilu = open('jilu.txt','w+')
            jilu.write(str(shuju))
            jilu.close()
        else:
            pass#待开发
    def fire(self,attacks):#这里选择性导入攻击模块，进行fuzz测试。
        daoru = 'from fuzz.'+attacks+' import *'
        exec(daoru) #字符串代码执行函数

    def xuanze(self):
        huoqu = switch.Switch.Choose()
        return huoqu