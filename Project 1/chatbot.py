# ==========================================================
# Project 1: Rule-Based AI Chatbot
# Internship: Decode Labs
# Track: Artificial Intelligence
# Author: Moeez Ur Rahman
# ==========================================================

import string
import difflib
import datetime

# ==========================================================
# KNOWLEDGE BASE
# ==========================================================

responses = {

    # Greetings
    "hello": "Hello.",
    "hi": "Hello.",
    "hey": "Hello.",
    "good morning": "Good morning. Have a wonderful day.",
    "good afternoon": "Good afternoon.",
    "good evening": "Good evening.",

    # General Questions
    "how are you": "I am doing well. Thank you for asking.",
    "who are you": "I am Decode Assistant, a rule-based AI chatbot built using Python.",
    "your name": "My name is Decode Assistant.",
    "who made you": "I was created using Python as part of an Artificial Intelligence internship.",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that usually require human intelligence.",
    "python": "Python is one of the most widely used programming languages for Artificial Intelligence.",

    # Help
    "help":
        "Available commands:\n"
        "- hello / hi / hey\n"
        "- good morning / afternoon / evening\n"
        "- who are you\n"
        "- your name\n"
        "- what is ai\n"
        "- python\n"
        "- what can you do\n"
        "- my name is <your name>\n"
        "- what is my name\n"
        "- happy / sad\n"
        "- time\n"
        "- date\n"
        "- thanks\n"
        "- bye / exit / quit",

    "what can you do":
        "I can greet you, answer basic questions, remember your name, respond to simple moods, provide the current time and date, and chat using rule-based logic.",

    # Gratitude
    "thanks": "You are welcome.",
    "thank you": "You are welcome."

}

# ==========================================================
# EXIT COMMANDS
# ==========================================================

exit_commands = {"bye", "exit", "quit"}

# ==========================================================
# USER MEMORY
# ==========================================================

user_name = None

# ==========================================================
# FUNCTIONS
# ==========================================================

def sanitise(text):
    """Clean the user's input."""

    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))

    return text


def get_time():
    """Return the current time."""

    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."


def get_date():
    """Return today's date."""

    today = datetime.date.today()
    return f"Today's date is {today.strftime('%d %B %Y')}."


def closest_match(user, threshold=0.75):
    """Return the closest matching command."""

    matches = difflib.get_close_matches(
        user,
        responses.keys(),
        n=1,
        cutoff=threshold
    )

    if matches:
        return matches[0]

    return None


def get_response(user):
    """Generate a response."""

    global user_name

    # Exit
    if user in exit_commands:
        return "Goodbye."

    # Time
    elif user == "time":
        return get_time()

    # Date
    elif user == "date":
        return get_date()

    # Remember user's name
    elif "my name is" in user:

        name = user.replace("my name is", "").strip().title()

        if name:
            user_name = name
            return f"Nice to meet you, {user_name}."

        return "I did not catch your name."

    # Recall user's name
    elif "what is my name" in user:

        if user_name:
            return f"Your name is {user_name}."

        return "You have not told me your name yet."

    # Mood detection
    elif any(word in user for word in ["happy", "good", "fine", "great", "awesome"]):
        return "I am pleased to hear that."

    elif any(word in user for word in ["sad", "upset", "not good"]):
        return "I am sorry to hear that. I hope things improve soon."

    # Exact match
    elif user in responses:
        return responses[user]

    # Partial match
    else:

        for key in responses:

            if key in user:
                return responses[key]

    # Typo suggestion
    suggestion = closest_match(user)

    if suggestion:
        return (
            f"I am not sure I understood that. "
            f"Did you mean '{suggestion}'?\n"
            f"{responses[suggestion]}"
        )

    # Default
    return "I apologise, I do not understand that. Type 'help' to view the available commands."


# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("=" * 55)
print("Welcome to Decode Assistant")
print("Rule-Based AI Chatbot")
print("Type 'help' to view the available commands.")
print("Type 'bye' to exit.")
print("=" * 55)

while True:

    user = sanitise(input("\nYou: "))

    if not user:
        print("Bot: Please enter something.")
        continue

    response = get_response(user)

    print(f"Bot: {response}")

    if user in exit_commands:
        break