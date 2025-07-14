# filename: openai_meme_explainer.py

import streamlit as st
import openai

# OpenAI API 키 등록 (secrets.toml에 넣어야 안전)
openai.api_key = st.secrets["openai_api_key"]

# 프롬프트 구성 함수
def build_prompt(meme_name):
    return f"""
너는 인터넷 밈 전문가야. '{meme_name}'이라는 밈을 아래 세 가지 항목으로 한국어로 간단히 설명해줘:

1. 뜻
2. 유래
3. 사용 예시

친근하고 이해하기 쉽게 설명해줘.
"""

# GPT API 호출 함수
def query_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 gpt-4 (유료 계정만)
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[에러] GPT 호출 실패: {e}"

# Streamlit 앱 구성
st.set_page_config(page_title="GPT 밈 설명기", page_icon="🧠")
st.title("🧠 OpenAI 기반 AI 밈 설명기")
st.write("GPT-3.5가 밈의 뜻과 유래를 친절하게 설명해드려요!")

meme_input = st.text_input("밈 이름을 입력하세요 (예: 킹받네, 손절각, 갓생)").strip()

if st.button("설명 보기") and meme_input:
    with st.spinner("GPT가 밈을 분석 중입니다..."):
        prompt = build_prompt(meme_input)
        explanation = query_gpt(prompt)
        st.text_area("💬 밈 설명", explanation, height=300)

st.markdown("---")
st.caption("Made with ❤️ OpenAI + Streamlit")
