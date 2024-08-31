import streamlit as st

# 퀴즈 데이터
quiz_data = [
    {
        "question": "다음 중 비타민 C가 풍부한 음식은 무엇인가요?",
        "options": ["사과", "오렌지", "밥", "치즈"],
        "answer": "오렌지"
    },
    {
        "question": "항생제는 주로 무엇을 치료하는 데 사용되나요?",
        "options": ["바이러스 감염", "세균 감염", "신경 장애", "알레르기"],
        "answer": "세균 감염"
    },
    {
        "question": "인체에서 가장 큰 장기는 무엇인가요?",
        "options": ["심장", "간", "폐", "위"],
        "answer": "간"
    }
]

# 앱 제목
st.title("HealthQuest: 의약학 퀴즈")

# 퀴즈 함수
def run_quiz():
    score = 0
    for i, q in enumerate(quiz_data):
        st.subheader(f"문제 {i + 1}: {q['question']}")
        answer = st.radio(
            "답을 선택하세요:",
            q['options'],
            key=f"question_{i}"
        )
        if answer == q['answer']:
            st.write("정답입니다!")
            score += 1
        else:
            st.write(f"틀렸습니다. 상심하지 말고 다시 한 번 도전해 보세요!")
        st.write("---")

    st.write(f"퀴즈 종료! 플레이해주셔서 감사합니다! 총 점수: {score}/{len(quiz_data)}")

# 앱 실행
if __name__ == "__main__":
    run_quiz()
