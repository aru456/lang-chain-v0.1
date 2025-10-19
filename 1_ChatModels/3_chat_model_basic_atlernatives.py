import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "3"


load_dotenv()

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
)
messages  = [
    SystemMessage(content="Answer the following quesions"),
    HumanMessage(content='Pick a random number from 1- 100'),
]

result = model.invoke(messages)
print(f"Answer from ChatGPT :\n{result.content}")


# model = ChatAnthropic(model = "claude")
messages  = [
    SystemMessage(content="Answer the following quesions"),
    HumanMessage(content='Pick a random number from 1- 100'),
]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = model.invoke(messages)
print(f"Answer from Googles Model :\n{result.content}")
