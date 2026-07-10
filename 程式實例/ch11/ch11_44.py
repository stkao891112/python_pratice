# ch11_44.py
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

a, b = eval(input("請輸入2個整數值 : "))
print("最大公因數是 : ", gcd(a, b))





