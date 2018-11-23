import json
import templates as template


def __read_data(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def __load_json_data():
    path = 'data/java/'
    answer_path = path + 'answer/answers.min.json'
    question_path = path + "question/question.min.json"
    queue_path = path + 'queue.json'

    answer = __read_data(answer_path)
    question = __read_data(question_path)
    queue = __read_data(queue_path)
    return answer['answers'], question['questions'], queue['queue']


def load_data():
    answer, question, queue = __load_json_data()
    answer_list = []
    question_list = []
    length = len(answer)

    for index in range(length):
        answer_element = template.answer.Answer(answer[index]['number'], answer[index]['answer'])
        answer_list.append(answer_element)
        question_element = template.question.Question(question[index]['number'], question[index]['tag'],
                                                      question[index]['question'], question[index]['options'])
        question_list.append(question_element)
    return answer_list, question_list, queue
