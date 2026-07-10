# ch8_21.py
point = (3, 0)

match point:
    case (0, 0):
        print("原點位置")
    case (x, 0):
        print(f"在 X 軸上, X 座標是{x}")
    case (0, y):
        print(f"在 Y 軸上, Y 座標是{y}")
    case (x, y):
        print(f"一般座標點, X座標是{x}, Y座標是{y}")
    case _:
        print("無效點")



