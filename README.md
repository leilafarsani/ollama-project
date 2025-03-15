# Ollama Integration Project

A collection of tools for interacting with Ollama, a framework for running large language models locally.

## Project Overview

This repository contains multiple ways to interact with Ollama:

1. **Command Line Interface** - A simple Python script for interacting with Ollama via the terminal
2. **Parchat Web Interface** - A Flask-based web application for chatting with Ollama models

## Features

- Connect to locally running Ollama models
- Send prompts and receive responses
- Simple but functional web interface

## Requirements

- Python 3.6+
- Ollama installed and running locally
- Required Python packages:
  - requests
  - flask (for web interface)

## Installation

1. Clone this repository
2. Install dependencies:

   `pip install -r requirements.txt`

3. Make sure Ollama is installed and running:

    `ollama serve`

## Usage

### Command Line Interface 
`python3 ollama_app.py`

This will start a simple command-line chat with your default Ollama model.

### Parchat Web Interface

`python3 app.py`

Then open your browser and navigate to http://127.0.0.1:5000 to use the web interface.

## Project Structure

- `ollama_app.py` - Command line interface for Ollama
- `app.py` - Flask web application
- `templates/` - HTML templates for the web interface
  - `index.html` - Main chat interface

## Future Development

Planned enhancements:
- Improved styling for the web interface
- Model selection dropdown to choose between available models
- Support for model parameters (temperature, etc.)
- Conversation history saving
- Document Q&A capabilities
- Support for multi-modal models

## Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)

## License

MIT



