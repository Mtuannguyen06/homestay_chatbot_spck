# chatbot_logic.py
import os
import json
import pandas as pd
import google.generativeai as genai

from dotenv import load_dotenv

# Setup API
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# Load config ban đầu của LLM
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    functions = config.get('function', 'giới thiệu homestay')
    initial_bot_message = config.get('initial_bot_message', 'Xin chào! Bạn cần hỗ trợ gì?')

# Load nội dung menu
room_df = pd.read_csv("rooms.csv", index_col=[0])

# Tạo LLM
model = genai.GenerativeModel("gemini-2.5-flash",
                              system_instruction=f"""
                              Bạn tên là VBot, một trợ lý AI có nhiệm vụ hỗ trợ giải đáp thông tin cho khách hàng của homestay V.
                              Các chức năng mà bạn hỗ trợ gồm: {', '.join(room_df['name'].to_list())}.
                              Tự động nhận biết và trả lời bằng tiếng Việt hoặc tiếng Anh theo ngôn ngữ của khách.
                              Nếu không chắc, hỏi lại khách muốn dùng ngôn ngữ nào.
                              Giúp khách đặt phòng
                              Check-in / Check-out:
                              Giờ check-in tiêu chuẩn.
                              Giờ check-out tiêu chuẩn.
                              Thông tin về check-in sớm / check-out muộn (nếu có)
                              Gợi ý quán ăn, cà phê, đặc sản địa phương gần khách sạn
                              Gợi ý địa điểm du lịch, tham quan, vui chơi trong bán kính gần
                              Mỗi gợi ý nên kèm:
                              Khoảng cách / thời gian di chuyển
                              Phù hợp cho ai (gia đình, cặp đôi, đi một mình…)
                              Hãy sử dụng lại lịch sử trò chuyện để đưa ra hỗ trợ có ích hơn.
                              Đối với các câu hỏi ngoài chức năng mà bạn hỗ trợ, trả lời bằng 'Tôi đang không hỗ trợ chức năng này. Xin liên hệ nhân viên homestay V để biết thêm thông tin.'
                              """
)

# Hàm xử lý logic chatbot
def get_bot_reply(prompt):
    # Kiểm tra xem prompt có đề cập đến menu không
    if "menu" in prompt.lower() or "món" in prompt.lower():
        return '\n\n'.join([f"**{row['name']}**: {row['description']}" for _, row in room_df.iterrows()])
    else:
        # Sử dụng LLM để tạo câu trả lời
        response = model.generate_content(prompt)
        return response.text
