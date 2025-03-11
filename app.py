# 画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果を画面上に表示。
# ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変える。
# 「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し利用。
# Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示。
# Streamlit Community Cloudにデプロイする際Pythonのバージョンは「3.11」。

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

st.title("質問回答Webアプリ")
st.write("##### 「スキルアップ」「趣味」「老後の生活」から一つ選び、質問を入力して「実行」ボタンを押すことで質問に回答します。")

st.divider()

selected_item = st.radio(
    "質問の種類を選択してください。",
    ["スキルアップ", "趣味", "老後の生活"]
)
input_message = st.text_input(label="質問を入力してください。入力後にreturnキーを押すと実行ボタンが現れます。")

st.divider()

if not input_message:
    st.error("質問を入力してから「実行」ボタンを押してください。")
else:
    if st.button("実行"):
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content=f"あなたは、{selected_item}に詳しいAIです。ユーザーからの質問に回答してください。"),
            HumanMessage(content= input_message),
        ]
        result = llm(messages)
        st.write(result.content)