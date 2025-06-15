import fitz
from components.ingester import Ingester
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model_embed = "text-embedding-3-large"

def extract_text_from_pdf():
    pdf_path = "/mnt/c/Users/Aarav Eeshan/Downloads/CoS 2024.pdf"
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

text = extract_text_from_pdf()
pdf_obj = Ingester(model_embed, api_key)
pdf_obj.ingest(text)



