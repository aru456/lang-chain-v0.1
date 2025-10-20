from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")


#part 1
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic" : "cats"})
result = model.invoke(prompt)
print(result.content)

#part 2 - prompt with multiple place holder

template_multiple = """You are a helpful assistant.
Human : Tell me a {adjective} short story about a {animal}
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective" : "funny" , "animal" : "panda"})
result = model.invoke(prompt)
print(result.content)



