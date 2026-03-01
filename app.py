import streamlit as st
from chatbot_logic import get_bot_reply

# Giới thiệu về Homestay (Phần Body)
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
    # ===== CSS cho Layout (Header, Body, Footer) với nền màu sáng beige =====
    st.markdown(
        """
        <style>
            /* Toàn bộ background */
            body {
                background-color: #f5f5dc; /* Nền màu beige sáng */
                margin: 0;
                padding: 0;
            }

            /* Header */
            .header {
                background-color: #70c1b3;  /* Xanh nhạt nhẹ */
                padding: 20px;
                color: white;
                text-align: center;
                font-size: 30px;
                font-weight: bold;
                border-radius: 10px;
            }

            /* Footer */
            .footer {
                background-color: #f7f7f7;  /* Màu xám sáng */
                padding: 10px;
                text-align: center;
                font-size: 14px;
                color: #333;
                position: fixed;
                bottom: 0;
                width: 100%;
                border-top: 1px solid #ddd;
                left: 0;
                right: 0;
            }

            /* Body */
            .body-content {
                margin-bottom: 60px;  /* Để tránh che footer */
            }

            /* Sidebar */
            .css-1v3fvcr {
                background-color: #ffffff; /* Sidebar trắng sáng */
            }

            .sidebar .sidebar-content {
                background-color: #e3f2f1; /* Xanh nhạt cho phần sidebar */
            }

            /* Đảm bảo nội dung có đủ chiều cao để đẩy footer xuống dưới */
            .main {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # ===== Wrapper để đảm bảo layout không bị che khuất =====
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # ===== Header =====
    st.markdown('<div class="header">VHomestay - Nơi nghỉ dưỡng tuyệt vời</div>', unsafe_allow_html=True)

    # ===== Body =====
    st.markdown('<div class="body-content">', unsafe_allow_html=True)
    
    # Phần giới thiệu về Homestay (Body Content)
    homestay_intro()

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

        st.rerun()  # Gọi st.rerun() để làm mới ứng dụng

    st.markdown('</div>', unsafe_allow_html=True)  # Đóng body content

    # ===== Footer =====
    st.markdown('<div class="footer">© 2026 VHomestay - Tất cả các quyền được bảo lưu.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Đóng wrapper chính

if __name__ == "__main__":
    homestay_app()