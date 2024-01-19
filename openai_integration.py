import os
import openai
from dotenv import load_dotenv
from prompt_toolkit import print_formatted_text, HTML

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

def send_message_to_gpt4(message):
    try:
        response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        content = response.choices[0].message.content if response.choices else None
        
        return content
    except Exception as e:
        print_formatted_text(HTML(f'<ansired>Error communicating with OpenAI: {e}</ansired>'))
        return None
