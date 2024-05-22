import speech_recognition as sr
import pyttsx3
import os
import subprocess

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except Exception as e:
            print(f"Ошибка при записи аудио: {e}")
            return "Не удалось записать аудио"
        
        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали: " + text)
            return text.lower()  # Приводим текст к нижнему регистру для удобства
        except sr.UnknownValueError:
            return "Не удалось распознать аудио"
        except sr.RequestError as e:
            return "Ошибка сервиса; {0}".format(e)

def speak(text):
    engine = pyttsx3.init()
    
    # Получение и вывод доступных голосов
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voice {i}:")
        print(f" - ID: {voice.id}")
        print(f" - Name: {voice.name}")
        print(f" - Languages: {voice.languages}")
        print(f" - Gender: {voice.gender}")
        print(f" - Age: {voice.age}")
    
    # Установка голоса (можно выбрать другой голос, изменив индекс)
    engine.setProperty('voice', voices[1].id)  # Пример: выбираем второй доступный голос

    # Установка скорости речи (слова в минуту)
    engine.setProperty('rate', 150)  # Пример: 150 слов в минуту

    # Установка громкости (от 0.0 до 1.0)
    engine.setProperty('volume', 0.9)  # Пример: 90% громкости
    
    engine.say(text)
    engine.runAndWait()

def open_program(command):
    if "браузер" in command:
        speak("Открываю браузер")
        subprocess.run(["start", "chrome"], shell=True)  # Пример для Google Chrome
    elif "блокнот" in command:
        speak("Открываю блокнот")
        subprocess.run(["notepad.exe"], shell=True)
    elif "проводник" in command:
        speak("Открываю проводник")
        subprocess.run(["explorer.exe"], shell=True)
    elif "калькулятор" in command:
        speak("Открываю калькулятор")
        subprocess.run(["calc.exe"], shell=True)
    else:
        speak("Команда не распознана")

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if "стоп" in command:
            speak("До свидания!")
            break
        else:
            open_program(command)
            speak("Вы сказали: " + command)
