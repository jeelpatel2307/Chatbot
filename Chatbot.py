import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I am doing well.']),
    (r'what is your name', ['I am a Chatbot. You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*)', ['I am not sure I understand.', 'Can you please elaborate?', 'I am a simple chatbot.']),
]

# Create a chatbot using patterns and reflections
chatbot = Chat(patterns, reflections)

def chat_with_user():
    print("Welcome to the Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Download NLTK data (if not already downloaded)
    nltk.download('punkt')

    # Run the chat with the user
    chat_with_user()
