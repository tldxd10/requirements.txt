import random
import streamlit as st

st.set_page_config(page_title="가위바위보 대결", page_icon="🎮")
st.title("🎮 컴퓨터와 함께하는 가위바위보 한판!")
st.write("아래 버튼 중 하나를 눌러 컴퓨터에게 도전하세요!")

options = ["가위", "바위", "보"]
emojis = {"가위": "✌️", "바위": "✊", "보": "✋"}

col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "가위"
with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "바위"
with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "보"

if user_choice:
    computer_choice = random.choice(options)
    st.divider()
    st.subheader("⚔️ 대결 결과")

    c1, c2 = st.columns(2)
    with c1:
        st.info(f"👤 **나의 선택:** {emojis[user_choice]} {user_choice}")
    with c2:
        st.warning(f"🤖 **컴퓨터의 선택:** {emojis[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        st.warning("🤝 무승부입니다! 다시 도전해보세요.")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        st.balloons()
        st.success("🎉 축하합니다! 당신의 승리입니다!")
    else:
        st.error("😭 아쉽게도 컴퓨터가 이겼습니다!")
