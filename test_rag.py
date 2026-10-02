from app.rag import answer_question

question = "What was the company's revenue?"

answer = answer_question(question)

print("Answer:")
print(answer)