# Варіант №12
# 
#   Вам запропонували створити програму, яка допоможе у перевірці робіт
#   теоретичного іспиту з правил дорожнього руху. Іспит складається 
#   з 20 варіантів запитань, в кожному з яких відповідями є лише одне
#   значення із списку: A, B, C, D. Програма повинна прочитати відповіді
#   студента на кожне з 20 питань з текстового файлу (відповіді 
#   розташовуються на окремих рядках). Після того, як відповіді 
#   були прочитані з файлу, програма повинна відображати повідомлення про те,
#   чи студент пройшов іспит чи не пройшов його (необхідно правильно відповісти
#   на 15 з 20 питань, щоб скласти іспит). Після цього має відображатися загальна
#   кількість правильних відповідей на запитання, кількість неправильних відповідей
#   та список із зазначенням номерів запитань, на які відповідь була неправильною.
#   Вхідні дані:
#   input.txt
#   Вихідні дані:
#   You failed
#   Correctly answerd question is 7
#   Incorrectly answerd question is 13
#   Wrong answers 2 3 5 8 9 10 11 12 13 14 17 18 19
#   або
#   You passed
#   Correctly answerd question is 17
#   Incorrectly answerd question is 3
#   Wrong answers 7 13 19
# 
# Дзюба Владислав

with open("correct_answers.txt", "r") as file:
    data_from_c_a = file.readlines()

with open("stud_answers.txt", "r") as file:
    user_answers = file.readlines()

correct_score_counter = 0
wrong_score_counter = 0
wsc_list = []

for i in range(len(data_from_c_a)):
    if data_from_c_a[i].upper() == user_answers[i].upper():
        correct_score_counter += 1
    else:
        wrong_score_counter += 1
        wsc_list.append(i + 1)
if correct_score_counter >= 15:
    print("You passed")
else:
    print("You failed")
print("Correctly answerd question is: ", correct_score_counter)
print("Incorrectly answerd question is: ", wrong_score_counter)
print("Wrong answers: ", end=" ")
for l in wsc_list:
    print(l, end=" ")
