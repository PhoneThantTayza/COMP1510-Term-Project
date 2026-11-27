"""Scoreboard functions for the COMP 1510 term project.

Write load_scoreboard and save_scoreboard so the arcade keeps scores across
restarts. Their docstrings and the tests in tests/test_scoreboard.py define
the required behavior.
"""
import json

def load_scoreboard(filename):
    """Return the scoreboard read from filename, or an empty one.

    :param filename: name of a JSON scoreboard file
    :return: the scoreboard as a dictionary. The caller still checks the
             nested record shape, as the README describes
    """

    try:
        with open(filename, encoding="utf-8") as file:
            scoreboard = json.load(file)
    except FileNotFoundError:
        print("Scoreboard not found, starting fresh")
        return {}
    except json.JSONDecodeError:
        print("The scoreboard is not a correct JSON format, starting fresh")
        return {}

    if not isinstance(scoreboard, dict):
        print("The scoreboard is not a dictionary, starting fresh")
        return {}
    return scoreboard


def save_scoreboard(scoreboard, filename):
    """Write the scoreboard to filename as JSON.

    :param scoreboard: the scoreboard dictionary to write
    :param filename: name of the JSON scoreboard file
    :return: None
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(scoreboard,file, indent=2)
