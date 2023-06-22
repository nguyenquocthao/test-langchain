task: input image => captioning; image captioning; google vision

LLMs: Large Language Models, take a text string as input, return a text string

A word is a unit of language that has meaning and is typically separated by spaces in written text. For example, "cat", "dog", "house", and "apple" are all words in the English language.

A token, on the other hand, is a sequence of characters that represents a unit of meaning in a text. Tokens can be words, but they can also be punctuation marks, numbers, or any other sequence of characters that are meaningful in a given context. For example, in the sentence "I have 2 cats.", there are four tokens: "I", "have", "2", and "cats". "2" is a token, but not a word, because it represents a number rather than a linguistic unit.


Text Embedding Models

The third type of models we cover are text embedding models. These models take text as input and return a list of floats.

In text embedding models, the list of floats that is returned represents a vector that captures the semantic meaning of the input text. Each float in the vector represents a dimension in the semantic space, and the combination of values across all dimensions represents the overall meaning of the text.

The specific meaning of each float in the vector is not directly interpretable by humans, but their values are learned through a training process that seeks to maximize the model's ability to predict certain outcomes, such as document classification or language translation.



prompt_tokens: This refers to the number of tokens that you provide as input to the language model in order to generate text. 
completion_tokens: This refers to the number of tokens that the language model generates as output in response to the provided input.

prompt_tokens are input tokens, and completion_tokens are output tokens



https://python.langchain.com/en/latest/modules/models/llms/examples/streaming_llm.html

ChatAnthropic: ChatAnthropic is a wrapper around Anthropic large language models. To use it, you should have the @anthropic-ai/sdk package installed, with the ANTHROPIC_API_KEY environment variable set.


https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/image_captions.html

from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv
load_dotenv()
index = VectorstoreIndexCreator().from_loaders([loader])

=> index.query only read from already queried caption

/home/ubuntu/.local/lib/python3.8/site-packages/langchain/document_loaders/image_captions.py

Image.open 
def open(fp, mode="r"):
    """
    Opens and identifies the given image file.

    This is a lazy operation; this function identifies the file, but
    the file remains open and the actual image data is not read from
    the file until you try to process the data (or call the
    :py:meth:`~PIL.Image.Image.load` method).  See
    :py:func:`~PIL.Image.new`. See :ref:`file-handling`.

    :param fp: A filename (string), pathlib.Path object or a file object.
       The file object must implement :py:meth:`~file.read`,
       :py:meth:`~file.seek`, and :py:meth:`~file.tell` methods,
       and be opened in binary mode.
    :param mode: The mode.  If given, this argument must be "r".
    :returns: An :py:class:`~PIL.Image.Image` object.
    :exception FileNotFoundError: If the file cannot be found.
    :exception PIL.UnidentifiedImageError: If the image cannot be opened and
       identified.
    :exception ValueError: If the ``mode`` is not "r", or if a ``StringIO``
       instance is used for ``fp``.
    """


Todo:
- Vuejs / appsmith server frontend
- backend python
- 



Todo:
- run mm-react
- https://github.com/microsoft/MM-REACT

Run using google colab research resource:
https://colab.research.google.com/drive/1SiTOnQW2B-zyxcMWT7_fkE5UBUiUZaqy#scrollTo=9r0sKf-62YFK

https://onnx.ai/
ONNX is an open format built to represent machine learning models. ONNX defines a common set of operators - the building blocks of machine learning and deep learning models - and a common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes, and compilers

https://docs.streamlit.io/


https://learn.microsoft.com/en-us/answers/questions/1191884/how-to-fix-the-error-using-azure-openai-model-endp

https://azure.microsoft.com/en-us/products/cognitive-services/vision-services


https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

https://levelup.gitconnected.com/amazing-i-created-my-own-image-based-chatbot-powered-by-chatgpt-api-azure-79845f1eff86



langchain Tools: 
SerpAPI.run : Langchain creator -> Harrison Chase - Co-
Bing search run: Langchain creator -> <b>LangChain.</b> At its core,<b> LangChain</b> is a framework built around LLMs. We can use it for chatbots, G enerative Q uestion- A nswering (GQA), summarization, and much more. The core idea of the library is that we can<b> “chain”</b> together different components to create more advanced use cases around LLMs. Photo by Christopher Gower on Unsplash. In the previous articles (1,2), we saw that LLMs could generate and execute coding instructions sequences — however, often, they get stuck on errors, especially related to package installation.I wanted to have something similar to <b>Langchain</b> Python REPL, but that instead: Allowed the generated source code to be saved in a file. <b>LangChain</b> is a software development framework designed to simplify the creation of applications using large language models (LLMs). As a language model integration framework,<b> LangChain&#39;s</b> use-cases largely overlap with those of language models in general, including document analysis and summarization , chatbots , and code analysis. <b>LangChain</b> is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model, but will also be: Data-aware: connect a language model to other sources of data Agentic: allow a language model to interact with its environment <b>GitHub</b> - logspace-ai/langflow: ⛓️ LangFlow is a UI for <b>LangChain</b>, designed with react-flow to provide an effortless way to experiment and prototype flows. logspace-ai langflow dev 62 branches 42 tags Code ogabrielluiz feat (langflow): add version endpoint to API efbdd6f 5 hours ago 1,783 commits .devcontainer docs: add readme guide 2 months ago Yeager.ai: Yeager.ai Agent is the first<b> Langchain</b> Agent<b> creator</b> designed to help you build, prototype, and deploy AI-powered agents with ease ; Services. GPTCache: A Library for Creating Semantic Cache for LLM Queries ; Gorilla: An API store for LLMs ; LlamaHub: a library of data loaders for LLMs made by the community Yeager.ai Agent is the first <b>Langchain</b> Agent <b>creator</b> designed to help you build, prototype, and deploy AI-powered agents with ease. With an emphasis on flexibility, interactivity, and seamless integration, Yeager.ai Agent is the perfect tool for developers, researchers, and AI enthusiasts alike. <b>LangChain</b> 101: Build Your Own GPT-Powered Applications.<b> LangChain</b> is a Python library that helps you build GPT-powered applications in minutes. Get started with<b> LangChain</b> by building a simple question-answering app. By Bala Priya C, KDnuggets on April 3, 2023 in Natural Language Processing.

