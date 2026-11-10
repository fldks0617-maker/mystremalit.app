import streamlit as st
import sqlite3
import hashlib
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

def get_db_connection():
    conn = sqlite3.connect('myproject.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT NOT NULL,
            userid TEXT UNIQUE NOT NULL,
            passwd TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            userid TEXT NOT NULL,
            q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
            q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

st.set_page_config(page_title="AI PRIVACY HUB", page_icon="🛡️", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None
if 'username' not in st.session_state:
    st.session_state['username'] = None

nav_col1, nav_col2 = st.columns([3, 1])
with nav_col1:
    st.markdown("### 🛡️ **AI PRIVACY HUB**")
with nav_col2:
    if st.session_state['logged_in']:
        st.write(f"👤 **{st.session_state['username']}** 학생 로그인 중")
        if st.button("로그아웃"):
            st.session_state['logged_in'] = False
            st.session_state['user_id'] = None
            st.session_state['username'] = None
            st.rerun()

st.markdown("---")

if not st.session_state['logged_in']:
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <h2>🔒 AI PRIVACY HUB 전자교과서</h2>
        <p style="color: #64748B;">수업 참여를 위해 먼저 로그인해 주세요.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        tab_login, tab_register = st.tabs(["🔑 로그인", "📝 신규 회원가입"])
        
        with tab_login:
            login_id = st.text_input("아이디", key="l_id")
            login_pw = st.text_input("비밀번호", type="password", key="l_pw")
            
            if st.button("교과서 입장하기 →", key="btn_login", use_container_width=True):
                if login_id and login_pw:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM users WHERE userid = ? AND passwd = ?", (login_id, hash_password(login_pw)))
                    user = cursor.fetchone()
                    conn.close()
                    
                    if user:
                        st.session_state['logged_in'] = True
                        st.session_state['user_id'] = user['userid']
                        st.session_state['username'] = user['username']
                        st.success(f"반갑습니다, {user['username']}님!")
                        st.rerun()
                    else:
                        st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
                else:
                    st.warning("아이디와 비밀번호를 모두 입력해 주세요.")
                    
        with tab_register:
            reg_name = st.text_input("성명", key="r_name")
            reg_id = st.text_input("사용할 아이디", key="r_id")
            reg_pw = st.text_input("비밀번호", type="password", key="r_pw")
            reg_pw_confirm = st.text_input("비밀번호 확인", type="password", key="r_pw_confirm")
            
            if st.button("가입 신청", key="btn_reg", use_container_width=True):
                if reg_name and reg_id and reg_pw and reg_pw_confirm:
                    if reg_pw != reg_pw_confirm:
                        st.error("비밀번호가 일치하지 않습니다.")
                    else:
                        conn = get_db_connection()
                        cursor = conn.cursor()
                        try:
                            now_kst = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')
                            cursor.execute(
                                "INSERT INTO users (username, userid, passwd, created_at) VALUES (?, ?, ?, ?)",
                                (reg_name, reg_id, hash_password(reg_pw), now_kst)
                            )
                            conn.commit()
                            st.success("🎉 회원가입이 완료되었습니다! 로그인 탭에서 로그인해 주세요.")
                        except sqlite3.IntegrityError:
                            st.error("이미 존재하는 아이디입니다.")
                        finally:
                            conn.close()
                else:
                    st.warning("모든 항목을 입력해 주세요.")

else:
    st.markdown(f"""
    <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #E2E8F0; margin-bottom: 25px;">
        <span style="color: #3B82F6; font-weight: 600; font-size: 13px;">● AI & DIGITAL CITIZENSHIP</span>
        <h1 style="font-size: 38px; font-weight: 800; color: #0F172A; margin: 10px 0;">AI를 이해하고, <span style="color:#2563EB;">개인정보를 지키다.</span></h1>
        <p style="color:#64748B;">환영합니다, <strong>{st.session_state['username']}</strong> 학생! 학습할 단계를 선택하면 왼쪽 메뉴와 함께 이동합니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📖 학습 메뉴 선택")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 01 LEARN")
        st.caption("AI 윤리 개념 및 추천 영상 시청")
        if st.button("01 LEARN 이동 ➔", key="btn_nav_1", use_container_width=True):
            st.switch_page("pages/1_LEARN.py")
            
    with col2:
        st.markdown("### 02 PRACTICE")
        st.caption("사생활 보호 실습 서버")
        if st.button("02 PRACTICE 이동 ➔", key="btn_nav_2", use_container_width=True):
            st.switch_page("pages/2_PRACTICE.py")
            
    with col3:
        st.markdown("### 03 REVIEW")
        st.caption("Kahoot, Padlet 등 복습 도구")
        if st.button("03 REVIEW 이동 ➔", key="btn_nav_3", use_container_width=True):
            st.switch_page("pages/3_REVIEW.py")
            
    with col4:
        st.markdown("### 04 SURVEY")
        st.caption("AX 대응 학생 인식 실태조사")
        if st.button("04 SURVEY 이동 ➔", key="btn_nav_4", use_container_width=True):
            st.switch_page("pages/4_SURVEY.py")