import utils
import embedding_generator
import faiss
import numpy as np
import json

class Ingester:
    def __init__(self, model, api_key):
        self.model = model
        self.api_key = api_key
    
    def ingest(self, text):
        chunks = utils.text_splitter_with_overlap(text)
        dict = {}
        for i,chunk in enumerate(chunks):
            dict[i] = chunk
        with open("../data/text_map.json",'w') as f:
            json.dump(dict,f)
        embed_obj = embedding_generator.EmbeddingGenerator(self.model, self.api_key)
        embedding_vectors = embed_obj.create_embeddings(chunks)
        dimension = len(embedding_vectors[0])
        np_embedding_vectors = np.array(embedding_vectors)
        index = faiss.IndexFlatL2(dimension)
        index.add(np_embedding_vectors)
        faiss.write_index(index, "../data/index.faiss")
