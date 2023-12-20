# Варіант №12
# 
#   Напишіть функцію для сортування рядка слів, розділених пропусками, за довжиною слів в порядку зменшення.
#   Вхідні дані:
#   Ruby Python Go JavaScript Java
#   Вихідні дані:
#   JavaScript Python Java Ruby Go
# 
# Дзюба Владислав

def sort_words(names):
    names_list = names.split()
    sorted_names_list = sorted(names_list, key=len, reverse=True)
    sorted_names = " ".join(sorted_names_list)
    return sorted_names


names = input("Введіть слова через пробіл: ")
print(sort_words(names))
