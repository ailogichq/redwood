from redwood.redwood import Redwood

# Create an instance of the Redwood class and load data, set a model, and set an agent
redwood = Redwood().data(["data_syntax_v1_dataset_json.json","csv_metrics.csv"]).model("OpenAI", api_key='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').agent("CSV")
#redwood = Redwood().data("csv_metrics.csv").model("OpenAI", api_key='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').agent("CSV")

# redwood = Redwood().model("OpenAI", api_key="sk-puU33Bq9WMW8nxMzgefnq0CdMVn4anGOtoEmPSPw").agent("Python")

# Ask a question about the data
# response = redwood.ask("write me a simple python chatbot in the terminal")
# print(response)

# def chatbot():
#     print("Hello, I'm a chatbot. What can I help you with?")
#     user_input = input()
#     if (user_input==''):
#         exit
#     response = redwood.ask(user_input)
#     print(response)

# while (True):
#     chatbot()



while True:
    message = input("You: ")

    if (message==''):
        break
    output = redwood.ask(message)
    print("AI Agent: ", output)
