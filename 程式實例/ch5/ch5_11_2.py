# ch5_11_2.py
response = eval(input("請輸入系統回應 : "))

match response:
    case 200:
        print("請求成功")
    case 400 | 401 | 403:
        print("客戶端錯誤")
    case 404:
        print("找不到資源")
    case 500:
        print("伺服器錯誤")
    case _:
        print("未知錯誤")


