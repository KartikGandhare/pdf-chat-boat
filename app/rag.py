from app.llm import generate_answer
from app.retriever import retrieve_chunks

def answer_question(question):

   chunks =retrieve_chunks(question)

   context = "\n\n".join(chunks)

   answer = generate_answer(
    question,
    context
   )

   return answer
