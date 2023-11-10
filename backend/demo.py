import os
from dotenv import load_dotenv
from openai import OpenAI

def askgpt(question, chat_log=None):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    

    client = OpenAI(
    api_key="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",  # this is also the default, it can be omitted
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
    print(chat_completion)
    return

askgpt('Hi')