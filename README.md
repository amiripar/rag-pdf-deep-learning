# RAG PDF Deep Learning

A simple Retrieval-Augmented Generation (RAG) project using LangChain, FAISS, and OpenAI GPT on a custom PDF.

## Features
- Extracts text from PDF
- Chunks and indexes text with FAISS
- Retrieves relevant context and answers questions using GPT

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Place your PDF (e.g., `deep learning.pdf`) in the project folder.

## Usage

1. Extract text from PDF:
   ```
   python extract_pdf.py
   ```

2. Chunk the text:
   ```
   python chunk_text.py
   ```

3. Build the FAISS index:
   ```
   python build_faiss_index.py
   ```

4. Ask questions using GPT:
   ```
   python rag_with_gpt.py
   ```

## Notes
- Do **not** commit your `.env` file or API keys.
- The `faiss_index/` folder is ignored for security and size reasons.

## License
MIT