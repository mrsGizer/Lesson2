num_one = input('Введите первое целое число: ')
num_two = input('Введите второе целое число: ')

def get_sum(one, two):
    try:
        one = int(num_one)
        two = int(num_two)
        print(one + two)
    except ValueError:
        print ('Вы ввели не целое число.')
    
get_sum(num_one, num_two)