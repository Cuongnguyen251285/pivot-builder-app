import openai

class ChatGPTClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

# Usage example
if __name__ == '__main__':
    api_key = 'your_api_key_here'  # Replace with your actual API key
    client = ChatGPTClient(api_key)
    prompt = "What are the benefits of natural language processing?"
    response = client.get_response(prompt)
    print(response)