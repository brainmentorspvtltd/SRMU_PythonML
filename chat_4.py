import datetime
import os, random

msg = "hello how are you ?"

helloIntent = ["hello","hi","hey","hey there","hello there"]
dateIntent = ["date","please tell me date","date please"]
timeIntent = ["time","time please","what's the time"]
musicIntent = ["play music","start song"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = datetime.datetime.now().date()
        print(d.strftime("%d/%m/%y,%a"))
    elif msg in timeIntent:
        t = datetime.datetime.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg in musicIntent:
        os.chdir(r"C:\Users\asus\Music")
        songs = os.listdir()
        random_song = random.choice(songs)
        os.startfile(random_song)
    elif msg == "show songs":
        os.chdir(r"C:\Users\asus\Music")
        songs = os.listdir()

        for i in range(len(songs)):
            print(i,songs[i])
        song = int(input("Enter the song number you want to play : "))
        os.startfile(songs[song])
        
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
