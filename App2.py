# filename: openai_meme_explainer.py

import streamlit as st
import openai

# OpenAI 클라이언트 생성
client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

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
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 친근한 밈 설명가야."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except openai.APIError as e:
        return f"[에러] GPT API 오류: {e}"
    except Exception as e:
        return f"[에러] 알 수 없는 오류: {e}"
