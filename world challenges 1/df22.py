# tocar música
from pygame import mixer
mixer.init()
mixer.music.load('exe21.mp3')
mixer.music.play()
input()
mixer.event.wait()
