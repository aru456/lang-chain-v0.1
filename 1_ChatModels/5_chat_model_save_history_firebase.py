from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")

chat_history = []

system_message = SystemMessage(content = "You are an helpful AI assistant.")
chat_history.append(system_message)

#Chat Loop
while True:
    query = input("You : ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query)) # add user query to chat history

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) # Add AI response to history

    print(f"AI : {response}")


print("--------Message History----------")
print(chat_history)