"""Script demonstrates how to use the OpenAI API to generate a response from a model."""

from openai import OpenAI

from main.settings import OpenAISettings

api_key = OpenAISettings().api_key
client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4.1", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
