from openai import OpenAI

#client = OpenAI()

client = OpenAI(
  api_key="gAAAAABmFmLplODi2NxnZYnkqEG177I6cfZguGJ_kYncc6y95ViTka9uMryxXla1KJWSRtp2Lv7-p5Gk-rCxMvALTUneEykefaUIkhPeD_uDam3ENi2OMoKn3ui5FWMIeHcbUXfbQ_Yl",
  base_url="https://aiops-api.baijia.com/openai/v1"
)

class IntentService():
     def __init__(self):
        pass
     
     def get_intent(self, user_question: str):
         # call the openai ChatCompletion endpoint
         response = client.chat.completions.create(model="gpt-3.5-turbo",
         messages=[
               {"role": "user", "content": f'Extract the keywords from the following question: {user_question}'+
                 'Do not answer anything else, only the keywords.'}
            ])

         # extract the response
         return (response.choices[0].message.content)