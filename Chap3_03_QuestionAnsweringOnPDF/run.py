from dotenv import load_dotenv

load_dotenv()
from intentservice import IntentService
from responseservice import ResponseService
from dataservice import DataService


if __name__ == '__main__':
    # Example pdf
    #pdf = 'files/ExplorersGuide.pdf'
    pdf = 'file/MicroSip.pdf'

    data_service = DataService()

    # Drop all data from redis if needed
    data_service.drop_redis_data()

    # Load data from pdf to redis
    data = data_service.pdf_to_embeddings(pdf)

    data_service.load_data_to_redis(data)

    intent_service = IntentService()
    response_service = ResponseService()

    # Question
    question = '祥云服务商的账号名、用户名和登良名的格式是什么？'
    # Get the intent
    intents = intent_service.get_intent(question)
    print("intent: ", intents)
    # Get the facts
    facts = data_service.search_redis(intents)
    print("facts: ", facts)
    # Get the answer
    answer = response_service.generate_response(facts, question)
    print(answer)