import sys
from peizhi.option import Option
import button

def mian():
    if(int(len(sys.argv)<=1) != True):
        fanhui = Option(sys.argv)
        jieshou = fanhui.mokuai()
        return jieshou
    else:
        print('''

        Put version=> 1.0 -_-

        python put.py --url 文件上传地址 --crawler 1
        
        #本工具会将fuzz测试成功信息保存在/cache/ip.txt文件里！
        ''')
        exit(1)

if __name__ == '__main__':
    data = mian()
    kaishi = button.Start(data)
    attack = kaishi.xuanze()
    kaishi.fire(attack)
