import random
from gtts_test import gtts_func


lst = []
with open("documents\\new_cities.txt", "r", encoding="utf-8") as file:  # открываем список на чтение
    result = file.read().split("\n")
    for i in result:
        lst.append(i)  # пополняем список
    random.shuffle(lst)  # перемешиваем в случайном порядке


def cities_game():
    gtts_func(text="Сейчас мы сыграем с тобой в города. Для окончания игры просто напиши выход."
                   "Я начну первая.", file_name="city.mp3")
    print("\n" * 10)
    print("Правила игры:\n1. Пишешь название русского города.\n2. Алёна присылает новый город, "
          "оканчивающийся на последнюю букву твоего города.\n3. Пишешь новый город, оканчивающийся "
          "на последнюю букву города Алёны.\n Если город оканчивается на ь, ы, й, то и Алёна и игрок"
          " называют город на предпоследнюю букву. Пример - Липецк-Казань-Норильск")
    print()
    count = 0
    bot = random.choice(lst)
    print(f"Ответ Алёны: {bot}")
    game_over = False
    while not game_over:
        if bot[-1] in ("ь", "й", "ы"):
            res = -2
        else:
            res = -1
        city = input("Введи ответ: ").title()
        if city == "Выход":
            game_over = True
            break

        elif city not in lst:
            gtts_func(text="Такого города в списке нет, либо он уже был использован", file_name="no_city.mp3")
        elif city[0] != bot[res].title():
            letter = bot[res]
            gtts_func(text=f"Ошибка! Город должен начинаться с буквы {letter}", file_name="mistake.mp3")

        else:
            count += 1
            if city[-1] in ("ь", "ы", "й"):
                lst.remove(city)
                for i in lst:
                    if i.lower()[0] == city[-2] and i.lower()[-1] not in ("ь", "ы", "й"):
                        bot = i
                        print(f"Ответ Алёны: {bot}")
                        print("-" * 30)
                        gtts_func(text=bot, file_name="bot_ans.mp3")
                        lst.remove(i)
                        break
                    else:
                        if i[-1] in ("ь", "ы", "й"):
                            letter = i[-2]
                            for j in lst:
                                if j.startswith(letter):
                                    bot = i
                                    print(f"Ответ Алёны: {bot}")
                                    print("-" * 30)
                                    gtts_func(text=bot, file_name="bot_ans2.mp3")
                                    lst.remove(i)
                                    break

                else:
                    game_over = True
                    gtts_func(text="Я сдаюсь", file_name="surrender.mp3")
                    break
            else:
                lst.remove(city)
                for i in lst:
                    if i.lower()[0] == city[-1]:
                        bot = i
                        print(f"Ответ Алёны: {bot}")
                        print("-" * 30)
                        gtts_func(text=bot, file_name="bot_ans3.mp3")
                        lst.remove(i)
                        break
                else:
                    game_over = True
                    gtts_func(text="Я сдаюсь", file_name="surrender2.mp3")
                    break
    if game_over:
        gtts_func(
            text=f"Спасибо за игру.{'Вы неплохо справились' if count > 5 else 'Ничего, в следующий раз вспомните больше городов.'}!",
            file_name="thanks.mp3")
