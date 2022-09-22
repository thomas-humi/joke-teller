#!/usr/bin/env python
"""A joke teller."""

import json
import random

with open("jokes.json", encoding="UTF-8") as file:
    jokes = json.load(file)

joke = random.choice(jokes)

text = "Here's a good joke: \n\n" + joke["setup"] + "\n\n" + joke["punchline"]

print(text)
