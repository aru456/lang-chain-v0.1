from dotenv import load_dotenv
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import firestore

load_dotenv()
PROJECT_ID = "langchain-learn-3c260"
SESSION_ID = "user_session_new"
COLLECTION_NAME =  "chat_history"


print("Initializing firestore client...")

client = firestore.Client(project = PROJECT_ID)

print("Initializing firestore chat message history....")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client
)
print("Chat history Initialized.")

# Check if chat history is empty and add system message if it is
if len(chat_history.messages) == 0:
    system_prompt = "You are a helpful AI assistant that provides concise and accurate information."
    chat_history.add_message(SystemMessage(content=system_prompt))
    print(f"Added system prompt: '{system_prompt}'")

model = ChatOpenAI(model = "gpt-5-mini")

#Chat Loop
while True:
    human_input = input("User : ")
    if human_input.lower() == "exit":
        break
    chat_history.add_user_message(human_input)
    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI : {ai_response.content}")


print("--------Message History Saved----------")
messages = chat_history.messages  # This uses the synchronous property
for message in messages:
    if isinstance(message, SystemMessage):
        print(f"System: {message.content}")
    elif isinstance(message, HumanMessage):
        print(f"User: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"AI: {message.content}")
    else:
        print(f"Other: {message.content}")