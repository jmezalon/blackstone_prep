from Question import Question


questions_prompts = [
    "What is 2 to the 3rd power?\n(a) 4 \n(b) 8 \n(c) 16 \n(d) 2\nAnswer: ",
    "What is the square root of 64?\n(a) 8 \n(b) 9 \n(c) 32 \n(d) 0\nAnswer: "
]

questions = [
    Question(questions_prompts[0], 'b'),
    Question(questions_prompts[1], 'a')
]

def make_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    
    result = "You got " + str(score) + "/" + str(len(questions)) + " correct!"

    print(result)


make_test(questions)