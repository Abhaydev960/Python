import random

subjects = ["The student", "A clever robot", "My friend", "The teacher"]
verbs = ["writes", " studies", " builds", "explores"]
objects = ["a Python program", "a useful application", "new ideas", "the computer lab"]

count = int(input("How many sentences should be generated? "))

if count <= 0:
    print("Enter a number greater than zero.")
else:
    print("\nGenerated sentences:")
    for i in range(count):
        sentence = (random.choice(subjects) + " " +
                    random.choice(verbs).strip() + " " +
                    random.choice(objects) + ".")
        print(f"{i + 1}. {sentence}")
