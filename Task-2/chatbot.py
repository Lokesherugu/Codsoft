import random
from datetime import datetime

# Define rules and responses
rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!", "All good, thanks!"],
    "bye": ["Goodbye!", "Bye!", "See you later!"],
    "thank you": ["You're welcome!", "No problem!", "My pleasure!"],
    "who are you": ["I'm a simple rule-based chatbot designed by LOKESH!", "I'm your friendly neighborhood chatbot designed by LOKESH!"],
    "what can you do": ["I can respond to basic questions and have simple conversations.", "I'm here to chat with you!"],
    "time": [f"The current time is {datetime.now().strftime('%H:%M')}."],
    "date": [f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure I follow."]
}

def get_response(user_input):
    for rule in rules:
        if rule in user_input:
            return random.choice(rules[rule])
    return random.choice(rules["default"])

def main():
    print("Chatbot: Hello! How can I help you today?")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
