from fastapi import FastAPI
from pydantic import BaseModel
import openai

class Message(BaseModel):
    role: str

class CompletionInputModel(BaseModel):
    messages: list

app = FastAPI()

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}

@app.post('/completar/teste')
def create_item(inputModel: CompletionInputModel):
    return inputModel.messages

@app.post('/completar/')
def create_item(inputModel: CompletionInputModel):

    OPENAI_API_KEY = "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"
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
            model="ft:gpt-3.5-turbo-0613:personal::81NwI1HE",
            messages=inputModel.messages,
            max_tokens = 100,
            temperature = 0.2
        )
    
    

    return response




#uvicorn gpt-ucs-api:app --reload