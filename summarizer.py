from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_abstract(abstract: str) -> str:
    prompt = f"""
    Summarize the following abstract. 
    Make sure to include:
    1. Premise and unmet need 
    2. Methods
    3. Key findings
    4. Limitations and future direction

    Abstract: {abstract}
    """

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()