from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

query = input("Enter your question: ")
results = faiss_index.similarity_search(query, k=3)

for i, doc in enumerate(results, 1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 40)