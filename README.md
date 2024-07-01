PDF Document Processor and Vector Store Creation

Overview
This project provides a comprehensive solution for processing PDF documents, extracting text, generating embeddings, and storing the data in a vector store for efficient querying. Additionally, the project leverages a Large Language Model (LLM) to generate quiz questions from the processed text, making it an excellent tool for educational purposes.

Features
PDF Processing: Upload and process multiple PDF documents.

Text Splitting: Split documents into smaller text chunks for efficient embedding.

Embedding Generation: Generate embeddings for text chunks using a pre-configured embedding model.

Vector Store Creation: Store text chunks and their embeddings in a Chroma in-memory vector store.

Querying: Query the vector store to retrieve documents similar to a given query.

Quiz Question Generation: Automatically generate quiz questions from the processed text using an LLM.

Requirements
Python 3.8 or higher

Required Python libraries:
streamlit
langchain
langchain_community
chromadb
re
