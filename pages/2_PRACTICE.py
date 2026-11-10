import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("🔒 로그인 후 이용 가능합니다. 메인(run.py)에서 먼저 로그인해 주세요.")
    st.stop()

st.title("📷 02 - PRACTICE : 직접 실천하기.")

st.markdown("""
<div style="background-color: #0F172A; color: white; border-radius: 20px; padding: 35px;">
    <span style="color:#A7F3D0; font-size:13px; font-weight:bold;">PRACTICE MODE</span>
    <h2 style="font-size:28px; color:#60A5FA; margin:10px 0;">안전한 AI 사용을 직접 경험해 보세요.</h2>
    <p style="color:#94A3B8;">AI 개인정보보호 실습 서버에서 안전한 입력과 정보 보호 방법을 경험합니다. 실습 링크가 연결될 예정입니다.</p>
    <br>
    <div style="background:#1E293B; padding:15px; border-radius:10px; border:1px solid #334155; color:#E2E8F0;">
        ● PRIVACY CHECK READY: 실습 서버 연동 준비 완료
    </div>
</div>
""", unsafe_allow_html=True)