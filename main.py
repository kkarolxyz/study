import time
from datetime import datetime


class Sensor:
    def __init__(self, temperature=None, humidity=None, pressure=None):
        self.temp = temperature
        self.hum = humidity
        self.pres = pressure
        print("BME280 - initialization")

    def add_temperature(self):
        print("DEF one")
        time.sleep(2)
        # temp = "temperature from add_temperature"
        # time.sleep(10)
        # return temp

    def update(self, temperature):
        print("DEF two")
        self.add_temperature = temperature



while True:
    sensor = Sensor()
    now = datetime.now()
    sec = now.second
    if sec == 30:
        print(sec)
        sensor.add_temperature()
    else:
        print(sec)
        sensor.update(80)
        print("-----------------------------------------------------")

