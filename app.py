from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import emotion  # Import your emotion detection script

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return jsonify({"message": "POST request received at /, but try /chat instead"}), 400
    return "Service is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Happiness Detection (using detect_happiness function from emotion.py)
    if emotion.detect_happiness(user_message):
        bot_response = "I detected happiness! How can I help?"
    else:
        bot_response = "I didn't detect any happiness. How can I assist you?"

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 10000))  # Use assigned port or default to 10000
    app.run(host='0.0.0.0', port=port, debug=True)
