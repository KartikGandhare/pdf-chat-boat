import streamlit as st
import requests

st.title("Pdf Chat Boat")
st.write("Ask Question About your uploaded Pdf")

uploaded_file = st.file_uploader(
    "chose a pdf file",
     type=["pdf"]
)

if uploaded_file is not None:
    if st.button("upload pdf"):
        response = requests.post(
            "http://backend:8000/upload",
            files = {
                "pdf_upload": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }
        )

        if response.status_code == 200:
            result = response.json()
            st.success("pdf uploaded successfully")
            st.write("Filename:", result["filename"])
            st.write("Number of chunk:", len(result["chunks"]))
        else:
            st.error("faild to uploaded pdf")

# user aske Question
st.divider()
st.subheader("Ask the Question")
question = st.text_input("please enter your question")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://backend:8000/ask",
             json={
                "question": question
             }
        )
        if response.status_code == 200:
            result = response.json()
            st.write("### Answer")
            st.write(result["answer"])

        else:
            st.error("Failed to get answer")
    else:
        st.warning("Please Enter the question")


    

