from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


#モデルの初期化
llm = ChatOpenAI(model="gpt-4o-mini", 
                 temperature=0)

question  = "日本の一番魅力的な都市は,１つに絞って回答ください？"

#質問を送信して回答を取得
response = llm.invoke(question)

#回答を表示
print(response.content)


