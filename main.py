import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

# print(os.environ["OPENAI_API_KEY"], os.environ["SERPAPI_API_KEY"])
# os.environ["OPENAI_API_KEY"] = 

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# agent.run(
#     "What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?"
# )

agent.run(
    "What is langchain ChatAnthropic?"
)

# print(llm("Do you know langchain? Do you have the link to langchain?"))
