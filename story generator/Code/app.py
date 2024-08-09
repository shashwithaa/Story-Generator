from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline
import os

app = Flask(__name__, static_folder='static')

# Load a text generation model
generator = pipeline('text-generation', model='gpt2')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/styles.css')
def serve_css():
    return send_from_directory(app.static_folder, 'styles.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory(app.static_folder, 'script.js')

@app.route('/generate', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt', '')
    print(f"Received data: {data}")  # Debug print
    if prompt:
        print(f"Received prompt: {prompt}")  # Debug print
        story = generator(prompt, max_length=300, num_return_sequences=1, pad_token_id=50256)[0]['generated_text']
        print(f"Generated story: {story}")  # Debug print
        return jsonify({'story': story})
    else:
        return jsonify({'error': 'No prompt provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
