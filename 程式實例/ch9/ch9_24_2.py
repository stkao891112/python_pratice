# ch9_24_2.py
# AI客服機器人的資料庫
faq_db = {
    "營業時間": "我們營業時間為每天早上 8:00 至晚上 9:00",
    "地址": "本店位於台北市大安區敦化南路二段 46 號",
    "招牌商品": "我們的招牌是「經典手沖咖啡」以及「藍莓起司蛋糕」",
    "推薦飲品": "推薦您試試我們的拿鐵咖啡, 口感滑順濃郁!",
}

def ai_customer_service(question: str):
    # 使用match-case判斷問題的關鍵字
    match question:
        case {"intent": "詢問", "type": "營業時間"}:
            return faq_db["營業時間"]
        case {"intent": "詢問", "type": "地址"}:
            return faq_db["地址"]
        case {"intent": "推薦", "category": "甜點"}:
            return faq_db["招牌商品"]
        case {"intent": "推薦", "category": "飲料"}:
            return faq_db["推薦飲品"]
        case _:
            return "很抱歉, 我不太明白您的問題, 您可以換個方式再問一次嗎?"

# 模擬顧客的詢問
user_question_1 = {"intent": "詢問", "type": "營業時間"}
user_question_2 = {"intent": "推薦", "category": "甜點"}
user_question_3 = {"intent": "詢問", "type": "地址"}
user_question_4 = {"intent": "其他"}

# 回覆顧客
print(ai_customer_service(user_question_1))
print(ai_customer_service(user_question_2))
print(ai_customer_service(user_question_3))
print(ai_customer_service(user_question_4))









