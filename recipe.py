import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# OpenAI API key
client = OpenAI(api_key=os.getenv('api_key'))


def get_recipes(seasonings, items):
    # Create a conversation-like prompt based on the input
    prompt_text = "Generate one recipe based on the following seasonings and items:\nSeasonings: {}\nItems: {}\n".format(
        ", ".join(seasonings),
        ", ".join(items)
    )
    
    # Call the OpenAI API with the prompt
    response = client.chat.completions.create(model="gpt-4",  # Or the most appropriate model you have access to
    messages=[
        {"role": "system", "content": f"You are a helpful assistant providing recipes."},
        {"role": "user", "content": prompt_text}
    ])

    # Extract the response
    message_content = response.choices[0].message.content
    return message_content

if __name__ == '__main__':
    # Example usage
    seasonings = ['salt', 'pepper', 'paprika', 'soy source', 'ketchap']
    items = ['chicken', 'rice', 'broccoli', 'mango', 'italian pasta', 'beef', 'egg']
    print(get_recipes(seasonings, items))
