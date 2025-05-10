import os
from langchain.chat_models import openai
from langchain_core.messages import HumanMessage, SystemMessage


class Model:
    llm = openai.ChatOpenAI(
        model="gpt-4-turbo",
        temperature=0,
        api_key=os.environ['OPENAI_API_KEY'],
    )
    messages = [
        SystemMessage(content="You are a math tutor with years of experience.")
        
    ]