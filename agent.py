import speech_recognition as sr
import keywords
import spotify
import actions
from gtts import gTTS
import os
import tempfile
import pygame
import news
import webbrowser
import threading
import uuid
import secrets

def speak(input: str, lang='en', accent='co.uk', wait=False):
    def play():
        file = os.path.join(tempfile.gettempdir(), f"jarvis_{uuid.uuid4().hex}.mp3")
        tts = gTTS(text=input, lang=lang, tld=accent)
        tts.save(file)

        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock()

        pygame.mixer.music.unload()
        os.remove(file)
    
    if wait:
        play()
    else:
        threading.Thread(target=play, daemon=True).start()


def main(source, text):
        while(text.lower() != keywords.input.killswitch):
            text = ''
            audio = r.listen(source, timeout=None, phrase_time_limit=None)
            try:
                text = r.recognize_google(audio)
                print("Text: "+text)
            except:
                print("Sorry, I did not get that")
            
            if text == keywords.input.activation.lower():
                speak(keywords.output.startup)
            
            if keywords.input.playSong.lower() in text.lower() and keywords.input.secondary.lower() in text.lower():
                song, artist = actions.getSongInfo(text)
                if song != None or artist != None:
                    spotify.play_song(song_name=song, artist_name=artist, device_id=keywords.input.secondayDevice)
                    speak(
                        f"{keywords.output.playSong}{song}"
                        f"{f' by {artist}' if artist else ''}"
                        f"{keywords.output.onPhone}"
                    )

            if keywords.input.playSong.lower() in text.lower() and keywords.input.main.lower() in text.lower():
                song, artist = actions.getSongInfo(text)
                if song != None or artist != None:
                    speak(
                        f"{keywords.output.playSong}{song}"
                        f"{f' by {artist}' if artist else ''}"
                        f"{keywords.output.onComputer}"
                    )
                    spotify.play_song(song_name=song, artist_name=artist, device_id=keywords.input.primaryDevice)

            if keywords.input.set in text.lower() and (keywords.input.main in text.lower() or keywords.input.secondary in text.lower()) and keywords.input.pc or keywords.input.phone in text.lower():
                if keywords.input.phone in text:
                    if keywords.input.main in text.lower():
                        keywords.input.primaryDevice = keywords.output.phone
                    else:
                        keywords.input.secondayDevice = keywords.output.phone
                elif keywords.input.pc in text:
                    if keywords.input.main in text.lower():
                        keywords.input.primaryDevice = keywords.output.pc
                    else: 
                         keywords.input.secondayDevice = keywords.output.pc
                else:
                    speak(
                        "I did not get that, can you repeat that?"
                    )

            if keywords.input.news in text.lower():
                keywords.output.articles = news.getNews()
                speak("Retrieving today's top 10 news articles", wait=True)
                for i, article in enumerate(keywords.output.articles):
                    # speak(f'{i + 1} : {article[0]}', wait=True)
                    print(f'{i + 1} : {article[0]}')

            if keywords.input.inquiry in text.lower():
                webbrowser.get('chrome').open_new_tab( keywords.output.articles[5][1])

r = sr.Recognizer()
r.energy_threshold = 10
r.dynamic_energy_threshold = True
r.pause_threshold = 2
chromePath = r'C:\Program Files\Google\Chrome\Application\Chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
print("booting up....")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    text = 'booting up'
    print("started")
    if main(source, text) == False:
        exit
