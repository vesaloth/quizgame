print("Welcome to my Quiz")

playing = input("Would you like to play (y/n): ")
if playing != "y":
    quit()

print("Starting Quiz")
score = 0

answer = input("What language do you use for Web Development? ")
if answer == "html":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is considered the best computer language to learn as a beginner? ")
if answer == "python":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is the best networking encryption? ")
if answer == "wpa2-aes":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Do you need a Bachelor's Degree to get into Cybersecurity? (y/n) ")
if answer == "n":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("When you impliment a sidebar to effectively make it responsive what language would you need to use? ")
if answer == "javascript":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Can taskmanager disable startup items? (y/n) ")
if answer == "y":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What do you write in the search menu to open up command prompt? ")
if answer == "cmd":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

print("You got " + str(score) + " questions correct.")
print("You got " + str((score / 7) * 100) +  "%. ")


