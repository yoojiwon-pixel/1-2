# app.py
import random
import streamlit as st

st.set_page_config(page_title="고급 게임 추천기", page_icon="🎮")

st.title("🎮 문장 기반 게임 추천 AI")
st.write("문장을 입력하면 장르를 분석해서 게임을 추천합니다.")

# -----------------------------
# 대용량 게임 데이터 생성
# 실제 서비스에서는 DB/API 사용 권장
# -----------------------------

genres = {
    "rpg": "RPG",
    "fps": "FPS",
    "horror": "Horror",
    "healing": "Healing",
    "strategy": "Strategy",
    "coop": "Co-op",
    "openworld": "Open World",
    "survival": "Survival",
    "sports": "Sports"
}

# 장르별 1000개 이상 데이터 생성
game_db = {}

for genre, label in genres.items():
    game_db[genre] = [
        f"{label} Game {i}" for i in range(1, 1001)
    ]

# 실제 유명 게임 몇 개 추가
game_db["rpg"] += [
    "The Witcher 3",
    "Elden Ring",
    "Skyrim",
    "Persona 5"
]

game_db["fps"] += [
    "Valorant",
    "Call of Duty",
    "Battlefield 2042"
]

game_db["coop"] += [
    "It Takes Two",
    "Lethal Company",
    "Overcooked 2"
]

game_db["openworld"] += [
    "GTA V",
    "Red Dead Redemption 2",
    "Cyberpunk 2077"
]

# -----------------------------
# 키워드 분석
# -----------------------------

keyword_map = {
    "rpg": ["rpg", "스토리", "판타지", "모험"],
    "fps": ["fps", "총", "슈팅", "전쟁"],
    "horror": ["공포", "무서운", "호러"],
    "healing": ["힐링", "편한", "잔잔한"],
    "strategy": ["전략", "시뮬", "두뇌"],
    "coop": ["협동", "친구", "멀티"],
    "openworld": ["오픈월드", "자유도"],
    "survival": ["생존", "크래프팅"],
    "sports": ["축구", "농구", "스포츠"]
}

# -----------------------------
# 추천 함수
# -----------------------------

def analyze_genres(text):
    text = text.lower()
    matched_genres = []

    for genre, keywords in keyword_map.items():
        if any(keyword in text for keyword in keywords):
            matched_genres.append(genre)

    return matched_genres


def recommend_games(genres_found):
    recommendations = []

    # 장르별 추천
    for genre in genres_found:
        recommendations.extend(
            random.sample(game_db[genre], 3)
        )

    # -----------------------------
    # 융합 장르 추천
    # 예: RPG + 오픈월드
    # -----------------------------

    fusion_games = []

    if "rpg" in genres_found and "openworld" in genres_found:
        fusion_games += [
            "The Witcher 3",
            "Skyrim",
            "Elden Ring"
        ]

    if "coop" in genres_found and "horror" in genres_found:
        fusion_games += [
            "Phasmophobia",
            "Lethal Company"
        ]

    if "survival" in genres_found and "openworld" in genres_found:
        fusion_games += [
            "Minecraft",
            "Valheim",
            "Rust"
        ]

    recommendations.extend(fusion_games)

    # 중복 제거
    recommendations = list(set(recommendations))

    # 최대 12개 출력
    return random.sample(
        recommendations,
        min(12, len(recommendations))
    )


# -----------------------------
# UI
# -----------------------------

user_input = st.text_area(
    "예시: 자유도 높은 오픈월드 RPG 추천해줘",
    height=120
)

if st.button("추천 받기"):

    if user_input.strip():

        genres_found = analyze_genres(user_input)

        if genres_found:

            st.subheader("🔍 분석된 장르")

            for g in genres_found:
                st.write(f"- {genres[g]}")

            recommendations = recommend_games(genres_found)

            st.subheader("🎯 추천 게임")

            for game in recommendations:
                st.write(f"- {game}")

        else:
            st.warning("장르를 찾지 못했습니다.")
            st.write("예: RPG, 공포, 협동, 오픈월드 등")

    else:
        st.warning("문장을 입력해주세요.")
