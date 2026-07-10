# ch9_22.py
my_dict = {'Orange':60, 'Apple':100, 'Grape':80}
sorted_dict_by_key = {k: my_dict[k] for k in sorted(my_dict)}
print(f"依據 key 排序的新字典 = {sorted_dict_by_key}")



