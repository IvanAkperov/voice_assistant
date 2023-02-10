import requests
import pyautogui
import webbrowser
from bs4 import BeautifulSoup
from random import choice
from gtts_test import gtts_func


# заголовки для успешного статус кода
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36"}


class FilmSearcher:

    def __init__(self, lst: list, link: str):
        self.lst = lst
        self.link = link

    def get_response(self):
        """
        Ф-ция, получающая ответ от страницы и находящая нужные теги в переданной ссылке
        """
        req = requests.get(self.link, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        parser = soup.find_all("td", class_="titleColumn")
        return parser

    def find_all_links(self):
        """
        Ф-ция, находящая все ссылки
        :return str
        """
        for film in self.get_response():
            self.lst.append(
                {
                    "https://www.imdb.com/" + film.find("a").get("href"),
                    film.find("a").get_text(strip=True)
                }
            )
        return choice(self.lst)

    def open_link(self, x, y, num):
        """
        Ф-ция, управляющая клавиатурой
        :param x: int
        :param y: int
        :param num: int
        """
        pyautogui.moveTo(1014, 75)
        pyautogui.click()
        pyautogui.moveTo(x, y)
        pyautogui.PAUSE = num
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(325, 794)
        pyautogui.moveTo(327, 702)
        pyautogui.click()
        pyautogui.moveTo(1210, 800)
        pyautogui.click()


class Talking:

    def __init__(self, title: str):
        self.title = title

    def tell_the_title(self):
        """
        Ф-ция, где Алёна произносит название фильма
        """
        gtts_func(text=f"Сегодня предлагаю тебе посмотреть фильм под названием: {self.title}. Включаю трейлер",
                  file_name="enginge.mp3")


def final_func():
    temp = FilmSearcher(lst=[], link="https://www.imdb.com/chart/top")
    link = temp.find_all_links()
    links = []
    word = []
    for i in str(link):
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i in alphabet:
            word.append(i)
        elif i == " ":
            word.append(i.replace(",", ""))
        else:
            links.append(i)
    name, itog = "", ""
    for i in word:
        name += i
    for i in links:
        if i not in ",{}@'":
            itog += i
    webbrowser.open(itog)
    Talking(title=name).tell_the_title()
    temp.open_link(x=670, y=827, num=1.5)
