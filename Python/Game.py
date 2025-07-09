import random

# Define responses for the chatbot
responses = {
    "hello": "Hello! Let's play the Over/Under 7 dice game. Make a prediction: 'over 7', 'exactly 7', or 'under 7'.",
    "bye": "Goodbye! If you want to play again, just say 'hello'.",
    "default": "Let's play the Over/Under 7 dice game. Make a prediction: 'over 7', 'exactly 7', or 'under 7.'",
}

# Function to get a response from the chatbot
def get_response(message):
    message = message.lower()
    response = responses.get(message, responses["default"])
    return response

def roll_dice():
    return random.randint(1, 6)

def play_game(prediction):
    user_roll = roll_dice()
    computer_roll = roll_dice()
    total = user_roll + computer_roll

    if (prediction == "over 7" and total > 7) or (prediction == "exactly 7" and total == 7) or (prediction == "under 7" and total < 7):
        return f"You rolled {user_roll}. Computer rolled {computer_roll}. Total: {total}. You win!"
    else:
        return f"You rolled {user_roll}. Computer rolled {computer_roll}. Total: {total}. Computer wins."

# Chatbot and game interaction
print("Chatbot: Hello! Let's play the Over/Under 7 dice game. Type 'hello' to start.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break

    chatbot_response = get_response(user_input)
    print(f"Chatbot: {chatbot_response}")

    if "prediction:" in chatbot_response:
        prediction = user_input
        result = play_game(prediction)
        print(f"Chatbot: {result}")

    if user_input == "hello":
        print("Make a prediction: 'over 7', 'exactly 7', or 'under 7.'")
