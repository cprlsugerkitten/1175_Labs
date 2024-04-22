import speech_recognition as sr
import pygame
import random
import time

#specify path to songs here

#create array mapping audio files with lyrics to finish
songs = {
    "Song 1": {
        "file_path": "songs/ambitionz_as_a_ridah.mp3",
        "start_time": 60,  #time at which song will start
        "play_duration": 10,  #how long song will play
        "leading_lyric": "I won't deny it, I'm a straight _____", #lyrics leading up to lyric to finish, pass this string to LCD
        "expected_lyric": "ridah" #expected lyric
    },
    # Add more songs similarly
}


def play_song_segment(song_data):
    pygame.mixer.init()
    pygame.mixer.music.load(song_data["file_path"])
    pygame.mixer.music.play(start=song_data["start_time"])
    time.sleep(song_data["play_duration"])
    pygame.mixer.music.stop()


def recognize_speech_from_mic(recognizer, microphone, duration):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source, duration=duration)
    
    # Recognize speech using Google Web Speech API
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Request failed"


def start_game(songs):
    song_name, song_data = random.choice(list(songs.items()))
    
    print(f"Now playing: {song_name}")
    play_song_segment(song_data)
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("Listening for the verse...")
    user_input = recognize_speech_from_mic(recognizer, microphone, duration=5)  # listens for 5 seconds
    
    if user_input.lower() == song_data["expected_lyric"].lower():
        print("Correct!")
        # Continue the game or perform some action
    else:
        print("Incorrect! Game Over.")
        # End the game or perform some action

# Choose a random song and start the game
start_game(songs)
