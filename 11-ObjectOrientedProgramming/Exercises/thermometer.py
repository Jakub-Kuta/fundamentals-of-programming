###
# Class describing a medical thermometer
#
import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print('Thermometer is off')

    def display_temperature(self):
        if self.temperature is None:
            print('No measurement yet')
        elif self.temperature >= 37.0:
            print(f'Temperature: {self.temperature}C (fever)')
            if self.temperature >= 41.0:
                print('CRITICAL TEMPERATURE!!')
        else:
            print(f'Temperature: {self.temperature}C')
