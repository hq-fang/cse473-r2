# query_parser.py

import json
from ollama_client import call_ollama

PROMPT_TEMPLATE = """
<|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023

When you receive a tool call response, use the output to format an answer to the orginal user question.

You are a helpful assistant with tool calling capabilities.<|eot_id|>

<|start_header_id|>user<|end_header_id|>

Given the following functions, please respond with a JSON for a function call with its proper arguments that best answers the given prompt.

Respond in the format {"name": function name, "parameters": dictionary of argument name and its value}. Do not use variables.
{
  "name": "get_weather",
  "description": "Returns the city the user is requesting its real-time wheather. Return none if the user is not requesting real-time wheather.",
  "parameters": {
    "city": "city"
  }
}<|eot_id|>
"""

PROMPT_ADD = """
\n{user_query}<|eot_id|>
"""

def parse_query_with_llm(user_query: str) -> dict:
    """
    Ask the LLM to parse the user's intent. Return a dict like:
      {"name": "get_weather", "city": "Paris"}
    or
      {"name": "none"}
    """
    prompt_add = PROMPT_ADD.format(user_query=user_query)
    prompt = PROMPT_TEMPLATE + prompt_add
    llm_response = call_ollama(prompt)

    # print(llm_response)

    # Attempt to parse the JSON from the LLM's output
    # If parsing fails, default to no name
    try:
        parsed = json.loads(llm_response)
        return parsed
    except json.JSONDecodeError:
        return {"name": "regular_response"}
