import pyttsx3
import os
import wikipedia

engine = pyttsx3.init()

def play_music(song):
    path = "Путь к папке с музыкой"
    music_files = os.listdir(path)
    for file in music_files:
        if song.lower() in file.lower():
            os.startfile(os.path.join(path, file))
            break

def search_wikipedia(query):
    summary = wikipedia.summary(query, sentences=2)
    print(summary)

# Пример использования
text = input("Чем я могу помочь? ")

if "напомни" in text:
    reminder_text = input("Какое напоминание? ")
    reminder_time = input("На какое время? ")
    set_reminder(reminder_text, reminder_time)

elif "включи музыку" in text:
    song_name = input("Какую песню включить? ")
    play_music(song_name)

elif "поиск" in text:
    search_query = input("Что найти? ")
    search_wikipedia(search_query)

import requests

def get_weather(city):
    api_key = "Ваш API"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info = f"Погода в городе {city}: {description}\n"
        weather_info += f"Температура: {temperature}°C\n"
        weather_info += f"Влажность: {humidity}%\n"
        weather_info += f"Скорость ветра: {wind_speed} м/с"

        return weather_info
    else:
        return "Не удалось получить информацию о погоде"

city = "Санкт-Петербург"
print(get_weather(city))

from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language=target_language)

    return translation["translatedText"]

text = "Hello World!"
target_language = "ru"
print(translate_text(text, target_language))

import webbrowser

def search(query):
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

query = "как приготовить пиццу"
search(query)

import schedule
import time

def task():
    print("Выполняю задачу...")

schedule.every(1).minutes.do(task)

schedule.every().day.at("10:00").do(task)

schedule.every().friday.at("18:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
