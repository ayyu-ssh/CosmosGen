from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import faiss
import json
from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')

app = FastAPI()


index = faiss.read_index('processed/faiss_index.bin')

with open('processed/chunked_text.json','r') as f:
    metadata = json.load(f)

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('HF_API_KEY')
headers = {'Authorization':f'Bearer {API_KEY}'}
API_URL = 'https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B'


if not API_KEY:
    raise ValueError("HF_API_KEY not found in environment variables.")


class QueryInput(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

def answer_query(query,model,index,metadata,k=3):


    query_encoded = model.encode(query).reshape(1,-1)

    distances, indices = index.search(query_encoded, k)

    results = []
    for idx in indices[0]:
        chunk_id = list(metadata.keys())[idx]  # Get chunk ID from index
        chunk_text = metadata[chunk_id]  # Retrieve text using the chunk ID
        results.append(chunk_text)
    
    return results

response = {}
def query_llm(prompt:str) -> str:
    response = requests.post(API_URL, headers=headers, json=prompt)
    return response

@app.post('/query',response_model=QueryResponse)
async def query_endpoint(input: QueryInput) -> QueryResponse:
    try:
        query = input.question
        
        relevant_chunks = answer_query(query,model,index,metadata,k=5)
   
        context = '\n\n'.join(relevant_chunks)
   
        #prompt = f'{context}\n\nQuestion:{query}\nAnswer:'
        prompt = {
            "inputs": f"Context: {context}\nQuestion: {query}\nAnswer:",
            "parameters": {
                #"max_new_tokens": 200,
                "temperature": 0.5,
                "top_p": 0.95,
                "repetition_penalty": 1.0}
                    }

        answer = query_llm(prompt)

        answer = answer.json()[0]['generated_text'].split('Answer:')[-1]

        return QueryResponse(answer=answer[:answer.rindex('.')+1])     # ensures deletion of incomplete sentences

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    
