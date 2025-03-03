from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import emotion  # Import your emotion detection script

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Service is running!"})

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.json
        user_message = data.get("message", "")
        
        # Happiness Detection (using detect_happiness function from emotion.py)
        if emotion.detect_happiness(user_message):
            bot_response = "I detected happiness! How can I help?"
        else:
            bot_response = "I didn't detect any happiness. How can I assist you?"
        
        return jsonify({"response": bot_response})
    
    # Handling GET requests 
