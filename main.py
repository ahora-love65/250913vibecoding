import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("🌍 MBTI 유형별 국가 Top10 시각화")
st.markdown("CSV 데이터를 불러와서 각 MBTI 유형에서 비율이 가장 높은 국가 10곳을 보여줍니다.")

# 데이터 불러오기
file_path = "countriesMBTI_16types.csv"

if os.path.exists(file_path):
    # 같은 폴더에 파일이 있을 경우
    df = pd.read_csv(file_path)
    st.success(f"✅ '{file_path}' 파일을 불러왔습니다.")
else:
    # 파일이 없을 경우 업로드 기능 사용
    uploaded_file = st.file_uploader("📂 CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ 업로드된 파일을 불러왔습니다.")
    else:
        st.warning("⚠️ CSV 파일이 필요합니다.")
        st.stop()

# MBTI 유형 목록
mbti_types = df.columns[1:]  # 첫 번째 컬럼은 Country, 나머지는 MBTI 유형
selected_type = st.selectbox("🔎 MBTI 유형을 선택하세요:", mbti_types)

# 선택된 유형 기준으로 Top10 추출
top10 = df.nlargest(10, selected_type)[["Country", selected_type]]

# Altair 그래프
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title="비율"),
        y=alt.Y("Country", sort="-x", title="국가"),
        tooltip=["Country", selected_type]
    )
    .properties(
        width=600,
        height=400,
        title=f"{selected_type} 유형 비율 Top10 국가"
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
