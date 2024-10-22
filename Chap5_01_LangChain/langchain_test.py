from dotenv import load_dotenv
#from openai import OpenAI
from langchain_openai import OpenAI
load_dotenv()

if __name__ == '__main__':
    llm = OpenAI()
    llm.invoke("Hello how are you?")