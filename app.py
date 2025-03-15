from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    model = data.get('model', 'llama3.2:3b')
    
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': model,
                'prompt': question,
                'stream': False
            }
        )
        
        if response.status_code == 200:
            answer = response.json().get('response', 'No response found')
            return jsonify({'answer': answer})
        else:
            return jsonify({'error': f"Error: {response.status_code}"}), 500
            
    except Exception as e:
        return jsonify({'error': f"Error connecting to Ollama: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)