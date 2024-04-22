import speech_recognition as sr

a = sr.Recognizer()
mic_index = 2 # Replace with the correct device index for your Blue Yeti
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"Microphone with name \"{name}\" found for `Microphone(device_index={index})`")

with sr.Microphone() as source:
    print("Say something!")
    audio = a.listen(source)
    data = a.recognize_google(audio)
    print(data)
