import streamlit as st
from chatbot_logic import get_bot_reply  # Import hàm xử lý logic từ homestay_chatbot.py

# Giới thiệu về Homestay
def homestay_intro():
    st.title("VHomestay - Nơi nghỉ dưỡng tuyệt vời")
    st.markdown("""
    **VHomestay** mang đến cho bạn trải nghiệm tuyệt vời với không gian ấm cúng, phòng nghỉ tiện nghi, 
    dịch vụ chuyên nghiệp và giá cả hợp lý. Hãy cùng khám phá các phòng nghỉ của chúng tôi!
    """)
    st.image("https://fulltimeexplorer.com/wp-content/uploads/2017/12/What-is-a-Homestay-2.jpg", caption="VHomestay - Nơi nghỉ dưỡng tuyệt vời", use_container_width=800)

# Giao diện Chatbot
def homestay_chatbot():
    # Tạo cột Chatbot ở bên phải
    col1, col2 = st.columns([2, 1])  # 2 phần cột cho thông tin Homestay, 1 phần cột cho Chatbot

    with col1:
        # Phần thông tin homestay
        homestay_intro()

    with col2:
        # Phần giao diện Chatbot
        st.header("Trợ lý ảo VBot")
        st.write("Xin chào! Tôi là trợ lý online của VHomestay. Bạn cần trợ giúp gì?")
        st.write("(Bạn có thể hỏi tôi về giá phòng, địa điểm du lịch gần đây...)")

        # Nếu chưa có lịch sử trò chuyện
        if 'conversation_log' not in st.session_state:
            st.session_state.conversation_log = [{"role": "assistant", "content": "Xin chào! Bạn cần hỗ trợ gì?"}]

        # Hiển thị lịch sử trò chuyện
        for message in st.session_state.conversation_log:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # Khi người dùng nhập yêu cầu
        if prompt := st.chat_input("Nhập yêu cầu của bạn tại đây..."):
            # Hiển thị prompt của người dùng
            with st.chat_message("user"):
                st.write(prompt)
            # Thêm vào lịch sử trò chuyện
            st.session_state.conversation_log.append({"role": "user", "content": prompt})

            # Lấy câu trả lời từ chatbot logic
            bot_reply = get_bot_reply(prompt)

            # Hiển thị câu trả lời từ bot
            with st.chat_message("assistant"):
                st.write(bot_reply)

            # Thêm vào lịch sử trò chuyện
            st.session_state.conversation_log.append({"role": "assistant", "content": bot_reply})

# Chạy ứng dụng Streamlit
def homestay_app():
    homestay_chatbot()  # Hiển thị cả thông tin homestay và chatbot

# Gọi hàm để chạy ứng dụng
if __name__ == "__main__":
    homestay_app()
