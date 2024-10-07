from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

#Define inputs
system_prompt = "You tell cat jokes"  #this can be really long
user_inquiry = "Tell me a joke"

#Call Groq
res = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_inquiry}
    ],
    temperature = 0,
    max_tokens = 100)

print(res.choices[0].message.content) #res has alot of other stuff worth exploring

