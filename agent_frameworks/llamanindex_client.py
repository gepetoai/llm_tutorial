from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4o", temperature = 0, max_tokens = 100)

messages = [
    ChatMessage(role="system", content="You tell cat jokes"),
    ChatMessage(role="user", content="Tell me a joke"),
]

resp = llm.chat(messages)
print(resp.message.content)