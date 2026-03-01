import streamlit as st
from chatbot_logic import get_bot_reply

# Giới thiệu về Homestay (Hiển thị phần giới thiệu ngoài Sidebar)
def homestay_intro():
    st.title("VHomestay - Nơi nghỉ dưỡng tuyệt vời")
    st.markdown("""
    **VHomestay** mang đến cho bạn trải nghiệm tuyệt vời với không gian ấm cúng, 
    phòng nghỉ tiện nghi, dịch vụ chuyên nghiệp và giá cả hợp lý.
    """)
    st.image(
        "https://fulltimeexplorer.com/wp-content/uploads/2017/12/What-is-a-Homestay-2.jpg",
        use_container_width=True
    )

# Giao diện chính với chatbot trong Sidebar
def homestay_app():
    # ===== CSS để đưa sidebar sang bên phải =====
    st.markdown(
        """
        <style>
            /* Đưa Sidebar sang bên phải */
            .css-1v3fvcr {
                flex-direction: row-reverse;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # ===== Phần giới thiệu bên ngoài Sidebar =====
    homestay_intro()  # Hiển thị thông tin Homestay ngoài sidebar

    # ===== Phần chatbot trong Sidebar =====
    st.sidebar.header("Trợ lý ảo VBot")
    st.sidebar.write("Xin chào! Tôi là trợ lý online của VHomestay. Bạn cần trợ giúp gì?")
    st.sidebar.write("(Bạn có thể hỏi tôi về giá phòng, địa điểm du lịch gần đây...)")

    if "conversation_log" not in st.session_state:
        st.session_state.conversation_log = [
            {"role": "assistant", "content": "Xin chào! Bạn cần hỗ trợ gì?"}
        ]

    # Hiển thị lịch sử trò chuyện trong sidebar
    for message in st.session_state.conversation_log:
        with st.sidebar.chat_message(message["role"]):
            st.sidebar.write(message["content"])

    # Nhập nội dung mới cho chatbot
    if prompt := st.sidebar.chat_input("Nhập yêu cầu của bạn..."):
        st.session_state.conversation_log.append(
            {"role": "user", "content": prompt}
        )

        bot_reply = get_bot_reply(prompt)

        st.session_state.conversation_log.append(
            {"role": "assistant", "content": bot_reply}
        )

        st.rerun()  # Gọi st.rerun() thay vì st.sidebar.rerun()

if __name__ == "__main__":
    homestay_app()