#! python3
# random_quiz_generator.py - creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import string


# Quiz data {states: capitals}
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   "New Mexico": 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   "West Virginia": 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

filename_base = "quiz_geo_8th_1"
header = "Quiz 1 Geography, 8th grade"
date = "January 18th, 2016"
#todo: create folder

# generate 35 quiz files:

for quiz_num in range(35):
    #todo: create quiz and answer key
    with open("{}_{}.txt".format(filename_base, quiz_num), 'w') as f:
        with open("{}_{}_ankey.txt".format(filename_base, quiz_num), 'w') as a:

            #todo: write out header for the quiz
            f.write("{}, quiz number {}\nName:\nDate:\n\n".format(header, quiz_num))
            a.write("{}, Answer Key {}\n\n".format(header, quiz_num))

            #todo: shuffle the order of the states
            key_order = list(capitals.keys())
            random.shuffle(key_order)

            main_question = "\nWrite down the capital cities of the following states"
            f.write(main_question)
            a.write(main_question)

            q_number = 1
            #todo: loop through all 50 states, making a question for each
            for key in key_order:

                correct_answer = capitals[key]
                wrong_answers_pool = list(capitals.values())
                del wrong_answers_pool[wrong_answers_pool.index(correct_answer)]
                wrong_answers = random.sample(wrong_answers_pool, 3)
                answer_options = wrong_answers + [correct_answer]
                random.shuffle(answer_options)

                # write questions
                q_line = "\n{}. {}: ".format(q_number, key)
                f.write(q_line)
                a.write(q_line)

                # write answers
                alpha = string.ascii_uppercase
                for i in range(4):
                    f.write("\n\t{}. {}".format(alpha[i], answer_options[i]))

                correct_letter = alpha[answer_options.index(correct_answer)]
                a.write("{}. {}".format(correct_letter, correct_answer))

                q_number+=1

"""

# generate 35 quiz files:
for quiz_num in range(35):
    #todo: create quiz and answer key

    #todo: write out header for the quiz

    #todo: shuffle the order of the states

    #todo: loop through all 50 states, making a question for each
"""