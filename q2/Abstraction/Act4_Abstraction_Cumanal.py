
from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):

    def get_reading(self):
        return "7.2 pH (Neutral)"


class TempSensor(Sensor):

    def get_reading(self):
        return "24.5°C"


print("--- Lab Inventory System ---")

ph = PHSensor()
print("[pH Sensor] Reading:", ph.get_reading())

temp = TempSensor()
print("[Temperature Sensor] Reading:", temp.get_reading())

print("----------------------------")

