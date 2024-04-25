from uuid import NAMESPACE_DNS, uuid3
from openai import OpenAI
import os
import json


def create_message(role: str, content: str) -> dict:
    '''
    Helper function to create a message dictionary. 
    Parameters:
        role: str: 'user' or 'system'
        content: str: Message content
    '''
    return {'role': role, 'content': content}

def chat_request(user_msg, system_msg=None, model="gpt-3.5-turbo", response_format='text'):
    '''
    Function to send a request to GPT model and get response.
    Parameters:
    - user_msg (str): The user message text.
    - system_msg (str, optional): Optional system message text.
    - model (str, optional): Model name to use.
    Returns:
    - dict: Parsed JSON response from the GPT model.
    '''

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    seed = 4242024
    messages = []

    if system_msg:
        messages.append(create_message('system', system_msg))
    if user_msg:
        messages.append(create_message('user', user_msg))
    
    # Send request to the GPT model
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.1,
        max_tokens=512,
        seed=seed,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={'type': response_format}
    )
    if response_format == 'json_object':
        return json.loads(response.choices[0].message.content)
    return response.choices[0].message.content