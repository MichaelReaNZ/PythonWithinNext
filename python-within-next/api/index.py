from fastapi import FastAPI

#Langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#Environment variables
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get("/api/python")
def predict():    
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-3.5-turbo") 

    #set the model to use 'gpt-3.5-turbo'

    #vartiable for result 
    result = llm.predict("Tell me a joke about goats.")

    #print
    print(result)

    return {"message": result}
