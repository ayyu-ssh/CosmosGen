import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('processed/chunked_text.json','r') as f:
    data = json.load(f)

def generate_embeddings(data,model,batch_size=32):

    model_embeddings = {}
    chunk_embeddings=[]
    ids = list(data.keys())
    chunks = list(data.values())

    for i in range (0,len(chunks),batch_size):

        embeddings = model.encode(chunks[i:i+batch_size])
        chunk_embeddings.extend(embeddings)
    
    model_embeddings = dict(zip(ids,chunk_embeddings))
    return model_embeddings
    

embeddings = generate_embeddings(data,model)

#print (type(embeddings), len(embeddings),len(ids))

import pickle

with open('processed/embeddings.pkl','wb') as f:
    pickle.dump(embeddings,f)



