import chromadb
from app.embeddings import create_embedding

client = chromadb.PersistentClient(path="./chroma_db")  

collection =client.get_or_create_collection(
     name="pdf_documents"
)

def add_chunks(chunks):
    embeddings=[create_embedding(chunk) for chunk in chunks]

    ids = [f"chunk_{i}" for i in range(len(chunks))]


    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )