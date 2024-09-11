from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    api_key = data.get('apiKey')
    description = data.get('description')

    if not api_key or not description:
        return jsonify({'error': 'API key and description are required.'}), 400

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        'prompt': description,
        'n': 1,
        'size': '512x512'
    }

    try:
        response = requests.post('https://api.openai.com/v1/images/generations', json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        image_url = data['data'][0]['url']
        return jsonify({'imageUrl': image_url})
    except requests.exceptions.HTTPError as http_err:
        error_message = response.json().get('error', {}).get('message', str(http_err))
        return jsonify({'error': error_message}), response.status_code
    except Exception as err:
        return jsonify({'error': 'An error occurred while generating the image.'}), 500

if __name__ == '__main__':
    app.run()
