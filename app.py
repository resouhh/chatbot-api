from flask import Flask, request, jsonify
from flask_cors import CORS
import emotion  # Import your emotion detection script

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Emotion Detection (assuming detect_emotion function exists)
    detected_emotion = emotion.detect_emotion(user_message)  # Modify based on your emotion.py logic

    # Chatbot logic (modify as needed)
    bot_response = f"I detected {detected_emotion}. How can I help?"  # Replace with actual chatbot logic

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
