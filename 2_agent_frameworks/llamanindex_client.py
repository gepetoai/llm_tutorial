# Import necessary modules
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI language model
llm = OpenAI(model="gpt-4o", temperature=0, max_tokens=100)

# Define the chat messages
messages = [
    ChatMessage(role="system", content="You tell cat jokes"),
    ChatMessage(role="user", content="Tell me a joke"),
]

# Generate a response using the language model
resp = llm.chat(messages)

# Print the content of the response
print(resp.message.content)