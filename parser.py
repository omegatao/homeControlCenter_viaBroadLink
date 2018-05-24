# 根据指令调用对应设备发射对应类型的对应动作
# 指令格式 房间-指令类型(复合指令CC or 简单指令SC)-指令名称（指令字典中的键值）
import broadlink


def readDict(file_name):
    f=open(file_name,'r')
    dictInFile=eval(f.read())
    f.close
    return dictInFile

def getController(room_name,device_dict):
    print(room_name)
    print(device_dict)
    print('\n')
    devices=broadlink.discover(timeout=2)
    print(devices)
    for dev in devices:
        if dev.mac==device_dict[room_name]:
            return dev

def parser(instruct):
    # 获取设备字典devicesMac
    devicesMac=readDict('devices.txt')
    # 获取组合指令指令字典complexcommands
    complexcommands = readDict('complexcommands.txt')
    #获取简单指令字典commands
    commands=readDict('target.txt')

    #分解指令
    instruct_list=instruct.split('-')

    #获取指定房间对应设备
    activeControler=getController(instruct_list[0],devicesMac)
    activeControler.auth()

    #对简单指令和复杂指令分别处理
    #处理简单指令
    if instruct_list[1]=='SC':
        activeControler.send_data(commands[instruct_list[2]])

    






