import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("🔒 로그인 후 이용 가능합니다. 메인(run.py)에서 먼저 로그인해 주세요.")
    st.stop()

st.title("🔗 03 - REVIEW : 함께 정리하고, 오래 기억하기.")
st.caption("수업의 마지막 단계에서 퀴즈와 협업 도구로 배운 내용을 확인합니다.")

r_col1, r_col2, r_col3, r_col4 = st.columns(4)

with r_col1:
    st.markdown("#### 🎯 Kahoot!")
    st.caption("게임형 퀴즈로 핵심 개념 확인")
    st.markdown("[도구 바로가기 ↗](https://kahoot.it)")

with r_col2:
    st.markdown("#### ❓ Quizizz")
    st.caption("개별 이해도 점검 및 문항 풀이")
    st.markdown("[도구 바로가기 ↗](https://quizizz.com)")

with r_col3:
    st.markdown("#### 🧠 Coggle")
    st.caption("AI 윤리 개념 시각적 구조화")
    st.markdown("[도구 바로가기 ↗](https://coggle.it)")

with r_col4:
    st.markdown("#### 📌 Padlet")
    st.caption("모둠별 의견 공유와 성찰")
    st.markdown("[도구 바로가기 ↗](https://padlet.com)")