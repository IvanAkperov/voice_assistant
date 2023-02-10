import os
import random
from datetime import datetime
from random import choice
from gtts_test import gtts_func, sr_audio

# список фраз настроения Алёны
alena_mood = ("Все хорошо", "Не очень", "Бывало и лучше", "Все замечательно", "Отлично!", "Неплохо вроде", "Нормально")
# список слов предположительно содержащий ответ на вопрос Алёны
my_mood = ("хорошо", "нормально", "более-менее", "отлично", "превосходно",
           "замечательно", "офигенно", "круто", "восхитительно", "супер", "неплохо", "чудесно", "шикарно", "классно")


def adviser():
    """
    Ф-ция, считывающая случайный совет из advice.txt, а затем произносящая его с помощью gtts_func
    """
    with open("documents\\advice.txt", "r", encoding="utf-8") as file:
        gtts_func(choice([i for i in file.readlines()]), file_name="advice.mp3")


def timer():
    """
    Ф-ция, произносящая текущее время
    """
    gtts_func(f"Сейчас {datetime.now().hour} часов {datetime.now().minute} минут", file_name="time.mp3")


def shutdown():
    """
    Ф-ция, отключающая компьютер
    """
    gtts_func(text="Хорошо, выключаю", file_name="comp_off.mp3")
    os.system("shutdown -s")


def jokes():
    """
    Ф-ция, рассказывающая случайный анекдот
    """
    with open("documents\\jokes.txt", "r", encoding="utf-8") as nf:
        gtts_func(text=random.choice([i for i in nf.readlines()]), file_name="joke.mp3")


def zametka():
    gtts_func(text="Какую заметку добавить?", file_name="zam.mp3")  # спрашиваем у пользователя какую заметку внести
    with open(f"documents\\заметки.txt", "a", encoding="utf-8") as file:  # открываем файл с заметками
        file.write(f"❗ {sr_audio()} - задача от {datetime.now()}\n")  # записываем заметку и время добавления
        gtts_func(text="Заметка добавлена. Можешь проверять.", file_name="say.mp3")


def mood():
    """
    Ф-ция, где Алёна говорит о ёё настроении, а так же спрашивает у пользователя в ответ
    """
    gtts_func(text=random.choice(alena_mood), file_name="mood.mp3")
    gtts_func(text="А как у вас?", file_name="reply.mp3")
    text = sr_audio()
    if text in my_mood:
        gtts_func(text="Рада слышать, что у вас все хорошо!", file_name="otvet.mp3")
    else:
        gtts_func(text="Надеюсь, что все плохое останется у вас позади", file_name="otvet2.mp3")
