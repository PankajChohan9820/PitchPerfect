import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import sseclient
from flask import stream_with_context, json

def askgpt( question, chat_log = None):
    client = OpenAI(
    api_key = os.getenv('OPENAI_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )
    value = chat_completion.choices[0].message.content
    return value



def generate(role_play, my_resume, prompt = '' ):
    try:
        client = OpenAI(
        api_key = os.getenv('OPENAI_KEY'),
        )

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role_play},
            {"role": "user", "content": my_resume},
            {"role": "user", "content": prompt}
        ],
        stream=True
        )

        for chunk in completion:
            try:
                text = chunk.choices[0].delta.content
                # print(text)
                yield text
            except:
                yield ''

    except Exception as e:
        print("Error",str(e))
        return 'Unable to answer'