# app.py
import streamlit as st

st.set_page_config(page_title="게임 추천기", page_icon="🎮")

st.title("🎮 문장 기반 게임 추천기")
st.write("원하는 분위기나 취향을 문장으로 입력하면 게임을 추천해줍니다.")

user_input = st.text_area(
    "예시: 스토리가 깊고 자유도가 높은 RPG 하고 싶어",
    height=120
)

# 아주 간단한 키워드 기반 추천 함수
def recommend_game(text):
    text = text.lower()

    if "rpg" in text or "스토리" in text:
        return "🧙 추천 게임: The Witcher 3"

    elif "공포" in text or "무서운" in text:
        return "👻 추천 게임: Resident Evil Village"

    elif "fps" in text or "총" in text or "슈팅" in text:
        return "🔫 추천 게임: Call of Duty"

    elif "힐링" in text or "농장" in text:
        return "🌱 추천 게임: Stardew Valley"

    elif "전략" in text:
        return "♟️ 추천 게임: Civilization VI"

    elif "오픈월드" in text:
        return "🌍 추천 게임: GTA V"

    else:
        return "🎲 추천 게임: Minecraft"

if st.button("추천 받기"):
    if user_input.strip():
        result = recommend_game(user_input)
        st.success(result)
    else:
        st.warning("문장을 입력해주세요.")
