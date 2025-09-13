import speech_recognition as sr
import keywords
import spotify
import actions
from gtts import gTTS
import os
import tempfile
import pygame
import threading
import uuid

def speak(input: str, lang='en', accent='co.uk'):
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
            
            if keywords.input.playSong.lower() in text.lower() and keywords.input.phone.lower() in text.lower():
                song, artist = actions.getSongInfo(text)
                if song != None or artist != None:
                    spotify.play_song(song_name=song, artist_name=artist, device_id=keywords.output.phone)
                    speak(
                        f"{keywords.output.playSong}{song}"
                        f"{f' by {artist}' if artist else ''}"
                        f"{keywords.output.onPhone}"
                    )

            if keywords.input.playSong.lower() in text.lower() and keywords.input.computer.lower() in text.lower():
                song, artist = actions.getSongInfo(text)
                if song != None or artist != None:
                    speak(
                        f"{keywords.output.playSong}{song}"
                        f"{f' by {artist}' if artist else ''}"
                        f"{keywords.output.onComputer}"
                    )
                    spotify.play_song(song_name=song, artist_name=artist, device_id=keywords.output.pc)
        
        return False


r = sr.Recognizer()
r.energy_threshold = 10
r.dynamic_energy_threshold = True
r.pause_threshold = 2
print("booting up....")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    text = 'booting up'
    print("started")
    if main(source, text) == False:
        exit
