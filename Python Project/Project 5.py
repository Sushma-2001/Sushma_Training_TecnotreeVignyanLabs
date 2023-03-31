questions = [
    {
        "question": " What is the national heritage animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Cheethah"],
        "answer": "Elephant"
    },
    {
        "question": "Which of the following states is not located in the North?",
        "options": ["Jharkhand", "Jammu and Kashmir", "Himachal Pradesh", "Haryana"],
        "answer": "Jharkhand"
    },
    {
        "question": "The Gol Gumbaz is located in the city?",
        "options": ["Bijapur", "Belagavi", "Mysore", "Tumkur"],
        "answer": "Bijapur"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    return question["options"][int(answer)-1] == question["answer"]

def play_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}")
    print(f"Your final score is {score}/{len(questions)}")

play_quiz()
