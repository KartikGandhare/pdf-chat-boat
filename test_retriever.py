from app.retriever import retrieve_chunks

query = "What was the company's revenue?"

results = retrieve_chunks(query)

print("Retrieved chunks:")

for chunk in results:
    print("--------------------")
    print(chunk)