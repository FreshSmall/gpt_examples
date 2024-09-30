from openai import OpenAI
import os

#client = OpenAI()
client = OpenAI(
    api_key=os.environ['api_key'],
    base_url=os.environ['base_url']
)

class ResponseService():
     def __init__(self):
        pass
     
     def generate_response(self, facts, user_question):
         response = client.chat.completions.create(model="gpt-3.5-turbo",
         messages=[
               {"role": "user", "content": 'Based on the FACTS, give an answer to the QUESTION.'+ 
                f'QUESTION: {user_question}. FACTS: {facts}'}
            ])

         # extract the response
         return (response.choices[0].message.content)