import os
import gtts
import speech_recognition as sr
from playsound import playsound
from googletrans import Translator


def gtts_func(text: str, file_name: str, path="sounds"):
    """
    Ф-ция, произносящая текстовый ответ.
    После сохраняет его в mp3 файл, произносит, и сразу удаляет
    """
    temp = gtts.gTTS(text, lang="ru")
    temp.save(f"{path}\\{file_name}")
    playsound(f"{path}\\{file_name}")
    del_result(file=f"{path}\\{file_name}")


def del_result(file):
    """
    Ф-ция, проверяющая на наличие файла в директории.
    Если файл существует, то удаляем его
    """
    if os.path.isfile(fr"{os.getcwd()}\{file}"):
        os.remove(fr"{os.getcwd()}\{file}")


def sr_audio():
    """
    Ф-ция, считывающая речь с микрофона и переводящая его в текст
    """
    recognition = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = recognition.listen(mic)
        try:
            result = recognition.recognize_google(audio, language="ru-RU").lower()
        except sr.UnknownValueError:
            pass
    return result


def translate():
    """
    Ф-ция, которая принимает фразу от пользователя и переводит ее на английский
    """
    gtts_func(text="Скажи фразу и я переведу ее на английский", file_name="say_so_translate.mp3")
    text = sr_audio()  # принимает фразу от пользователя
    translator = Translator()
    result = translator.translate(text=text)
    say_result = gtts.gTTS(text=result.text, lang="en")  # переписываем ф-цию, чтобы сконвертировать речь на английский
    say_result.save("sounds\\english_phrase.mp3")
    playsound("sounds\\english_phrase.mp3")
    del_result(file="sounds\\english_phrase.mp3")
    print(result.text)
