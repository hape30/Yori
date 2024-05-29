import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import pygame

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        try:
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=1)
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
    tts = gTTS(text=text, lang='ru')
    tts.save("response.mp3")
    
    # Инициализация pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    
    # Ждем окончания воспроизведения
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Останавливаем и закрываем pygame mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    
    os.remove("response.mp3")

def open_program(command):
    if "браузер" in command:
        speak("Открываю браузер")
        subprocess.run(["start", "chrome" or "yandex" or "firefox"], shell=True)  # Пример для Google Chrome
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
