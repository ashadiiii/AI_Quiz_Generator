# embedding_client.py

from langchain_google_vertexai import VertexAIEmbeddings

class EmbeddingClient:
    
    def __init__(self, model_name, project, location):
        # Initialize the VertexAIEmbeddings client with the given parameters
        # Read about the VertexAIEmbeddings wrapper from Langchain here
        # https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai
        self.model = model_name
        self.project = project
        self.location = location
        self.client = VertexAIEmbeddings(model_name= self.model,project=self.project, location= self.location)
        
    def embed_query(self, query):
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):

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
