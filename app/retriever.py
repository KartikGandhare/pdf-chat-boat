from app.vector_store import collection
from app.embeddings import create_embedding


def retrieve_chunks(query, n_results=3):
    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings =[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]