import json

from recipes.models import Ingredient


def run():
    with open('data/ingredients.json') as f:
        data = json.load(f)
        for item in data:
            ingredient = Ingredient.objects.get_or_create(
                name=item['name'],
                ingredient_amount=item['ingredient_amount'])
            ingredient.save()
