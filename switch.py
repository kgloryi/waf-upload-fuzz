import os

class Switch:

    def zifucuanpinjie():
        zifuchuan = '''
        选择攻击方式:
        
        '''
        wenjianshuliang = len(os.listdir(os.getcwd()+'\\fuzz'))#返回目录下所有文件和文件夹
        wenjianming = os.listdir(os.getcwd()+'\\fuzz')
        global hebing
        hebing = []
        for x in range(wenjianshuliang):
            if('.py' in wenjianming[x]):
                xieru = str(x)+'.'+wenjianming[x][:-3]
                zifuchuan += xieru+'\n'+'        '
                hebing.append(xieru)
            else:
                pass
        return zifuchuan+'\n'+'please input:'

    def Choose():
        shilihua = Switch.zifucuanpinjie()
        attack = input(shilihua)
        for x in hebing:
            if(str(attack) in x):
                return x[2:]
            else:
                pass
        print('''
        请选择选项!
        ''')
        return Switch.Choose()
