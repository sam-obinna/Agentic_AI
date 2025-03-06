import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")

vectorstore = PineconeVectorStore(
    embedding=embed_model,
    index_name=os.getenv("PINECONE_INDEX"),
    namespace="nav_indexed"
)
