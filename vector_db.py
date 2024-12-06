'''
storing the genreated embeddings in vector database
for efficient similarity searches and quick lookups 
using faiss vector database
'''
import pickle
import faiss 
import numpy as np


def store_in_faiss(embeddings):
    dimension = len(next(iter(embeddings.values())))
    index = faiss.IndexFlatL2(dimension)
    ids = list(embeddings.keys())
    vectors = list(embeddings.values())

    # converting to numpy array and adding to datdabase index
    vectors = np.array(vectors).astype('float32')
    index.add(vectors)

    return ids, index


with open('processed/embeddings.pkl','rb') as f:
    embeddings = pickle.load(f)

ids, index = store_in_faiss(embeddings)

faiss.write_index(index,'processed/faiss_index.bin')        # save the index faiss locally
