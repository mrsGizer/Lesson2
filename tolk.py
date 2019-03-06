user_answer = input('Как твои дела? ')
def ask_user(answer):
    while True:
        answer = input('Как твои дела? ')
        if answer == 'Хорошо':
            print('И у меня отлично!')
            break
        
ask_user(user_answer)