def get_quiz_answer():
    while True:
        try:
            answer = input("Enter your answer (A, B, C, or D):").strip().casefold()
            if answer in ["a", "b", "c", "d"]:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        except KeyboardInterrupt:
            print("\nQuiz interrupted.")
            return None
def main():
    score = 0
    question_key = {
        "What is the capital of France?": "a",
        "Which planet is known as the Red Planet?": "b",
        "What is the largest mammal?": "c",
        "Who wrote 'To Kill a Mockingbird'?": "d",
        "Which country has won the most FIFA World Cup titles?": "a"
    }
    question_options = {
        "What is the capital of France?": "a) Paris\nb) London\nc) Rome\nd) Berlin",
        "Which planet is known as the Red Planet?": "a) Earth\nb) Mars\nc) Jupiter\nd) Venus",
        "What is the largest mammal?": "a) Elephant\nb) Giraffe\nc) Blue Whale\nd) Hippopotamus",
        "Who wrote 'To Kill a Mockingbird'?": "a) Mark Twain\nb) J.K. Rowling\nc) Ernest Hemingway\nd) Harper Lee",
        "Which country has won the most FIFA World Cup titles?": "a) Brazil\nb) Germany\nc) Italy\nd) Argentina"
    }
    for question, correct_answer in question_key.items():
        print(question)
        print(question_options[question])
        user_answer = get_quiz_answer()
        if user_answer is None:
            break
        elif user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"Quiz completed! Your score is {score}/{len(question_key)}.")
    if score == len(question_key):
        print("Excellent! You got a perfect score!")
if __name__ == "__main__":
    main()