from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.llms import OpenAI
from langchain_openai import OpenAI


load_dotenv()


def chat_openai():
    llm = ChatOpenAI()
    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]
    response = llm.invoke(messages)
    print(response)
#

# def openai():
#     llm = OpenAI()
#     text = "why elon musk is so smart?"
#     print(llm.invoke(text))


if __name__ == '__main__':
    chat_openai()
