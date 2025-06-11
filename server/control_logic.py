import json

with open('command_mapping.json', 'r', encoding='utf-8') as f:

    command_table = json.load(f)

def execute_command(command):
    if command not in command_table:
        print(f"未知指令:{command}")
        return
    
    data = command_table[command]

    if command == "start_rotation":
        print(f"旋轉平台啟動:方向={data['direction']}，轉速={data['rpm']}rpm")

    elif command == "stop_rotation":
        print(f"平台旋轉已停止")

    elif command == "reverse_rotation":
        print(f"平台逆轉中:方向={data['direction']}，轉速={data['rpm']}rpm")

    elif command == "set_speed_60":
        print(f"調整轉速至{data['rpm']}rpm")

    elif command == "emergency_shutdown":
        print(f"緊急停止!所有系統已停機")

    else:
        print(f"執行:{data['description']}")