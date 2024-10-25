
#? Media Player Management System

from abc import ABC, abstractmethod

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MusicPlayer(Playable):
    def play(self):
        print("Play music")

    def pause(self):
        print("Pause")

    def stop(self):
        print("Stop music")

class VideoPlayer(Playable):
    def play(self):
        print("Play video")

    def pause(self):
        print("Pause video")

    def stop(self): 
        print("Pause video")

class PodcastPlayer(Playable):
    def play(self):
        print("Play podcast")

    def pause(self):
        print("Pause podcast")

    def stop(self):
        print("Pause podcast")

# Usage
players = [MusicPlayer(), VideoPlayer(), PodcastPlayer()]
for player in players:
    player.play()
    player.pause()
    player.stop()
