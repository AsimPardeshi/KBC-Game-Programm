""""Create a program capable of displaying questions to the user like KBC.
 Use List data type to store the questions and their correct answers.
 Display the final amount the person is taking home after playing the game
"""

questions = [("What is the capital of India?", "New Delhi"),
             ("Who is the current PM of India?", "Narendra Modi"),
             ("What is the currency of Japan?", "Yen"),
             ("Who is the inventor of the telephone?", "Alexander Graham Bell"),
             ("What is the largest planet in our solar system?", "Jupiter")]

total_amount = 0

for questions, correct_answer in questions:
    user_answer = input(questions)
    if user_answer.lower() == correct_answer.lower():
        total_amount +=10000
    else:
        print("Incorrect Answer.")

print("You Won a total of Rs.", total_amount)