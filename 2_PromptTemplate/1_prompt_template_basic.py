from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# template = "Tell me {number} jokes about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)


# def build_prompt(topic, num=2):
#     print("======Prompt from Template=======")
#     prompt = prompt_template.invoke({"topic": topic, "number" :num})
#     return prompt

# def call_model(prompt):
#     model = ChatOpenAI(model = "gpt-5-mini")
#     res = model.invoke(prompt)
#     print(res.content)

# topic = input("Enter an animal name : ")
# num = input("How many jokes ? ")
# prompt = build_prompt(topic,num)
# call_model(prompt)

messages = [
    ("system" , "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes"),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count" : 3})
print("\n-----Prompt with humand and system messages (Tuple)-------")
print(prompt)


