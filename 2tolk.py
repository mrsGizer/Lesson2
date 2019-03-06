import sys

def my_except_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print('Пока!')
    else:
        sys.__excepthook__(exctype, value, traceback)
sys.excepthook = my_except_hook

def how_are_you():
    answer = input('Как твои дела? ')
    if answer == 'Хорошо':
        print('И у меня отлично!')
        return False
    else:
        return True

answer = True        
while answer == True:
    answer = how_are_you()

chat = {'Как дела?': 'Замечательно', 
'Что делаешь?': 'Программирую', 
'На каком языке ты программируешь?': 'На Python, конечно))', 
'У тебя получается?': 'Я еще учусь'}

def questions():
    chat_question = input('Давай поболтаем, спроси меня о чем нибудь! ')
    if chat_question in chat:
        print(chat[chat_question])
    else:
        new_question = input('Я не знаю такого вопроса.\nЯ его записала. А как мне на него отвечать? ')
        chat[chat_question] = new_question

while True:
    questions()
 



    
    

        