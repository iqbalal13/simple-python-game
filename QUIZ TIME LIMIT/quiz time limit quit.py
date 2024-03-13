import random
import time

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)  # Evaluate the expression to get the correct answer
    return question, answer

def math_quiz(time_limit, num_questions):
    score = 0
    start_time = time.time()

    for question_index in range(num_questions):
        question, correct_answer = generate_question()
        print(f"\nQuestion: {question}")

        user_input = input("Your answer (type 'skip' to skip, 'quit' to quit): ")

        if user_input.lower() == 'quit':
            print("\nQuiz terminated. Your current score:", score)
            return
        elif user_input.lower() == 'skip':
            print("Question skipped. No points deducted.\n")
            continue
        elif user_input.isdigit():
            user_answer = int(user_input)

            if user_answer == correct_answer:
                print("Correct! You get +1 point.\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}. You get -1 point.\n")
                score -= 1
        else:
            print("Invalid input. Please enter a number, 'skip', or 'quit'.\n")
            continue

        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            print(f"\nTime's up! Quiz completed.")
            break

    print(f"\nYour final score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz_time_limit = 30  # Set the time limit for the quiz in seconds
    number_of_questions = 10  # Set the number of questions in the quiz

    print(f"Welcome to the Math Quiz! You have {quiz_time_limit} seconds.")
    input("Press Enter to start the quiz.")

    math_quiz(quiz_time_limit, number_of_questions)