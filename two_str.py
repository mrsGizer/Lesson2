def comparison_str(one_str, two_str):
    if type(one_str) != str or type(two_str) != str:
        print(0)
    elif one_str == two_str:
        print('1')
    elif one_str != two_str and len(one_str) > len(two_str):
        print('2')
    elif one_str != two_str and two_str == 'learn':
        print('3')     

comparison_str(1, 2)
comparison_str(2, 'ghbdtn')
comparison_str('learn', 'learn')
comparison_str('мама', 'папа')
comparison_str('крокодил', 'я')
comparison_str('я', 'тиранозавр')
comparison_str('мама', 'learn')