def detect_happiness(message):
    """
    Detects happiness in a message based on specific keywords.

    Args:
        message (str): The input message to analyze.

    Returns:
        bool: True if the message contains happy keywords, False otherwise.
    """
    happy_keywords = [
        "happy", "joy", "excited", "glad", "pleased", 
        "delighted", "cheerful", "thrilled", "ecstatic"
    ]
    return any(word in message.lower() for word in happy_keywords)

# Optional: Test the function locally
def test():
    test_messages = [
        "I am so happy today!", 
        "This is such a joyful moment.", 
        "I'm feeling sad and down.",
        "Absolutely ecstatic about the news!",
        "Just a normal day, nothing special."
    ]
    for message in test_messages:
        print(f"Message: '{message}' => Happiness Detected: {detect_happiness(message)}")

if __name__ == "__main__":
    test()
