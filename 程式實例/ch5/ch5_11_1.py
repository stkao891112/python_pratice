# ch5_11_1.py
command = input("請輸入狀態 : ")

match command:
    case "start":
        print("系統啟動中")
    case "stop":
        print("系統停止中")
    case "pause":
        print("系統暫停")
    case _:
        print("無效的指令")



