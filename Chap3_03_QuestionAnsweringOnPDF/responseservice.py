from openai import OpenAI

#client = OpenAI()
client = OpenAI(
  api_key="gAAAAABmFmLplODi2NxnZYnkqEG177I6cfZguGJ_kYncc6y95ViTka9uMryxXla1KJWSRtp2Lv7-p5Gk-rCxMvALTUneEykefaUIkhPeD_uDam3ENi2OMoKn3ui5FWMIeHcbUXfbQ_Yl",
  base_url="https://aiops-api.baijia.com/openai/v1"
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