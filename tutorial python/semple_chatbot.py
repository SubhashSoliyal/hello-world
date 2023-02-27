from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY") # "your_api_key"

@app.route('/api/messages', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return jsonify({'message': response.choices[0].text})

if __name__ == '__main__':
    app.run()
