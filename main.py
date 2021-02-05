from question_model import Q
import quiz_backend as qbe
from data_questions import all_questions
from user_interface import UI

#functionality

question_storage = []
for q in range(len(all_questions["results"])):
    question_storage.append(Q(all_questions["results"][q]["question"], all_questions["results"][q]["correct_answer"], all_questions["results"][q]["incorrect_answers"]))

#QuestionBank
question_Bank = qbe.Backend(question_storage)

#tkinter
ui = UI(question_Bank)





