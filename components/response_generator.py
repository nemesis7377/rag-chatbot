import openai

class ResponseGenerator:
    def __init__(self, model, api_key):
        self.model = model
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, query, context_chunks):
        context = "\n\n".join(context_chunks)
        prompt = f"You are a helpful assistant, designed to help IIT Delhi students with their questions about the content of the Courses Of Study document provided by the institute. Use the context below to answer the user's question in a clear, structured format. Context:{context}. Question:{query}"
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
        model = self.model
        response = openai.chat.completions.create(
            model = model,
            messages = messages
        )

        return response.choices[0].message.content