print("***********************")
print("Welcome to my quiz game!!")

question_bank=[
    {"text": "List some popular application of python in the world of technology?", "answer": "D"},
    {"text": "Who developed python programing language?", "answer": "C"},
    {"text": "Which of the following is the correct extension of the python file?", "answer": "C"},
    {"text": "Is python case sensitive when dealing with identifiers?", "answer": "B"},
    {"text": "Is python code compiled interpreted?", "answer": "A"},
]

options = [["A. System Scription", "B. Web development", "C. Software development", "D. All of the mentioned"],
          ["A. Wick van rossum", "B.Rasmus lerdorf", "C. Guido var rossum", "D. Niene stom"],
          ["A. .Python", "B. .p", "C. .py", "D. .pl"],
           ["A. NO", "B. Yes", "C. Machine dependent", "D. NOne of the mentioned"],
           ["A. Python code is both compiled and interpreted ", "B. python code is neither compiled and interpreted",
            "C. python code is only compiled", "D. python code is only interpreted"],
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("*********************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer(A/B/CD/): ").upper()
    is_correct= check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("correct answer")
        score += 1
    else:
        print("Incorrect answer")
        print(f"tTHe correct answer is {question_bank[question_num]['answer']} ")
    print(f"your correct score is {score}/{question_num*1}")
print(f"You have given score {score} correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")