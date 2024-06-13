import sys
import os
from quiz_package.questions import get_default_readme_path, load_questions
from quiz_package.quiz import quiz

def main():
    print("Welcome to AZ900 quizzer!")
    print("To answer multiple choice questions, enter answers separated with a comma, example:")
    print("> 1,3,5\n")

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = get_default_readme_path()

    if not os.path.exists(path):
        path = input("Please provide the path to the README.md file: ").strip()

    randomize = input("Should I randomize questions order (y/n)? ").strip().lower() == 'y'

    questions = load_questions(path)

    correct_count, incorrect_answers = quiz(questions, randomize)
    total_questions = len(questions)

    print(f"{total_questions} questions answered, {correct_count} answers correct, {total_questions - correct_count} answers wrong")
    if incorrect_answers:
        print(f"Your score: {correct_count}/{total_questions} ({correct_count/total_questions*100:.2f}%)")
        print("Questions you answered wrong: " + ", ".join(map(str, incorrect_answers)))

        while incorrect_answers:
            retry = input("Do you want to answer again the questions that you have answered wrong (y/n)? ").strip().lower()
            if retry != 'y':
                break

            questions_to_retry = [questions[i - 1] for i in incorrect_answers]
            correct_count, incorrect_answers = quiz(questions_to_retry, randomize)

            print(f"{total_questions} questions answered, {correct_count} answers correct, {total_questions - correct_count} answers wrong")
            if incorrect_answers:
                print("Questions you answered wrong: " + ", ".join(map(str, incorrect_answers)))

    print("Quiz finished.")

if __name__ == "__main__":
    main()
