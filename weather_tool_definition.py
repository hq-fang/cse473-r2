# weather_tool_definition.py

weather_tool = {
    "name": "WeatherTool",
    "description": "Provides real-time weather information for a given city",
    "context_schema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city for which weather data is requested"
            }
        },
        "required": ["city"]
    },
    "actions": [
        {
            "name": "get_current_weather",
            "description": "Fetch current weather data for the specified city",
            "input_schema": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "description": {"type": "string"},
                    "temperature": {"type": "number"},
                    "humidity": {"type": "number"}
                },
                "required": ["description", "temperature", "humidity"]
            }
        }
    ]
}
