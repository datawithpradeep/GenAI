from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

emedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
result=emedding.embed_query("explain the python")
print(str(result))