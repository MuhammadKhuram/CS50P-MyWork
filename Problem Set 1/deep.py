question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
question = question.lower()

if question.replace(" ", "") == "42" or question == "forty two" or question == "forty-two":
    print("Yes")
else:
    print("No")
