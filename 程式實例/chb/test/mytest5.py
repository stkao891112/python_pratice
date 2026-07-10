# 計算1加到n的總和

def sum_1_to_n(n):
    """回傳1加到n的總和"""
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = int(input("請輸入n: "))
    print(f"1加到{n}的總和為: {sum_1_to_n(n)}")
