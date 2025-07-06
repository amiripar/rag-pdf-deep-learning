import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

load_dotenv()  # Load environment variables from .env

# No need to set os.environ["OPENAI_API_KEY"] manually

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

user_question = input("Enter your question: ")
retrieved_docs = faiss_index.similarity_search(user_question, k=3)
context = "\n".join([doc.page_content for doc in retrieved_docs])

prompt = f"""You are an expert assistant. Use the following context to answer the question.
Context:
{context}

Question: {user_question}
Answer:"""

llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke(prompt)
print("\n--- GPT Answer ---\n")
print(response.content)
