print("ELIZA: Hello. Tell me what is on your mind.")
print("Type 'bye' to end the conversation.")

while True:
    user = input("You: ").strip()
    message = user.lower()

    if message == "bye":
        print("ELIZA: Goodbye. Take care!")
        break
    elif "i am" in message:
        print("ELIZA: How long have you felt that way?")
    elif "sad" in message:
        print("ELIZA: What do you think is making you feel sad?")
    elif "happy" in message:
        print("ELIZA: What has made you feel happy?")
    elif "because" in message:
        print("ELIZA: Is that the main reason?")
    else:
        print("ELIZA: Can you tell me more about that?")
