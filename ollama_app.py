import requests
import json

print("Script starting...")

def ask_ollama(question, model="llama3.2:3b"):
    print(f"Asking Ollama: {question}")
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': model,
                'prompt': question,
                'stream': False  
            }
        )
        
        # Print the raw response for debugging
        print(f"Status code: {response.status_code}")
        print(f"Response text (first 200 chars): {response.text[:200]}")
        
        if response.status_code == 200:
            try:
                # Try to parse the JSON response
                resp_json = response.json()
                return resp_json.get('response', 'No response field found')
            except json.JSONDecodeError as e:
                return f"Error decoding JSON: {str(e)}, Response: {response.text[:500]}"
        else:
            return f"Error: {response.status_code}"
            
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}"

print("Ready to ask a question...")
# Example usage
if __name__ == "__main__":
    question = input("Ask Ollama a question: ")
    print("\nOllama is thinking...\n")
    answer = ask_ollama(question)
    print(answer)