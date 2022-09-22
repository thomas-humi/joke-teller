#!/usr/bin/env python
"""A joke teller."""

import json
import random


def get_jokes():
    """Gets a joke from a file."""
    with open("jokes.json", encoding="UTF-8") as file:
        return json.load(file)


def get_random_joke(jokes):
    """Gets a random joke."""
    return random.choice(jokes)


def print_joke(joke):
    """Prints a joke."""
    print("Here's a good joke: \n\n" + joke["setup"] + "\n\n" + joke["punchline"])


def main():
    """Main function"""
    jokes = get_jokes()
    joke = get_random_joke(jokes)
    print_joke(joke)


if __name__ == "__main__":
    main()
