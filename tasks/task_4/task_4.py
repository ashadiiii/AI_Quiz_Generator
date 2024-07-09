# embedding_client.py

from langchain_google_vertexai import VertexAIEmbeddings

class EmbeddingClient:
    """
    Task: Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.

    The EmbeddingClient class should be capable of initializing an embedding client with specific configurations
    for model name, project, and location. Your task is to implement the __init__ method based on the provided
    parameters. This setup will allow the class to utilize Google Cloud's VertexAIEmbeddings for processing text queries.
    """
    
    def __init__(self, model_name, project, location):
        # Initialize the VertexAIEmbeddings client with the given parameters
        :param query: The text query to embed.
        :return: The embeddings for the query or None if the operation fails.
        """
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.

        :param documents: A list of text documents to embed.
        :return: A list of embeddings for the given documents.
        """
        try:
            return self.client.embed_documents(documents,batch_size=0)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "trans-array-427509-h2"
    location = "us-central1"

    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        print(vectors)
        print("Successfully used the embedding client!")
