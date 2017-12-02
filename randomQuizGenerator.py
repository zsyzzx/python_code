#! python3
# 创建35份有50道题的试卷，每份试卷不一样且都有一份参考答案
import random, os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# capitalsItems = list(capitals.items())

os.makedirs("CapitalQuiz",exist_ok=True)
dirPath = "CapitalQuiz"

for quizNum in range(35):
    # 创建文件名称
    quizFileName = 'capitalsquiz%s.txt' % (quizNum + 1)
    answerFileName = 'capitalsquiz_answer%s.txt' % (quizNum + 1)
    quizFile = open(os.path.join(dirPath, quizFileName), 'w')
    answerFile = open(os.path.join(dirPath, answerFileName), 'w')

    # 试卷头: 名称等，第几份试卷等信息
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # 随机题目
    states = list(capitals.keys())
    random.shuffle(states)
    # print(states)

    #     创建50份题目与答案选项
    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # 将题目与答案写进文件
        quizFile.write('%s, What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s.%s\n'%('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()

