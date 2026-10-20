from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
docs=["delhi is the capital of india",
      "kolkata is the capital of west bengal",
      "paris is the capital of france"]
result=embedding.embed_documents(docs)
print(str(result))