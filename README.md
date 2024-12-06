# CosmosGen :  Knowledge-Infused QA System
## Overview
CosmosGen is a powerful Retrieval-Augmented Generation (RAG) system designed to answer questions about the universe, drawing from Carl Sagan's Cosmos as the primary knowledge base. Using cutting-edge machine learning models like GPT-Neo for generative responses and FAISS for efficient vector search, CosmosGen can provide insightful, contextually accurate answers to various questions about space, science, and philosophy.

## Features
- RAG Architecture: Combines retrieval-based search with generative models for comprehensive responses.
- Cosmos Knowledge Base: Uses text from Carl Sagan’s Cosmos as the foundation for answering questions.
- Generative AI: Leverages the GPT-Neo model for generating elaborative answers.
Vector Database: Stores and searches knowledge using FAISS, ensuring fast retrieval of relevant information.
- API Integration: Built with FastAPI, providing a simple RESTful interface for interaction.
## Project Setup
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/CosmosGen.git
cd CosmosGen
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root directory to store sensitive information such as API keys.

1. Create a `.env` file:
```bash
touch .env
```

2. Open text editor to add the Hugging Face API key:

```bash
notepad .env
```
3. Save the API key with format `HF_API_KEY = {your_api_key}`.

### 4. Produce required files (chunked_text, embeddings, vector database):
```bash
python extract.py --input_file Carl Sagan - Cosmos \(1980\)_knowledge_base.pdf --output_file text_data.json\
python preprocess.py --input_file text.json --output_file chunked_text.json\
python embeddings.py --input_file chunked_text.json --output_file embeddings.pkl\
python vector_db.py --input_file embeddings.pkl --output_file faiss_index.bin
```

### 5. Run the API Server
```bash
uvicorn main:app --reload
```
The server will be accessible at http://127.0.0.1:8000. You can test the `/query` endpoint directly or through Swagger UI (available at http://127.0.0.1:8000/docs).

## API Usage
The `/query` endpoint accepts POST requests with a JSON payload containing a `question`. Here’s an example of how to query the system:
```bash
curl -X POST "http://127.0.0.1:8000/query"
-H "Content-Type: application/json"
-d '{"question": "What is the Cosmic Calendar?"}'
```

The response will contain an answer to the question based on the relevant chunks retrieved from the Cosmos text.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
