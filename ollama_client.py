# ollama_client.py
import subprocess

def call_ollama(prompt: str, model_name: str = "llama3.2") -> str:
    """
    Calls Ollama with the given prompt using the specified model.
    Returns the LLM's output as a string.
    """
    cmd = ["ollama", "run", model_name]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt)

    if process.returncode != 0:
        print("Error calling Ollama:", stderr)
        return "I'm sorry, I had trouble generating a response."

    return stdout.strip()
