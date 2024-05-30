import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import pygame
import psutil
import shutil

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

def find_executable(program_name):
    # Ищем программу в системных путях
    executable = shutil.which(program_name)
    if executable:
        return executable

    # Ищем программу среди запущенных процессов
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if program_name.lower() in proc.info['name'].lower():
            return proc.info['exe']
    
    # Пытаемся найти программу в популярных каталогах
    common_paths = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs"),
        os.path.expanduser("~\\AppData\\Local")
    ]
    
    for path in common_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if program_name.lower() in file.lower():
                    return os.path.join(root, file)
    
    return None

def open_program(command):
    app_name = command.split("открыть ")[-1].strip()
    executable_path = find_executable(app_name)
    
    if executable_path:
        speak(f"Открываю {app_name}")
        subprocess.run([executable_path], shell=True)
    else:
        speak(f"Не удалось найти программу {app_name}")

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if "стоп" in command:
            speak("До свидания!")
            break
        else:
            open_program(command)
            speak("Вы сказали: " + command)
