from fastapi import FastAPI , UploadFile, File
from app.pdf_processor import extract_text
from app.chunker import chunk_text
from app.vector_store import add_chunks
from app.rag import answer_question
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_pdf(pdf_upload: UploadFile = File(...)):
    text = extract_text(pdf_upload.file)
    chunks = chunk_text(text)

    add_chunks(chunks)  

    return {
        "filename": pdf_upload.filename,
        "chunks": chunks
    }

    # function for Rag Connection
class QuestionRequest(BaseModel):

    question : str

@app.post("/ask")
def ask_question(request:QuestionRequest):
   answer = answer_question(request.question)
   
   return{
    "question": request.question,
     "answer": answer
   }