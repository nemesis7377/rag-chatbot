from openai import OpenAI

class EmbeddingGenerator:
    def __init__(self, model, api_key):
        self.model = model
        self.client = OpenAI(api_key = api_key)

    def create_embeddings(self, text): 
        embedding_vector = []
        for i in range(0,len(text),50):
            current_text = text[i:i+50]
            response = self.client.embeddings.create(
                model=self.model, 
                input=current_text
            )
            for r in response.data:
                embedding_vector.append(r.embedding)
        return embedding_vector
