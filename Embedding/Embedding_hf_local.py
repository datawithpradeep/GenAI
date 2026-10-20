from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
docs=["delhi is the capital of india",
      "kolkata is the capital of west bengal",
      "paris is the capital of france"]

vector=embedding.embed_documents(docs)
print(str(vector))
print("sucess")