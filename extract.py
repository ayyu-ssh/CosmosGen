from PyPDF2 import PdfReader
import json


def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text


def save_to_json(data, output_file):
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)


text = extract_text_from_pdf('Carl Sagan - Cosmos (1980)_knowledge_base.pdf')

save_to_json(text, 'processed/text.json')