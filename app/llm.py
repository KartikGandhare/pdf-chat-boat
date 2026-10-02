import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(question, context):
    prompt = f"""    
      You are a helpful assistant answering questions from a PDF document.

      Use ONLY the information provided in the context below.

      If the answer is not available in the context, say:
      "I could not find this information in the uploaded PDF."
      
      Context:
      {context}

      Question:
      {question}

      Answer:
     """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

    
