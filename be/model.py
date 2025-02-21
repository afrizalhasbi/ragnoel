# model iki isine function ngecall LLMe
# misale isine openai
#

from openai import OpenAI


def prompt(message):
    pass

def hit_endpoint(message):
    # preprocessing, header, dll
    message = [{
        "role" : "user",
        "content" : message
    }]
    output = prompt(message)
