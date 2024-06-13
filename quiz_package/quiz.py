import random
from utils import ask_question, validate_answer, select_question

def quiz(questions, randomize):
    correct_count = 0
    incorrect_answers = []

    questions_answered = []
    question_no = 1
    total_questions = len(questions)

    while True:
        question = select_question(questions, randomize, questions_answered, question_no, total_questions)

        if not question:
            break

        user_answer = ask_question(question, question_no, total_questions, correct_count, question_no - correct_count - 1)
        if user_answer == "q":
            break

        user_answers, error_message = validate_answer(user_answer, question)
        if error_message:
            print(error_message)
            continue

        if set(user_answers) == set(question["correct_answers"]):
            print("Correct")
            correct_count += 1
        else:
            print("Wrong! Proper answer(s): " + ", ".join(question["correct_answers"]))
            incorrect_answers.append(question_no)

        questions_answered.append(question)
        question_no += 1

    return correct_count, incorrect_answers
