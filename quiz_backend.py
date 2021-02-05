import random
import html
from question_model import Q
class Backend:
    def __init__(self, questions: Q):
        self.question_num = 0
        self.score = 0
        self.questions = questions
        self.question_count = 0
        self.correct_Answer = ""
        self.choices = {}

    def game_On(self):
        return len(self.questions) != self.question_count

    def next_Question(self):
        curr_Q = self.questions[self.question_num]
        curr_Q_text = html.unescape(curr_Q.question)
        self.question_count += 1
        self.correct_Answer = curr_Q.correct_Answer
        incorrect_Answers = curr_Q.incorrect_Answers
        all_Answers = [None, None, None, None]
        answer_Arrangement = random.sample([0, 1, 2, 3], 4)
        for i in range(len(answer_Arrangement)-1):
            all_Answers[answer_Arrangement[i]] = incorrect_Answers[i]
        last_Index = all_Answers.index(None)
        all_Answers[last_Index] = self.correct_Answer
        self.choices = {
            "a" : all_Answers[0],
            "b" : all_Answers[1],
            "c" : all_Answers[2],
            "d" : all_Answers[3]
        }
        self.question_num += 1
        return f"{curr_Q_text}  \n a: {all_Answers[0]} \n b: {all_Answers[1]} \n c: {all_Answers[2]} \n d: {all_Answers[3]}"


    def checkAnswer(self, answer, correct_answer, choices):
        if choices[answer] == correct_answer:
            self.score += 1
            print(self.score)
            return True
        else:
            return False


