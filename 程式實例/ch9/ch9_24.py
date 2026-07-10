# ch9_24.py
fruits = {'Orange':60, 'Apple':100, 'Grape':80}

# 按值排序字典並創建一個新的字典
fruits_sort = {k: v for k, v in sorted(fruits.items(), key=lambda item: item[1])}
print(f"依據字典的值排序的字典 : {fruits_sort}")

