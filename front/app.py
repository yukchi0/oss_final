import streamlit as st
import requests

st.set_page_config(page_title="게임 추천 시스템")

st.title("게임 추천 시스템")
st.markdown("장르, 플레이 시간, 플랫폼을 입력하면 조건에 맞는 게임을 추천합니다.")

st.divider()

genre = st.selectbox(
    "장르",
    ["액션", "RPG", "전략", "스포츠"]
)

play_time = st.selectbox(
    "하루 평균 플레이 시간",
    ["1시간 미만", "1~3시간", "3시간 이상"]
)

platform = st.selectbox(
    "플랫폼",
    ["PC", "콘솔"]
)

st.divider()

if st.button("추천 조회", use_container_width=True):
    with st.spinner("처리 중..."):
        try:
            response = requests.post(
                "http://backend:8000/recommend",
                json={
                    "genre": genre,
                    "play_time": play_time,
                    "platform": platform
                }
            )
            data = response.json()

            st.success("조회 완료")
            st.subheader("추천 게임 목록")

            for i, game in enumerate(data["recommendations"], 1):
                with st.container():
                    st.markdown(f"### {i}. {game['title']}")
                    st.markdown(f"{game['reason']}")
                    st.divider()

        except Exception as e:
            st.error(f"서버 연결 오류: {e}")
            st.info("FastAPI 백엔드 서버 실행 상태를 확인하세요.")