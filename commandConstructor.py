# 用于获取IR遥控器的指令并组成控制指令字典文件，用于后续程序的读取
import broadlink
# 发现博联设备
devices = broadlink.discover(timeout=5)
print(devices)
print('Please select the device you want to use by number from 0\n')
selectNum = int(input())

if(devices[selectNum].auth()):
    pass
else:
    print('无法访问指定设备')

print('设备选择完毕，请按任意键开始学习指令')
input()


commands = {}
a = 1
while(True):
    print('请输入指令', a, '名称,如果输入stop则停止记录\n')
    name = input()
    if(name == 'stop'):
        break
    devices[selectNum].enter_learning()
    print('请按下遥控器对应按钮，完成后按任意键继续\n')
    input()
    print('当前获取的指令为:')
    command = devices[selectNum].check_data()
    print(command)
    print('是否保存?yes&no:')
    confrimation = input()
    if(confrimation == 'yes'):
        commands[name] = command
    else:
        pass
    a = a+1

print('学习结束，请输入保存文件名')
fileName = input()
f = open(fileName, 'w')
f.write(str(commands))
f.close()
