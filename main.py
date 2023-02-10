import gtts
import random
from playsound import playsound
from kinopoisk import final_func
from cities import cities_game
from commands_answers import commands
from gtts_test import gtts_func, del_result, sr_audio, translate
from tests import timer, shutdown, adviser, jokes, mood, zametka
from riddle import puzzle


def info():
    """
    Ф-ция, где голосовой ассистент рассказывает о своих возможностях
    """
    gtts_func(text='Меня зовут Алёна, я твоя помощница. Я могу: \nДобавить замeтку.\n'
                   'Посоветовать фильм.\nСыграть с тобой в игру.\nПеревести фразу на английский.'
                   '\nСказать тебе время.\nСообщить как мои дела.\n. Выключить компьютер.'
                   '\nМогу дать совет или же рассказать анекдот.'
                   '\nТак же можешь попробовать отгадать мои загадки',
              file_name="inform.mp3")
    print("1. Добавить в файл заметку\n2. Порекомендовать тебе фильм\n3. Сыграть в игру\n4. Дам совет"
          "\n5. Расскажу шутку\n6. Загадаю загадку\n7. Сообщу время или выключу"
          " компьютер\n8. Переведу фразу на английский")


def time():
    """
    Ф-ция timer, где голосовой ассистент произносит текущее время
    """
    timer()


def turn_off():
    """
    Ф-ция shutdown, выключающая компьютер
    """
    shutdown()


def advice():
    """
    Ф-ция adviser, произносящая случайный совет из списка
    """
    adviser()


def anecdotes():
    """
    Ф-ция jokes, рассказывающая случайный анекдот из списка
    """
    jokes()


def translator():
    translate()


def feeling():
    """
    Ф-ция mood, которая отвечает на вопрос 'как дела', а затем спрашивает такой же вопрос у пользователя
    """
    mood()


def riddles():
    """
    Ф-ция puzzle, воспроизводящая игру в загадки
    """
    puzzle()


def zametki():
    """
    Ф-ция zametka, которая спрашивает у пользователя заметку, а затем добавляет ёё в файл
    """
    zametka()


def kino():
    """
    Ф-ция final_func, советующая случайный фильм
    """
    final_func()


def city_game():
    """
    Ф-ция cities_game, вовзращающая ответ в формате игры
    """
    cities_game()


name_of_assistant = "алёна"  # имя голосового ассистента, для работоспособности всегда обращаемся сначала к ней
assistant_greetings = ("Я вас слушаю", "Да, мой господин?", "Что пожелаете?", "Да-да, звали?", "Что хотели?")
assistant_stop = ("Отключаюсь", "До свидания", "Всего вам доброго!")
gtts_goodbye = gtts.gTTS(random.choice(assistant_stop), lang="ru", slow=False)
gtts_goodbye.save("sounds\\goodbye.mp3")


def main():
    flag = True
    while flag:
        print("В ожидании...")
        try:
            text = sr_audio()
            if text.count(name_of_assistant) > 0:  # если в произносимой речи будет имя ассистента:
                playsound("sounds\\sound.mp3")  # то проигрывается соответствующая мелодия
                print("Я вас слушаю")
                gtts_func(text=random.choice(assistant_greetings), file_name="answer.mp3")  # ответ ассистента
                text = sr_audio()  # ассистент ждёт вашей команды
                if any((i in text) for i in ("стоп", "отключись", "выход", "остановись", "до свидания", "пока",
                                             "до встречи", "всего доброго", "прощай", "отключайся")):
                    playsound("sounds\\goodbye.mp3")
                    del_result(file="sounds\\goodbye.mp3")
                    flag = False
                    break

                for k, v in commands["commands"].items():  # проходим по списку доступных команд
                    if any((x in text) for x in v):  # если есть совпадение:
                        globals()[k]()  # то воспроизводим соответствующую ф-цию

        except UnboundLocalError:
            pass


if __name__ == "__main__":
    main()

