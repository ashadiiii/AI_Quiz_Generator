## pdf_processing.py

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid
import concurrent.futures

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted.
    """
    def __init__(self):
        self.pages = []  # List to keep track of pages from all documents
    
    def process_pdf(self, uploaded_file):
        """
        Process a single PDF file, extract its pages, and return them.
        """
        # Generate a unique identifier to append to the file's original name
        unique_id = uuid.uuid4().hex
        original_name, file_extension = os.path.splitext(uploaded_file.name)
        temp_file_name = f"{original_name}_{unique_id}{file_extension}"
        temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

        # Write the uploaded PDF to a temporary file
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())

        # Step 2: Process the temporary file
        pdf_pages = []
        try:
            pdf_loader = PyPDFLoader(temp_file_path)
            pdf_pages = pdf_loader.load_and_split()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # Clean up by deleting the temporary file.
        os.unlink(temp_file_path)

        return pdf_pages

    def ingest_documents(self):
        """
        Renders a file uploader in a Streamlit app, processes uploaded PDF files,
        extracts their pages, and updates the self.pages list with the total number of pages.
        """
        # Step 1: Render a file uploader widget
        uploaded_files = st.file_uploader('Upload your files.', type=['pdf'], accept_multiple_files=True)
        
        if uploaded_files:
            # Use ThreadPoolExecutor for parallel processing of documents
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.process_pdf, uploaded_file) for uploaded_file in uploaded_files]
                for future in concurrent.futures.as_completed(futures):
                    self.pages.extend(future.result())

            # Display the total number of pages processed.
            st.write(f"Total pages processed: {len(self.pages)}")
        
if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()
