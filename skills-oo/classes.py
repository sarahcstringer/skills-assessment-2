class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initialize object with first name, last name, address"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):

    def __init__(self, question, correct_answer):
        """Initialize object with question and correct answer"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Print a question to the console and evaluate correctness. 

        Prompt user for answer and return True or False depending on whether 
        correct answer matches user answer."""

        print self.question
        user_answer = raw_input("> ")

        # Evaluate answer, provide feedback and return True or False depending
        # on correctness
        if user_answer == self.correct_answer:
            print "Correct."
            print
            return True
        else:
            print "Incorrect. Correct answer: {}".format(self.correct_answer)
            print
            return False


class Exam(object):

    def __init__(self, exam_name):
        """Initialize object with exam name and list of questions"""

        self.name = exam_name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Create a question and add to list of questions."""

        question = Question(question, correct_answer)

        # add question to the list of qusetions on the exam
        self.questions.append([question.question, 
                                question.correct_answer])

    def administer(self):
        """Administer all questions and return user's score."""
        
        # create a dictionary that will count True and False answers
        score = {True: 0, False: 0}

        # iterate through each question in the list of questions
        # keep track of user's score. The question and answer are stored as
        # a list, so convert back into Question class first to use
        # ask_and_evaluate

        # for test questions in order:

        # for i in range(len(self.questions)):
        #     question = Question(self.questions[i][0], self.questions[i][1])
        #     score_question = question.ask_and_evaluate()
        #     score[score_question] = score.get(score_question, 0) + 1


        # for random order test questions:
        list_of_questions = self.questions

        from random import choice
        
        for i in range(len(list_of_questions)):
            # choose a question randomly:
            question_choice = choice(list_of_questions)
            # delete that from the list of questions so it's not chosen again
            list_of_questions.remove(question_choice)
            # create a Question object from the question and answer
            question = Question(question_choice[0], question_choice[1])
            # ask and evaluate the question
            score_question = question.ask_and_evaluate()
            # record the score
            score[score_question] = score.get(score_question, 0) + 1


        # print the total number of correct and incorrect responses
        print "Total correct: {}. Total incorrect: {}".format(score[True], 
                                                    score[False])

        # return the number of incorrect and correct responses as a dictionary
        return score

class Quiz(Exam):

    def administer(self):
        """Administer quiz and return only True if passed, False if failed"""

        # set the score equal to the number of correct and incorrect responses
        # use the parent method for administering the questions
        score = super(Quiz, self).administer()

        # determine whether user passed or failed (over or under 50% correct)
        # return True if passed, False if failed
        if (float(score[True]) / (score[True] + score[False])) >= .5:
            return True
        else:
            return False


### functions below
def take_test(exam, student):
    """Administer test and assigns score to student."""

    student.score = exam.administer()
    return student.score


def example():
    """Create an example Exam"""

    exam = Exam('Exam Example')
    
    exam.add_question('What is the capital of California?', 'Sacramento')
    exam.add_question('What is the capital of Ohio?', 'Columbus')
    exam.add_question('What is the capital of Hawaii?', 'Honolulu')
    exam.add_question('What is the capital of New Mexico?', 'Santa Fe')

    student = Student('Sarah', 'Stringer', '7 Casa Way')

    score = take_test(exam, student)

    return score

print example()

