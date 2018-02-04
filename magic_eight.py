while True:

    response = input("What is your question?: ")

    if "?" in response:
        print(random.choice(validresponses))
    elif response == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
