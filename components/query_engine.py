from . import utils
from . import embedding_generator
import faiss
import numpy as np
import json

class QueryEngine:
    def __init__(self, model, api_key):
        self.model = model
        self.api_key = api_key
    
    def search(self, query):
        embed_obj = embedding_generator.EmbeddingGenerator(self.model, self.api_key)
        embedding_vectors = embed_obj.create_embeddings(query)
        np_embedding_vectors = np.array(embedding_vectors)
        index = faiss.read_index("data/index.faiss")
        distances, indices = index.search(np_embedding_vectors, k=10)
        dict = {}
        with open("data/text_map.json",'r') as f:
            dict = json.load(f)
        matching_chunks = []
        for i in (indices[0]):
            matching_chunks.append(dict[str(i)])
        return matching_chunks
