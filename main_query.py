from components.query_engine import QueryEngine
from components.response_generator import ResponseGenerator

model_embed = "text-embedding-3-large"
model_chat = "gpt-4"

def main_query(query, api_key):
    chunks_obj = QueryEngine(model_embed, api_key)
    context_chunks = chunks_obj.search(query)
    response_obj = ResponseGenerator(model_chat, api_key)
    response = response_obj.generate_response(query, context_chunks)
    return response

