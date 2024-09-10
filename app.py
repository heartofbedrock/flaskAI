from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Image Generation API is running!"

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    api_key = data['apiKey']
    description = data['description']

    # Mock response, replace this with actual API call (e.g., DALL·E, etc.)
    response = requests.post('https://image-generation-api.example.com/generate', json={
        'api_key': api_key,
        'description': description
    })

    # Simulating success and returning a mock image URL
    if response.status_code == 200:
        image_url = response.json().get('image_url', 'https://placekitten.com/400/400')
        return jsonify({'imageUrl': image_url})
    else:
        return jsonify({'error': 'Failed to generate image'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
