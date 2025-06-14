from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def text_splitter(text, max_tokens=300):
    words = text.split()
    chunks = []
    current_chunk = []

    token_count = 0
    for word in words:
        token_count += len(tokenizer.encode(word, add_special_tokens=False))
        current_chunk.append(word)

        if token_count >= max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            token_count = 0

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
