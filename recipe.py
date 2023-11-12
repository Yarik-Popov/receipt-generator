import requests
from dataclasses import dataclass


@dataclass
class Recipe:
    """A recipe object"""
    name: str
    ingredients: [str]
    instructions: str
    image: str


def get_recipes(items_to_include: [str]) -> [dict]:
    url = "https://tasty.p.rapidapi.com/recipes/list"

    querystring = {"from":"0","size":"5","q":f"{','.join(items_to_include)}"}

    headers = {
        "X-RapidAPI-Key": "b5169ce81dmsh997426a13200d04p10cfd6jsn184db561d74d",
        "X-RapidAPI-Host": "tasty.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    recipes = response.json()['results']
    output = []
    for i in recipes:
        output.append({
            'name': i['name'],
            'ingredients': parse_ingredients(i['sections'][0]),
            'instructions': parse_instructions(i['instructions']),
            'thumbnail_url': i['thumbnail_url']
        })
    return output


def parse_ingredients(sections: [dict]):
    """Parse the ingredients from the Tasty API"""
    parsed_ingredients = []
    for item in sections['components']:
        parsed_ingredients.append(item['raw_text'])
    return parsed_ingredients


def parse_instructions(instructions: [dict]):
    """Parse the instructions from the Tasty API"""
    parsed_instructions = ''
    for i, val in enumerate(instructions, start=1):
        parsed_instructions += f"{i}. "
        parsed_instructions += (val['display_text'])
        parsed_instructions += '\n'
    return parsed_instructions


if __name__ == '__main__':
    # Example usage
    seasonings = ['salt', 'pepper', 'paprika', 'soy source', 'ketchap']
    items = ['chicken', 'rice', 'broccoli', 'mango', 'italian pasta', 'beef', 'egg']
    print(get_recipes(seasonings, items))
