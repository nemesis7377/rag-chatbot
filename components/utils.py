def text_splitter_with_overlap(text, max_tokens=300, overlap_tokens=50):
    tokens = text.split()
    chunks = []
    start = 0
    while start <= len(tokens):
        end = start + max_tokens
        current_chunk = tokens[start:end]
        chunks.append(" ".join(current_chunk))
        start = end - overlap_tokens
    return chunks