# 本文件用于将所有的txt文件生成一个target.txt文件，用于最终控制
import os

f_list = os.listdir()
target_files = []
for file_name in f_list:
    if os.path.splitext(file_name)[1] == '.txt':
        if os.path.splitext(file_name)[0] not in ['target','complexcommands','devices']:
            target_files.append(file_name)

print('读取到当前目录有以下指令文件')
print(target_files)

target_commands = {}
for file_name in target_files:
    f = open(file_name, 'r')
    fileTemp = f.read()
    commands = eval(fileTemp)
    f.close()
    target_commands.update(commands)

print('合并结束，保存target.txt文件')
fileName = 'target.txt'
f = open(fileName, 'w+')
f.write(str(target_commands))
f.close()
print('target.txt中包含如下指令')
for i in target_commands.items():
    print(i[0])