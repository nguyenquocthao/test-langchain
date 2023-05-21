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