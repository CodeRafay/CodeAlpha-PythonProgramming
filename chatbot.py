# This is a simple chatbot implementation in Python.
# def chatbot():
#     print("Chatbot: Hi! Type 'bye' to exit.")
#     while True:
#         user_input = input("You: ").strip().lower()

#         if user_input == "hello":
#             print("Chatbot: Hi!")
#         elif user_input == "how are you":
#             print("Chatbot: I'm fine, thanks!")
#         elif user_input == "bye":
#             print("Chatbot: Goodbye!")
#             break
#         else:
#             print("Chatbot: Sorry, I didn't understand that.")


# if __name__ == "__main__":
#     chatbot()

# This is a simple GUI chatbot application using Tkinter.
# It allows users to interact with a rule-based chatbot through a graphical interface.
'''
import tkinter as tk

# Rule-based reply function


def get_reply(user_text):
    user_text = user_text.lower()
    if user_text == "hello":
        return "Hi!"
    elif user_text == "how are you":
        return "I'm fine, thanks!"
    elif user_text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

# Function to handle send button click


def send_message():
    user_msg = user_entry.get().strip()
    if not user_msg:
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_msg + "\n")
    reply = get_reply(user_msg)
    chat_log.insert(tk.END, "Chatbot: " + reply + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    user_entry.delete(0, tk.END)
    if user_msg.lower() == "bye":
        root.after(1000, root.destroy)


# Setup Tkinter window
root = tk.Tk()
root.title("Simple Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=15, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

# Bind Enter key to send message
root.bind('<Return>', lambda event: send_message())

root.mainloop()
'''
# Using improved Tkinter chatbot that uses keyword-based flexible replies for more natural conversation — no strict predefined inputs needed:
'''
import tkinter as tk

def get_reply(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "hi" in user_text:
        return "Hi there! How can I help you?"
    elif "how are you" in user_text or "how's it going" in user_text:
        return "I'm doing well, thanks! How about you?"
    elif "bye" in user_text or "goodbye" in user_text:
        return "Goodbye! Have a great day!"
    elif "help" in user_text:
        return "Sure, what do you need help with?"
    else:
        return "That's interesting! Tell me more."


def send_message():
    user_msg = user_entry.get().strip()
    if not user_msg:
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_msg + "\n")
    reply = get_reply(user_msg)
    chat_log.insert(tk.END, "Chatbot: " + reply + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    user_entry.delete(0, tk.END)
    if "bye" in user_msg.lower():
        root.after(1500, root.destroy)


root = tk.Tk()
root.title("Flexible Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=15, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

root.bind('<Return>', lambda event: send_message())

root.mainloop()
'''

# This code implements a simple chatbot using NLTK for natural language processing.
# It uses keyword-based intent recognition to provide flexible replies.
# The chatbot can handle greetings, farewells, and help requests, making it more interactive.
'''
import nltk
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


import tkinter as tk
from nltk.tokenize import word_tokenize

# Simple lists of keywords for intents
greetings = {"hello", "hi", "hey", "greetings"}
farewells = {"bye", "goodbye", "see you", "farewell"}
help_words = {"help", "support", "assist", "issue", "problem"}


def get_intent(words):
    if any(word in greetings for word in words):
        return "greeting"
    elif any(word in farewells for word in words):
        return "farewell"
    elif any(word in help_words for word in words):
        return "help"
    else:
        return "unknown"


def get_reply(user_text):
    words = set(word_tokenize(user_text.lower()))
    intent = get_intent(words)

    if intent == "greeting":
        return "Hello! How can I assist you today?"
    elif intent == "farewell":
        return "Goodbye! Have a wonderful day!"
    elif intent == "help":
        return "I’m here to help. Please tell me your issue."
    else:
        return "Interesting! Could you tell me more?"


def send_message():
    user_msg = user_entry.get().strip()
    if not user_msg:
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_msg + "\n")
    reply = get_reply(user_msg)
    chat_log.insert(tk.END, "Chatbot: " + reply + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    user_entry.delete(0, tk.END)
    if get_intent(set(word_tokenize(user_msg.lower()))) == "farewell":
        root.after(1500, root.destroy)


root = tk.Tk()
root.title("NLP-Enhanced Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=15, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

root.bind('<Return>', lambda event: send_message())

root.mainloop()
'''
