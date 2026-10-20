from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
docs=["virat kohli is an indian cricketer know for his aggressive batting and leadership",
      "ms dhoni is a former indian captain famous fro his calm demeanor and finishing skill",
      "sachin tendular also knows as the god of cricketer ,hold many batting records",
      "rohit sharma is know for his elegant batting and record breaking double centuries",
      "jasprit bumrah is an indian fast bowler knows for his unorthodox action and yorker"]

query="who score double centuries"

doc_embedding=embedding.embed_documents(docs)
query_embedding=embedding.embed_query(query)

score=cosine_similarity([query_embedding],doc_embedding)[0]
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print("similarity score is ",score)