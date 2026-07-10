# ch9_23.py
fruits = {'Orange':60, 'Apple':100, 'Grape':80}
print(f"原始水果字典 : {fruits}")

# 依據字典的鍵排序的串列 -- 水果名稱
fruits_key = sorted(fruits.items(), key=lambda item:item[0])
print(f"依據字典的鍵排序的串列 : {fruits_key}")
print(" 品項   價格")
for i in range(len(fruits_key)):
    print(f"{fruits_key[i][0]:6}   {fruits_key[i][1]}")

# 依據字典的值排序的串列 -- 售價
fruits_value = sorted(fruits.items(), key=lambda item:item[1])
print(f"依據字典的值排序的串列 : {fruits_value}")
print(" 品項   價格")
for i in range(len(fruits_value)):
    print(f"{fruits_value[i][0]:6}   {fruits_value[i][1]}")

