def quiz_app():
    questions = {
        "What is the capital of France?": "paris",
        "What is 5 + 7?": "12",
        "What is the color of the sky on a clear day?": "blue",
        "Who wrote 'Hamlet'?": "shakespeare",
        "What is the square root of 64?": "8"
    }

    score = 0

    print("Welcome to the Quiz App!")
    for question, answer in questions.items():
        user_answer = input(f"{question} ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{answer}'.")

    print(f"\nYour total score: {score}/{len(questions)}")

quiz_app()
