import streamlit as st
st.title('나의 첫 웻앱!')
st.write('이걸 내가 만들었다고 꺄르륵히히?!')
import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="MBTI 공부법 추천기 🎓✨", page_icon="📚", layout="centered")

# 헤더
st.title("📖 MBTI 공부법 추천기 🔮")
st.markdown("당신의 **MBTI 유형**을 선택하면, 딱 맞는 공부 꿀팁을 알려드려요! 🚀💡")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 공부법 딕셔너리
study_tips = {
    "INTJ": "📑 계획적으로 정리된 노트 & 자기주도 학습 📅\n👉 큰 목표를 세우고 작은 단위로 쪼개서 달성!",
    "INTP": "🧪 호기심 기반 탐구 학습 🔍\n👉 깊이 파고들며 원리를 이해하는 방식이 효과적!",
    "ENTJ": "📊 전략적 목표 설정 + 경쟁적인 환경 🏆\n👉 마감과 도전 과제가 있을 때 집중력이 폭발!",
    "ENTP": "💡 토론 & 브레인스토밍 중심 🤹‍♂️\n👉 자유롭게 아이디어를 연결하면서 공부하면 효율 ↑",
    "INFJ": "🕯️ 조용한 공간 + 깊은 몰입 🌌\n👉 감정을 글로 정리하면서 배운 내용을 내면화!",
    "INFP": "🎨 감성적 연결 학습 🎶\n👉 좋아하는 이야기나 가치와 연결하면 기억에 오래 남음!",
    "ENFJ": "🤝 협력 & 스터디 그룹 📚\n👉 친구 가르쳐주면서 같이 배우면 더 효과적!",
    "ENFP": "🌈 창의적 프로젝트 학습 🎭\n👉 즐겁고 재미있게 연결할수록 집중력이 올라감!",
    "ISTJ": "📘 체계적 요약 정리 + 반복 암기 🔁\n👉 규칙적인 루틴과 체크리스트가 큰 힘이 돼요!",
    "ISFJ": "🧸 꼼꼼한 필기 + 안정적인 환경 🛋️\n👉 친근한 자료와 따뜻한 분위기에서 잘 배움!",
    "ESTJ": "📅 철저한 계획표 + 결과 중심 학습 🥇\n👉 관리할 수 있는 구조 속에서 성과를 내는 스타일!",
    "ESFJ": "👥 그룹 학습 + 상호 피드백 💬\n👉 친구들과 교류하며 배울 때 에너지가 올라감!",
    "ISTP": "🔧 실습 중심 체험 학습 ⚙️\n👉 직접 만지고 실험할 때 가장 잘 흡수!",
    "ISFP": "🎶 감각적·시각적 학습 🌺\n👉 그림, 음악, 색감과 연결된 공부가 효과적!",
    "ESTP": "🔥 액션 기반 빠른 적용 🏃‍♂️\n👉 배운 것을 즉시 써먹을 때 집중도 상승!",
    "ESFP": "🎉 놀이형 학습 & 활동적 환경 🎶\n👉 게임처럼 즐길 때 기억이 오래 감!"
}

# MBTI 선택
selected = st.selectbox("👉 나의 MBTI 선택하기:", mbti_types)

if selected:
    st.subheader(f"✨ {selected} 유형에게 딱 맞는 공부법 ✨")
    st.success(study_tips[selected])

    # 랜덤 재미 효과
    effects = [st.balloons, st.snow]
    random.choice(effects)()

    st.markdown("💡 **오늘부터 바로 실천해보자구요!** 🚀🔥")
