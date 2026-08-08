# Rule-Based AI Chatbot

## Overview

This project is a simple **Rule-Based AI Chatbot** developed in Python as part of the **Decode Labs Artificial Intelligence Internship – Project 1**.

The chatbot uses predefined rules and conditional statements to respond to user input. It demonstrates core Python programming concepts without using machine learning or external libraries.

---

## Features

* Greets users with predefined responses
* Answers basic Artificial Intelligence-related questions
* Remembers the user's name during the conversation
* Responds to simple positive and negative moods
* Displays the current time and date
* Suggests the closest matching command for minor typing mistakes
* Provides a help menu with available commands
* Supports multiple exit commands (`bye`, `exit`, `quit`)

---

## Technologies Used

* Python 3
* Python Standard Library

  * `string`
  * `datetime`
  * `difflib`

---

## Project Structure

```text
Project-1-Rule-Based-Chatbot/
├── chatbot.py
├── README.md
└── requirements.txt
```

---

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project files.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python chatbot.py
```

---

## Example Interaction

```text
=======================================================
Welcome to Decode Assistant
Rule-Based AI Chatbot
Type 'help' to view the available commands.
Type 'bye' to exit.
=======================================================

You: hello
Bot: Hello.

You: my name is Alice
Bot: Nice to meet you, Alice.

You: what is my name
Bot: Your name is Alice.

You: time
Bot: The current time is 14:36:42.

You: bye
Bot: Goodbye.
```

---

## Concepts Demonstrated

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`)
* Functions
* Dictionaries
* Sets
* String Manipulation
* Input Sanitisation
* Basic Rule-Based Artificial Intelligence

---

## Future Improvements

Potential enhancements include:

* Additional conversation topics
* More intelligent pattern matching
* Persistent memory using files or a database
* Graphical User Interface (GUI)
* Integration with Natural Language Processing techniques

---

## Author

**Moeez Ur Rahman**

Decode Labs Artificial Intelligence Internship
