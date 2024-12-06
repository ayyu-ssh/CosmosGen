
import re
import nltk
from nltk.tokenize import sent_tokenize
import json

nltk.download('punkt_tab')

'''
Preprocessing
'''

def clean_text(text):

    text = re.sub(r'\s+',' ',text) #replace multiple space with single space
    text = re.sub(r'[^\w\s.,!?\,\"]','',text) #removing special charecters
    return text.strip()

'''
Chunking Text
'''

def chunk_text(text,max_words=150):
    sentences = sent_tokenize(text)
    chunks=[]
    current_chunk=[]
    current_word_count=0

    for sentence in sentences:
        word_count = len(sentence.split())
        if current_word_count + word_count <= max_words:
            current_chunk.append(sentence)
            current_word_count +=word_count
        else:
             chunks.append(' '.join(current_chunk))
             current_chunk = [sentence]
             current_word_count = word_count

    
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def preprocess_and_chunk(data, max_words=250):

    processed_data = {}
    chunk_with_ids = {}

    cleaned_text = clean_text(data)
    chunks = chunk_text(cleaned_text)

    chunk_ids = [f'chunk_{i}'for i in range (1,len(chunks)+1)]
    chunk_with_ids = dict(zip(chunk_ids,chunks))

    return chunk_with_ids


with open('processed/text.json','r') as f:
    data = json.load(f)

chunked_data = preprocess_and_chunk(data)

with open('processed/chunked_text.json','w') as f:
    json.dump(chunked_data,f,indent=4)

