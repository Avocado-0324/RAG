# LangChain RAG デモ

LangChainを使用した簡単なRAG（検索拡張生成）システムの実装です。

## 必要環境

- Python 3.8+
- OpenAI APIキー

## セットアップ手順

1. 仮想環境の作成と有効化:
```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

2. 必要なパッケージのインストール:
```bash
pip install langchain langchain-community langchain-openai openai chromadb python-dotenv
```

3. 環境変数の設定:
- `.env`ファイルを作成し、OpenAI APIキーを追加:
```
OPENAI_API_KEY=あなたのOpenAI-APIキー
```

## 使用方法

1. 仮想環境が有効化されていることを確認
2. デモプログラムの実行:
```bash
python rag_demo.py
```

## 機能説明

- OpenAIのembeddingモデルによるテキストのベクトル化
- Chromaをベクトルデータベースとして使用
- 日本語テキストの処理と検索に対応
- GPT-4による質問応答の生成

## 注意事項

- `.env`ファイルにAPIキーが正しく設定されていることを確認してください