serpapi.run: calling results(str)-> dict and _process_response(dict)->str




CHAT_CONVERSATIONAL_REACT_DESCRIPTION

----------------
system
content='Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful system that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.' additional_kwargs={}
----------------
----------------
human
content="Hello, I'm thao" additional_kwargs={} example=False
----------------
----------------
ai
content='Hello Thao! How can I assist you today?' additional_kwargs={} example=False
----------------
----------------
human
content="What's my name?" additional_kwargs={} example=False
----------------
----------------
ai
content='Your name is Thao' additional_kwargs={} example=False
----------------
----------------
human
content='tell me the last letter in my name, and also tell me who won the world cup in 1978?' additional_kwargs={} example=False
----------------
----------------
ai
content="The last letter in your name is 'o'. Argentina won the World Cup in 1978." additional_kwargs={} example=False
----------------
----------------
human
content='TOOLS\n------\nAssistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:\n\n> Search: A search engine. Useful for when you need to answer questions about current events. Input should be a search query. Prefer other specific search tool if possible\n> Calculator: Useful for when you need to answer questions about math.\n> BingSearch: Useful for when you need to answer questions about literature or temperature or health. Input should be in Vietnamese\n\nRESPONSE FORMAT INSTRUCTIONS\n----------------------------\n\nWhen responding to me, please output a response in one of two formats:\n\n**Option 1:**\nUse this if you want the human to use a tool.\nMarkdown code snippet formatted in the following schema:\n\n```json\n{\n    "action": string, \\ The action to take. Must be one of Search, Calculator, BingSearch\n    "action_input": string \\ The input to the action\n}\n```\n\n**Option #2:**\nUse this if you want to respond directly to the human. Markdown code snippet formatted in the following schema:\n\n```json\n{\n    "action": "Final Answer",\n    "action_input": string \\ You should put what you want to return to use here\n}\n```\n\nUSER\'S INPUT\n--------------------\nHere is the user\'s input (remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else):\n\nDo you know Adastra visual novel by EchoProject?' additional_kwargs={} example=False
----------------
----------------
ai
content='{\n    "action": "Search",\n    "action_input": "Adastra visual novel EchoProject"\n}' additional_kwargs={} example=False
----------------
----------------
human
content="TOOL RESPONSE: \n---------------------\nAdastra is a romance visual novel with a whole bunch of sci-fi and political intrigue mixed in. You'll experience the perils of navigating an empire in ...\n\nUSER'S INPUT\n--------------------\n\nOkay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else." additional_kwargs={} example=False
----------------


[
   {
      "role":"system",
      "content":"Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful system that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist."
   },
   {
      "role":"user",
      "content":"Hello, I'm thao"
   },
   {
      "role":"assistant",
      "content":"Hello Thao! How can I assist you today?"
   },
   {
      "role":"user",
      "content":"What's my name?"
   },
   {
      "role":"assistant",
      "content":"Your name is Thao"
   },
   {
      "role":"user",
      "content":"tell me the last letter in my name, and also tell me who won the world cup in 1978?"
   },
   {
      "role":"assistant",
      "content":"The last letter in your name is 'o'. Argentina won the World Cup in 1978."
   },
   {
      "role":"user",
      "content":"TOOLS\n------\nAssistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:\n\n> Search: A search engine. Useful for when you need to answer questions about current events. Input should be a search query. Prefer other specific search tool if possible\n> Calculator: Useful for when you need to answer questions about math.\n> BingSearch: Useful for when you need to answer questions about literature or temperature or health. Input should be in Vietnamese\n\nRESPONSE FORMAT INSTRUCTIONS\n----------------------------\n\nWhen responding to me, please output a response in one of two formats:\n\n**Option 1:**\nUse this if you want the human to use a tool.\nMarkdown code snippet formatted in the following schema:\n\n```json\n{\n    \"action\": string, \\ The action to take. Must be one of Search, Calculator, BingSearch\n    \"action_input\": string \\ The input to the action\n}\n```\n\n**Option #2:**\nUse this if you want to respond directly to the human. Markdown code snippet formatted in the following schema:\n\n```json\n{\n    \"action\": \"Final Answer\",\n    \"action_input\": string \\ You should put what you want to return to use here\n}\n```\n\nUSER'S INPUT\n--------------------\nHere is the user's input (remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else):\n\nDo you know Adastra visual novel by EchoProject?"
   },
   {
      "role":"assistant",
      "content":"{\n    \"action\": \"Search\",\n    \"action_input\": \"Adastra visual novel EchoProject\"\n}"
   },
   {
      "role":"user",
      "content":"TOOL RESPONSE: \n---------------------\nAdastra is a romance visual novel with a whole bunch of sci-fi and political intrigue mixed in. You'll experience the perils of navigating an empire in ...\n\nUSER'S INPUT\n--------------------\n\nOkay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else."
   }
]

Get memory:

memory.chat_memory.messages
memory.buffer

http://localhost:8888/notebooks/adding_memory_chain_multiple_inputs.ipynb
=> use vectorstores Chroma