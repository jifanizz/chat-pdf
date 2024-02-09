import streamlit as st
from dotenv import load_dotenv



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":books:", layout="centered")
    st.header("Chat with Multiple PDFs :books:")
    st.text("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Upload Documents here:")
        st.file_uploader("Upload PDFs here:", type="pdf", accept_multiple_files=True)
        st.button("Process")





if __name__ == "__main__":
    main() 