from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

#Define inputs
system_prompt = "<prompt>You tell cat jokes</prompt>"  #this can be really long
user_inquiry = "<user input>Tell me a joke</user input>"

#Call Anthropic
res = client.messages.create(
    model="claude-3-5-sonnet-20240620", 
    system=system_prompt,
    messages=[
        {"role": "user", "content": user_inquiry},
    ],
    temperature = 0,
    max_tokens = 100)

print(res.content[0].text)

