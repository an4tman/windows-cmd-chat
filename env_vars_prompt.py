import os
from prompt_toolkit import ANSI

def get_formatted_prompt():
    cwd = os.getcwd()
    prompt = ANSI(f'{cwd} > ')
    return prompt
