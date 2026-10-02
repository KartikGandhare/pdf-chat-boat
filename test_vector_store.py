from app.vector_store import add_chunks

chunks = [
    "The company generated revenue of 150 crore rupees.",
    "The company reported a net loss of 25 crore rupees."
]

add_chunks(chunks)

print("Chunks stored successfully!")