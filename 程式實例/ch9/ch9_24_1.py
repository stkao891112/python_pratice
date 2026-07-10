# ch9_24_1.py
user = {"name": "Alice", "age": 30}

match user:
    case {"name": "Alice", "age": age}:
        print(f"Alice 的年齡是 {age}")
    case {"name": "Bob", "age": age}:
        print(f"Bob 的年齡是 {age}")
    case _:
        print("未知使用者")



