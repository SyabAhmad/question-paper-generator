import openai
import os
import requests
from dotenv import load_dotenv
load_dotenv()
key = openai.api_key = os.getenv("OPENAIAPIKEY")

endpoint = "https://api.openai.com/v1/completions"
def generate(bookName, classs,chapterName, levelOfPaper,typePaper):
    
    textToReturn = ''
    
    params = {
            'model': "gpt-3.5-turbo-instruct",
            'prompt': f'Generate a {typePaper} test or quiz (don"t include any pattern of the paper or quiz, just questions no more nonsense) for class {classs}, the name of the book is {bookName} and the chapter name is {chapterName}, and should be {levelOfPaper}',
            'max_tokens': 2000,

        }

    response2 = requests.post(endpoint, json=params, headers={"Authorization": f'Bearer {key}'})

    if response2.status_code == 200:
        result = response2.json()
        textToReturn = result['choices'][0]['text']
    else:
        return response2.status_code
    index = 0
    
    return textToReturn
