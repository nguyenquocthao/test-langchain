import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI, AzureOpenAI

from dotenv import load_dotenv

load_dotenv()

# print(os.environ["OPENAI_API_KEY"], os.environ["SERPAPI_API_KEY"])
# os.environ["OPENAI_API_KEY"] = 
if os.environ.get("OPENAI_API_TYPE", "") == "azure":
    print(12, "fdnfdn")
    llm = AzureOpenAI(deployment_name="gpt-35-turbo-version-0301", model_name="gpt-35-turbo (version 0301)", temperature=0, max_tokens=512)
else:
    llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# agent.run(
#     "What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?"
# )

agent.run(
    "Langchain difference between OpenAI and AzureOpenAI"
)

# print(llm("Do you know langchain? Do you have the link to langchain?"))
