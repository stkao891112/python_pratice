# ch38_3.py 
import openai
# 設定API金鑰
openai.api_key = 'OPENAI_API_KEY'
# 定義對話函數
def mychat(messages):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=150  # 限制回應token數
    )
    return response.choices[0].message.content
# 定義生成圖片的函數
def generate_image(prompt):
    response = openai.images.generate(
        model="dall-e-3",
        prompt = prompt,
        n = 1,
        size = "1024x1024",
        quality = "hd"
    )
    return response.data[0].url
print("歡迎來到深智 Deepwisdom 客服中心")
# 初始化對話串列
messages = [{"role": "system", "content": "你是深智公司客服人員"}]

# 執行對話
while True:
    user_input = input("    客戶 : ")
    if user_input.lower() == "bye":
        print("深智客服 : 感謝您的諮詢，祝您有美好的一天！")
        break
    if user_input.lower().startswith("生成圖片:"):
        prompt = user_input[5:]
        image_url = generate_image(prompt)
        print(f"深智客服 : 這是您要求的圖片:{image_url}")
    else:
        messages.append({"role": "user", "content": user_input})
        response = mychat(messages)
        print("深智客服 : " + response)
        messages.append({"role": "assistant", "content": response})


