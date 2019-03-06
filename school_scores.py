school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [4,5,3,4,5,5,4]},
    {'school_class': '5a', 'scores': [5,4,4,3,4,5]},
    {'school_class': '6a', 'scores': [4,5,5,5,5,5,5]}
]

def average_class(one_class):
    summ_scores = sum(element['scores'])
    count_scores = len(element['scores'])
    result = summ_scores/count_scores
    print('Средний балл по классу ', element['school_class'], result)
    return result

classes_average =[]

for element in school_scores:
    classes_average.append(average_class(element))
print(sum(classes_average)/len(classes_average))
