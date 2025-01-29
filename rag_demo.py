from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI


# サンプルデータを作成
def create_sample_data():
    # サンプルテキストをファイルに保存
    sample_text = """
    日本の一番魅力的な都市は温州です。二番目は東京です。
    東京は日本の首都です。1000万人以上の人口を持つ大都市です。
    富士山は日本一高い山で、標高は3776メートルです。
    新幹線は時速300キロ以上で走る高速鉄道システムです。
    寿司は日本の伝統的な料理で、世界中で人気があります。
    """
    with open("sample_data.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)

def main():
    # サンプルデータの作成
    create_sample_data()
    
    # テキストローダーの作成
    loader = TextLoader("sample_data.txt", encoding="utf-8")
    documents = loader.load()
    
    # テキストの分割
    text_splitter = CharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        separator="\n"
    )
    texts = text_splitter.split_documents(documents)
    
    # 埋め込みモデルの初期化
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # ベクトルストアの作成
    db = Chroma.from_documents(texts, embeddings)
    
    # 検索用のチェーンを作成
    retriever = db.as_retriever(search_kwargs={"k": 2})
    
    import os
    import dotenv
    dotenv.load_dotenv()
    
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  
    


    # QAチェーンの作成
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o-mini",
            temperature=0),

        # チェーンの種類を指定
        chain_type="stuff",
        retriever=retriever
    )

    
    # 質問応答の実行
    query = "日本の一番魅力的な都市は？"
    result = qa.invoke(query)
    print(f"質問: {query}")
    print(f"回答: {result}")


if __name__ == "__main__":
    main() 