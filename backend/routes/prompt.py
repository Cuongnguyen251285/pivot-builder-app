import openai
import json

class PromptParser:
    def __init__(self, api_key):
        openai.api_key = api_key

    def parse_command(self, command):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": command}
            ]
        )
        return json.loads(response['choices'][0]['message']['content'])

# Example usage:
# parser = PromptParser(api_key="your_api_key")
# config = parser.parse_command("Create a pivot table with sales data by region and month.")
# print(config)