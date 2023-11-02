from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, load_tools, initialize_agent
import langchain
langchain.debug=True
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
agent = initialize_agent(load_tools(['llm-math', 'wikipedia'], llm=llm), llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION)

a = agent.run("What is the 25% of 300?")
b = agent.run("Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?")

print(a,b,sep='\n\n')