# ch35_5_1.py
import cv2

# 開啟預設攝影機, 預設是 0
cap = cv2.VideoCapture(0)
# 檢查攝影機是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# 取得攝影機畫面尺寸
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30                                    # 預設30幀/秒

# 建立影片寫入物件, 指定格式為mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('myvideo.mp4', fourcc, fps, (frame_width, frame_height))

print("開始錄影, 按 Esc 鍵結束")

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取畫面, 結束錄影")
        break
  
    cv2.imshow('Recording', frame)          # 顯示畫面  
    out.write(frame)                        # 寫入影片   
    if cv2.waitKey(1) == 27:                # 按 Esc 鍵結束錄影
        print("錄影結束")
        break

# 釋放資源
cap.release()
out.release()
cv2.destroyAllWindows()


