from flask import Flask, request, jsonify
from emotion import detect_happiness  # Make sure this module is correctly implemented and accessible

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():
    print("Request received!")  # Debug log for request received
    try:
        # Get JSON data from the request
        data = request.get_json()
        print("Received data:", data)  # Debug log for received data

        # Validate the request data
        if not data or "message" not in data:
            print("Invalid request: No 'message' provided")
            return jsonify({"error": "No 'message' provided"}), 400

        # Extract the message
        message = data["message"]
        print("Message:", message)  # Debug log for the message content

        # Process the message with the emotion detection function
        is_happy = detect_happiness(message)
        response_text = (
            "I sense happiness in your message! 😃" if is_happy else "Cheer up! It'll get better!"
        )
        print("Response:", response_text)  # Debug log for the response content

        # Return the response
        return jsonify({"response": response_text})

    except Exception as e:
        print("Error occurred:", str(e))  # Debug log for any exception
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=False, host="0.0.0.0", port=port)

