from openai import OpenAI

class EmbeddingGenerator:
    def __init__(self, model, api_key):
        self.model = model
        self.client = OpenAI(api_key = api_key)

    def create_embeddings(self, text): 
        response = self.client.embeddings.create(
            model=self.model, 
            input=text
        )
        embedding_vector = response.data[0].embedding
        return embedding_vector
