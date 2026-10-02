from app.embeddings import create_embedding

text = "The company generated revenue of 150 crore rupees."

vector = create_embedding(text)

print("Vector length:", len(vector))
print("First 5 values:", vector[:5])