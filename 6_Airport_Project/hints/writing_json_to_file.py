"""
We want to write a dictionary as JSON to a file.
"""
import json  # standard library for json handling
import tempfile  # create temporary files for testing

FILENAME = "./recipe.json"
banana_cake = {
    "eggs": 2,
    "butter": "1/2 cup",
    "bananas": 6,
    "flour": "1 cups",
    "sugar": "1/2 cup",
}

with open(FILENAME, "w") as f_write:
    json.dump(banana_cake, f_write)

with open(FILENAME, "r") as f_read:
    recipe = json.load(f_read)

print(recipe)
