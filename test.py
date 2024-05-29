from yandex_speech import TTS
import pygame
import os

def speak(text):
    tts = TTS(lang="ru_RU", emotion="good", speaker="oksana", key="YOUR_YANDEX_API_KEY")
    tts.generate(text)
    tts.save("response.ogg")

    pygame.mixer.init()
    pygame.mixer.music.load("response.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    os.remove("response.ogg")

if __name__ == "__main__":
    speak("Привет, это голосовой помощник от Яндекс!")
