import os
from dotenv import load_dotenv
from openai import OpenAI

def askgpt(question, chat_log=None):
    client = OpenAI(
    api_key=os.getenv('OPENAI_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )
    value = chat_completion.choices[0].message.content
    return value