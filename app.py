import streamlit as st
from chatbot_logic import get_bot_reply

#BODY MỚI
def homestay_intro():
    # Banner
    st.markdown("""
        <div style="
            background-image: url('https://fulltimeexplorer.com/wp-content/uploads/2017/12/What-is-a-Homestay-2.jpg');
            background-size: cover;
            background-position: center;
            height: 300px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
        ">
            VHomestay - Trải nghiệm như ở nhà
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Giới thiệu
    st.markdown("""
    ### 🌿 Giới thiệu
    **VHomestay** mang đến không gian ấm cúng, gần gũi thiên nhiên,  
    phù hợp cho du lịch nghỉ dưỡng, cặp đôi và gia đình.
    """)

    # Danh sách phòng
    st.markdown("### ⭐ Dịch vụ nổi bật")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/139/139899.png", width=80)
        st.write("**Wifi miễn phí**")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1046/1046857.png", width=80)
        st.write("**Ăn sáng tại phòng**")

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=80)
        st.write("**View đẹp sống ảo**")

    # Dịch vụ
    st.markdown("### ⭐ Dịch vụ")
    st.markdown("""
    - 🚗 Đưa đón sân bay  
    - 🍳 Ăn sáng miễn phí  
    - 📶 Wifi tốc độ cao  
    - 🏍️ Thuê xe máy  
    """)

    # Đánh giá
    st.markdown("### 💬 Đánh giá khách hàng")
    st.info("“Phòng sạch đẹp, chủ thân thiện, giá hợp lý!” ⭐⭐⭐⭐⭐")
    st.info("“Không gian chill, rất đáng để quay lại.” ⭐⭐⭐⭐")


def homestay_app():

    #CSS
    st.markdown("""
        <style>
            body {
                background-color: #f5f5dc;
            }

            .footer {
                background-color: #f7f7f7;
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

            .block-container {
                padding-bottom: 60px; /* tránh bị footer đè */
            }
        </style>
    """, unsafe_allow_html=True)
    homestay_intro()

    #SIDEBAR
    st.sidebar.header("Trợ lý ảo VBot")
    st.sidebar.write("Xin chào! Tôi là trợ lý online của VHomestay. Bạn cần trợ giúp gì?")
    st.sidebar.write("(Bạn có thể hỏi tôi về giá phòng, địa điểm du lịch gần đây...)")

    if "conversation_log" not in st.session_state:
        st.session_state.conversation_log = [
            {"role": "assistant", "content": "Xin chào! Bạn cần hỗ trợ gì?"}
        ]

    for message in st.session_state.conversation_log:
        with st.sidebar.chat_message(message["role"]):
            st.sidebar.write(message["content"])

    if prompt := st.sidebar.chat_input("Nhập yêu cầu của bạn..."):
        st.session_state.conversation_log.append(
            {"role": "user", "content": prompt}
        )

        bot_reply = get_bot_reply(prompt)

        st.session_state.conversation_log.append(
            {"role": "assistant", "content": bot_reply}
        )

        st.rerun()

    #FOOTER
    st.markdown(
        '<div class="footer">© 2026 VHomestay - Tất cả các quyền được bảo lưu.</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    homestay_app()