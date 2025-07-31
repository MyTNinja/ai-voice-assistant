from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

TEMPLATE = """
You are a helpful AI assistant.

Here is the conversation history:
{context}

Question:
{question}

(Respond in a helpful and concise tone, without any formatting to the text)
"""

model = OllamaLLM(model='deepseek-r1')
prompt = ChatPromptTemplate.from_template(template=TEMPLATE)
chain = prompt | model
