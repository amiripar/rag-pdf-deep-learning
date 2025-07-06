import json
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.docstore.document import Document

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.document import Document

documents = []
with open("chunks.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        documents.append(Document(page_content=data["text"]))

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

faiss_index = FAISS.from_documents(documents, embedding_model)

faiss_index.save_local("faiss_index")