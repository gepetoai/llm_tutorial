# Import necessary modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model = "gpt-4o", temperature = 0, max_tokens = 100)

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You tell cat jokes"),
    ("user", "{input}")
])

# Initialize the output parser
output_parser = StrOutputParser()

# Create the processing chain
chain = prompt | llm | output_parser

# Invoke the chain with a user input
res = chain.invoke({"input": "Tell me a joke"})

# Print the result
print(res)