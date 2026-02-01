# homestay_chatbot.py
import openai
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setup API
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# Load config ban đầu của LLM
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    initial_bot_message = config.get('initial_bot_message', 'Xin chào! Bạn cần hỗ trợ gì?')

# Tạo mô hình Chatbot
model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=f"""
    Bạn tên là VBot, một trợ lý AI có nhiệm vụ hỗ trợ giải đáp thông tin cho khách hàng của homestay V.
    Hãy sử dụng lại lịch sử trò chuyện để đưa ra hỗ trợ có ích hơn.
    Đối với các câu hỏi ngoài chức năng mà bạn hỗ trợ, trả lời bằng 'Tôi đang không hỗ trợ chức năng này. Xin liên hệ nhân viên homestay V để biết thêm thông tin.'
""")

def get_bot_reply(prompt):
    response = model.generate_content(prompt)
    return response.text
