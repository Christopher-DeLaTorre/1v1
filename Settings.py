
class Settings:
    def __init__(self, time=600, volume=100):
        self._time = time 
        self._volume = volume

    def _change_time(self, time):
        self._time = time
        return self._time

    def _change_volume(self, volume):
        if volume > 100:
            self._volume = volume
            return self._volume
        else:
            return "invalid option."



