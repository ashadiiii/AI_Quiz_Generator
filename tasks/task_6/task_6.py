import sys
import streamlit as st
sys.path.insert(0, '/Users/ashadi/Documents/mission-quizify/tasks')
from task_3.task_3 import DocumentProcessor
from task_4.task_4 import EmbeddingClient
from task_5.task_5 import ChromaCollectionCreator

if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "trans-array-427509-h2",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        st.header("Quizzify")
        processor = DocumentProcessor()
        processor.ingest_documents()
        embed_client = EmbeddingClient(**embed_config)
        faiss_creator = ChromaCollectionCreator(processor,embed_client)


        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
            topic_input = st.text_input("Topic for Generative Quiz")
            questions = st.slider("Number of questions")
            st.write('Number of questions:',questions)
            
            submitted = st.form_submit_button("Submit")
            
            document = None

            if submitted:
                faiss_creator.create_chroma_collection()
                document = faiss_creator.query_chroma_collection(topic_input) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)