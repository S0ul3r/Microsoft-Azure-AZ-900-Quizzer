import os

def get_default_readme_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions", "README.md")

def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.readlines()

    questions = []
    i = 0
    while i < len(content):
        if content[i].startswith("###"):
            question_text = content[i][4:-1]
            i += 2
            answers = []
            correct_answers = []

            while i < len(content) and content[i].startswith("- "):
                answer = content[i]
                answers.append(answer)
                if answer.startswith("- [x]"):
                    correct_answers.append(answer)
                i += 1

            answers = [x[5:-1] for x in answers]
            correct_answers = [x[5:-1] for x in correct_answers]
            questions.append({"question": question_text, "answers": answers, "correct_answers": correct_answers})
        else:
            i += 1
    return questions
