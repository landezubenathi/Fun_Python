def read_question_and_answers(questions_file, answers_file):
    questions = []
    answers = []
    with open(questions_file, 'r') as file:
        questions = file.read().splitlines()
    with open(answers_file, 'r') as file:
        answers = file.read().splitlines()
    return questions, answers

def get_chatbot_response(user_input, questions, answers):
    if user_input in questions:
        index = questions.index(user_input)
        return answers[index]
    else:
        return "Sorry I don't understand."
    
questions_file = "questions_file.txt"
answers_file = "answers_file.txt"
questions, answers = read_question_and_answers(questions_file, answers_file)

user_input = "What is the date today"
response = get_chatbot_response(user_input, questions, answers)
print(response)