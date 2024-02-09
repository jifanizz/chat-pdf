import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import faiss


 

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )

def VectorStore(text_chunks):

    
    chunks = text_splitter.split_text(text)
    return chunks
    



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":books:", layout="centered")
    st.header("Chat with Multiple PDFs :books:")
    st.text("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Upload Documents here:")
        pdf_docs = st.file_uploader("Upload PDFs here:", type="pdf", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
               
                # get pdf
                raw_text = get_pdf_text(pdf_docs)
                #st.write(raw_text)

                # get text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)

                # create vector store
                vectorstore = VectorStore(text_chunks)





if __name__ == "__main__":
    main() 