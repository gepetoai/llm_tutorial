from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature = 0, max_tokens = 100)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You tell cat jokes"),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
res = chain.invoke({"input": "Tell me a joke"})
print(res)