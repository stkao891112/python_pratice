# ch11_39_7.py
import time
# 創意裝飾器 - 智慧型執行計時
def smart_timer(threshold=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()        # 計時開始
            result = func(*args, **kwargs)
            end_time = time.time()          # 計時結束
            
            duration = end_time - start_time
            print(f"函數 '{func.__name__}' 執行時間:{duration:.4f} 秒")
            
            # 智慧提示 - 超過時間閾值時提醒
            if duration > threshold:
                print(f"'{func.__name__}' 執行時間超過建議值 {threshold:.2f} 秒,建議優化")
            else:
                print(f"'{func.__name__}' 執行效率良好")
            
            return result
        return wrapper
    return decorator

# 測試函數1 - 快速執行的函數
@smart_timer(threshold=0.5)
def fast_function():
    time.sleep(0.3)
    return "快速函數完成"
# 測試函數2 - 較慢的函數
@smart_timer(threshold=0.5)
def slow_function():
    time.sleep(0.8)
    return "慢速函數完成"
# 執行測試
print(fast_function())
print('-'*30)
print(slow_function())







