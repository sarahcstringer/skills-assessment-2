class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Print a question to the console and evaluate correctness. 

        Prompt user for answer and return True or False depending on whether 
        correct answer matches user answer."""

        print self.question
        user_answer = raw_input("> ")

        if user_answer == self.correct_answer:
            return True
        else:
            print "Incorrect. Correct answer: {}".format(self.correct_answer)
            return False


class Exam(object):

    def __init__(self, exam_name):
        self.name = exam_name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Create a question and add to list of questions."""

        question = Question(question, correct_answer)

        self.questions.append([question.question, 
                                question.correct_answer])

    def administer(self):
        """Administer all questions and return user's score."""
        
        score = {True: 0, False: 0}

        for i in range(len(self.questions)):
            question = Question(self.questions[i][0], self.questions[i][1])
            score_question = question.ask_and_evaluate()
            score[score_question] = score.get(score_question, 0) + 1

        total_correct = score[True]
        total_incorrect = score[False]
        total_num_questions = score[True] + score[False]

        print "Correct: {}. Incorrect: {}".format(total_correct, total_incorrect)