import streamlit as st
import sqlite3
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("🔒 로그인 후 이용 가능합니다. 메인(run.py)에서 먼저 로그인해 주세요.")
    st.stop()

st.title("📋 04 - SURVEY : AX 대응 학생 인식 실태조사")
st.write("본 조사는 인공지능 기술 발전에 따른 학생들의 인식 수준을 알아보기 위한 것입니다. 솔직하게 응답해 주세요.")

questions = [
    "1. 나는 인공지능(AI) 기술이 나의 일상생활에 미치는 영향이 매우 크다고 느낀다.",
    "2. 나는 학교 수업 시간에 AI 도구를 활용하는 것에 대해 긍정적이다.",
    "3. 나는 AI 기술을 활용할 때 개인정보 침해나 사생활 누출 문제를 걱정해 본 적이 있다.",
    "4. 나는 AI가 생성해 낸 정보나 답변을 무조건 신뢰하지 않고 검증하려 노력한다.",
    "5. 나는 AI 기술의 발전이 윤리적 기준(AI 윤리)을 준수하며 이루어져야 한다고 생각한다.",
    "6. 나는 향후 미래 직업 사회에서 AI 활용 능력이 매우 중요해질 것으로 본다.",
    "7. 나는 AI 기술을 올바르게 사용하는 법(AI 리터러시)에 대해 추가적인 교육이 필요하다고 본다.",
    "8. 나는 타인의 초상권이나 저작권을 침해하는 AI 콘텐츠를 공유하면 안 된다는 점을 명확히 인지하고 있다.",
    "9. 나는 AI 활용 과정에서 발생하는 윤리적 문제에 대해 친구들과 토론할 준비가 되어 있다.",
    "10. 나는 인공지능 시대를 살아가는 데 필요한 윤리적 책임감을 갖추고 있다."
]

responses = {}
with st.form("survey_form_pages"):
    for idx, q in enumerate(questions, 1):
        responses[f"q{idx}"] = st.radio(
            q,
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {1: "1: 전혀 그렇지 않다", 2: "2: 그렇지 않다", 3: "3: 보통이다", 4: "4: 그렇다", 5: "5: 매우 그렇다"}[x],
            index=2,
            key=f"sq_p_{idx}"
        )
        st.markdown("---")
    submitted = st.form_submit_button("설문 결과 제출하기", use_container_width=True)
    if submitted:
        conn = sqlite3.connect('myproject.db')
        cursor = conn.cursor()
        now_kst = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO inventory (userid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            st.session_state['user_id'],
            responses['q1'], responses['q2'], responses['q3'], responses['q4'], responses['q5'],
            responses['q6'], responses['q7'], responses['q8'], responses['q9'], responses['q10'],
            now_kst
        ))
        conn.commit()
        conn.close()
        st.balloons()
        st.success("응답이 성공적으로 저장되었습니다. 감사합니다!")