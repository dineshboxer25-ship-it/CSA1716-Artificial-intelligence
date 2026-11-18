# Simple Chatbot using NLP

import random

responses = {
    "hello": ["Hello! How can I help you?", "Hi! Welcome!"],
    "how are you": ["I am fine. How are you?", "I am doing great!"],
    "name": ["I am a simple AI chatbot."],
    "college": ["Welcome to the world of technology!"],
    "bye": ["Goodbye! Have a nice day!"]
}

print("AI Chatbot Started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user_input:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand that.")
