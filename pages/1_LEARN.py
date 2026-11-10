import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("🔒 로그인 후 이용 가능합니다. 메인(run.py)에서 먼저 로그인해 주세요.")
    st.stop()

st.title("🔍 01 - LEARN : 먼저, 제대로 이해하기.")
st.caption("AI 윤리와 개인정보보호의 핵심 개념을 다양한 자료로 학습합니다.")

st.markdown("---")
st.subheader("🎥 주요 추천 영상 학습 (4선)")

v_col1, v_col2 = st.columns(2)

with v_col1:
    st.markdown("#### 🎬 [AI 윤리 이슈 1] 사생활 보호 & 윤리적 문제")
    st.video("https://youtu.be/RgQWU2PNRXk")
    st.markdown("---")
    st.markdown("#### 🎬 [AI 윤리 이슈 3] 인공지능 편향성과 저작권 갈등")
    st.video("https://youtu.be/XyEOEBsa8I4")
    
with v_col2:
    st.markdown("#### 🎬 [AI 윤리 이슈 2] 딥페이크와 개인정보 침해 사례")
    st.video("https://youtu.be/MhI2dPrHF3s")
    st.markdown("---")
    st.markdown("#### 🎬 [AI 윤리 이슈 4] AI 시대의 책임감과 윤리 가이드")
    st.video("https://youtu.be/67KgzGcX4Gc")

st.markdown("---")
st.subheader("🔎 관심 키워드 추가 검색")
forbidden_keywords = ["게임", "놀이", "영화", "아이돌", "먹방", "웹툰"]
search_query = st.text_input("탐색하고 싶은 AI 윤리 키워드를 입력하세요 (예: 딥페이크, 저작권, 초상권):")
if search_query:
    if any(bad_word in search_query for bad_word in forbidden_keywords):
        st.error("⚠️ 경고: 수업 및 AI 윤리와 관련 없는 검색어입니다.")
    else:
        st.success(f"'{search_query}' 관련 학습 자료 탐색 결과:")
        st.markdown(f"- 🎬 [유튜브에서 '{search_query} AI 윤리' 교육영상 검색하기](https://www.youtube.com/results?search_query={search_query}+AI+윤리)")