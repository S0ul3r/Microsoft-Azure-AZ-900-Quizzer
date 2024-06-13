import random

def ask_question(question, question_no, total_questions, correct_count, incorrect_count):
    single_multiple_choice = "[single choice]" if len(question["correct_answers"]) == 1 else "[multiple choice]"
    summary = f"[{correct_count} OK, {incorrect_count} BAD]"

    print("")
    print(f"{question_no}/{total_questions}", summary, single_multiple_choice, question["question"], "[q to exit]")
    for i, answer in enumerate(question["answers"], start=1):
        print(f"{i}. {answer}")

    user_answer = input("Answer: ")
    return user_answer

def validate_answer(user_answer, question):
    user_answers_num = user_answer.split(",")
    user_answers_num = [x.strip() for x in user_answers_num if x.strip().isdigit()]
    if not user_answers_num:
        return None, "Invalid input! Please enter the numbers corresponding to the answers. (Example: 1,3,5)"

    user_answers_num = [int(x) - 1 for x in user_answers_num]
    user_answers = []
    for num in user_answers_num:
        if 0 <= num < len(question["answers"]):
            user_answers.append(question["answers"][num])
        else:
            return None, "Invalid input! Please enter the numbers corresponding to the answers. (Example: 1,3,5)"

    return user_answers, None

def select_question(questions, randomize, questions_answered, question_no, total_questions):
    if randomize:
        not_answered_questions = [q for q in questions if q not in questions_answered]
        if not not_answered_questions:
            return None
        return random.choice(not_answered_questions)
    else:
        if question_no > total_questions:
            return None
        return questions[question_no - 1]
