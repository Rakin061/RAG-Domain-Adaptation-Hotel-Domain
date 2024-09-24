def split_text_into_chunks(text):
    chunks = []
    words = text.split()
    current_chunk = []
    current_length = 0

    for word in words:
        if word.endswith(('.', '?', '!')):
            current_chunk.append(word)
            current_length += 1  # Add 1 for the space
            if current_length > 100:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = 0
        else:
            current_chunk.append(word)
            current_length += 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


