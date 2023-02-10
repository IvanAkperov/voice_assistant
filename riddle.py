import random
import time
from gtts_test import gtts_func

# список ответов Алёны, если игрок отгадал загадку
phrases_good_list = ["Молодец, правильно!", "Правильно, красавчик!", "Вы прям гуру по отгадыванию, так держать!",
                     "Вы отгадали, здорово!"]
# список ответов Алёны, если игрок не отгадал загадку
phrases_bad_list = ["Неа, попробуй ещё раз", "Неправильно, попробуйте снова", "Ошибка!"]

# список ответов Алёны на случай если игроку понадобится подсказка
clue_list = ["могу дать подсказку", "хочешь подскажу?", "воспользуйся подсказкой, если не получается",
             "ты всегда можешь получить подсказку"]


def puzzle():
    gtts_func(text=f"Добро пожаловать в мир загадок! Для получения помощи просто напиши подсказка."  # приветствие
                   f"Если надоест играть то просто напиши выход. Поехали!", file_name="welcome.mp3")
    print("\n" * 10)
    right_ans, count = 0, 1  # количество правильных ответов пользователя и номер загадки
    flag = True  # флаг для контроля игры
    while flag:
        gtts_func(text=f"Загадка номер {count}", file_name="count_of_riddles.mp3")
        count += 1  # увеличиваем счетчик номера загадки
        with open("documents\\riddles.txt", "r", encoding="utf-8") as nf:  # открываем документ на чтение
            res = random.choice(nf.readlines()).replace("\n", "").split("\\")  # выбираем случайный элемент из строки
        gtts_func(text=res[0], file_name="rdl.mp3")  # произносим загадку
        print()
        print(res[0])  # печатаем загадку для пользователя, дабы он смог на неё взглянуть
        attempts = 3  # кол-во попыток на отгадывание
        while True:
            print("-" * 10)
            answer = input("Ваш ответ: ").title()
            if answer.isalpha() and answer in res[1]:
                right_ans += 1  # увеличиваем счетчик правильных ответов, если пользователь отгадал загадку
                gtts_func(text=random.choice(phrases_good_list), file_name="ans_res.mp3")
                break
            elif answer == "Выход":
                flag = False
                gtts_func(text=(f"Отлично! Ты отгадал {right_ans} загадки! Кстати, ответ на предыдущую "
                                f"загадку был: {res[1]}" if right_ans > 2 else f"Вы отгадали {right_ans} загадки. "
                                                                               f"В следующий раз обязательно повезёт!"),
                          file_name="result.mp3")
                break
            elif answer == "Подсказка":  # если пользователь попросит подсказу,
                gtts_func(text="Держи подсказку", file_name="clue.mp3")
                print(f"Слово начинается на букву: {res[1][0]}")  # то выводим в качестве подсказки первую букву ответа
            else:
                if attempts == 1:
                    gtts_func(text=f"К сожалению попытки закончились. Правильный ответ был {res[1]}",
                              file_name="otvet.mp3")
                    print(f"Правильный ответ: {res[1]}")
                    time.sleep(3)
                    break
                else:
                    gtts_func(text=random.choice(phrases_bad_list), file_name="negative_ans.mp3")
                    if attempts == 2:  # если у пользователя осталась одна попытка,
                        say = random.randint(0, 1)  # вызываем метод randint
                        if say == 0:  # если равно 0,
                            gtts_func(text=random.choice(clue_list), file_name="maybe.mp3")  # то напоминаем о подсказке
                    attempts -= 1  # уменьшаем счётчик правильных попыток
                    print(f"Кол-во попыток: {attempts}")  # выводим на печать оставшееся кол-во попыток
