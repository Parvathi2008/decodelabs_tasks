print("=" * 50)
print("Smart Rule-Based Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Personal questions
    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is SmartBot.")

    elif user_input == "who created you":
        print("Bot: I was created by Parvathi as part of her AI internship.")

    # Date and time
    elif user_input == "time":
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    elif user_input == "date":
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    # Basic calculations
    elif user_input.startswith("add"):
        try:
            numbers = user_input.split()
            num1 = int(numbers[1])
            num2 = int(numbers[2])
            print(f"Bot: Sum = {num1 + num2}")
        except:
            print("Bot: Use format: add 5 10")

    elif user_input.startswith("multiply"):
        try:
            numbers = user_input.split()
            num1 = int(numbers[1])
            num2 = int(numbers[2])
            print(f"Bot: Product = {num1 * num2}")
        except:
            print("Bot: Use format: multiply 5 10")

    # Knowledge questions
    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "what can you do":
        print("Bot: I can chat, answer questions, tell date/time, and do simple calculations.")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
