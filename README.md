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

Create a `.env` file:
```bash
touch .env
```

Add the Hugging Face API key:

```plaintext
HF_API_KEY=your_huggingface_api_key
```
