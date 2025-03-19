# main.py

from query_parser import parse_query_with_llm
from ollama_client import call_ollama
from weather_api import get_current_weather  # from your Part 2 code
# from weather_tool_definition import weather_tool  # if you need the formal MCP definition

def handle_user_query(user_query: str) -> str:
    """
    1. Ask the LLM to parse the query (is it about weather? which city?)
    2. If action == "get_weather", call the weather API tool.
    3. Use Ollama again to produce a user-friendly final response.
    """
    # Step 1: Decide if we need weather data
    parse_result = parse_query_with_llm(user_query)
    action = parse_result.get("name", "none")
    # print(action)

    # if False:
    if action == "get_weather" and parse_result.get("parameters").get("city", None) is not None and parse_result.get("parameters").get("city", None) != 'none':
        city = parse_result.get("parameters").get("city", "Seattle")
        weather_data = get_current_weather(city)

        # Construct a raw weather info string
        weather_info = (
            f"City: {city}\n"
            f"Conditions: {weather_data['description']}\n"
            f"Temperature: {weather_data['temperature']}°C\n"
            f"Humidity: {weather_data['humidity']}%\n"
        )

        # print(weather_info)

        # Step 2: Ask the LLM to generate a natural-language summary
        # You can embed the raw data in the prompt:
        summary_prompt = f"""
You are a helpful assistant. The user gives a query: {user_query}.


The current weather data is also provided if needed:
{weather_info}

Please provide a concise and helpful answer.
"""
        summary = call_ollama(summary_prompt)

        # Combine or return the final summary
        return summary
    else:
        # If it's not about weather, just pass the user_query directly to the LLM
        generic_response = call_ollama(f"User asked: '{user_query}'. Provide a helpful answer.")
        return generic_response


if __name__ == "__main__":
    # Example usage
    queries = [
        "What is the weather like in Paris right now?",
        "Tell me a joke about the rain.",
        "What is the temperature in Tokyo?",
        "What should I wear if it iss 15°C and rainy?",
        "Who wrote <Pride and Prejudice>?",
        "Compare today's temperature in New York to yesterday's.",
        "Translate <How's the weather today?> into Spanish.",
        "What is the humidity level in Mumbai?",
        "Explain how weather patterns can affect mood, using Seattle as an example.",
    ]

    for q in queries:
        print(f"\n=== User Query: {q} ===")
        response = handle_user_query(q)
        print(f"LLM Response:\n{response}")
