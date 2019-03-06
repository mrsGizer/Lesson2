user_age = float(input('Введите Ваш возраст: '))
def what_to_do(age):
    if age < 6.5:
        result = ('Вам в детский сад.')
    elif 6.5 <= age < 18:
        result = ('Вы должны учиться в школе.')
    elif 18 <= age < 24:
        result = ('Вы должны учиться в ВУЗе.')
    else:
        result = ('Вы уже должны работать.')     
    print (result)

what_to_do(user_age)
