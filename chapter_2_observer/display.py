from abc import ABC, abstracmethod
from observer import Observer


class DisplayElement(ABC):
    '''Display element abstract class'''

    @abstractmethod
    def display(self):
        raise NotImplementedError()


class CurrentConditionsDisplay(Observer, DisplayElement):
    '''Implementation of current condition display'''

    def __init__(self, weather_data):
        self.temperature = 0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print("Current conditions: {0}F degress and {1}% humidity".format(
            self.temperature, self.humidity))


class StatisticDisplay(Observer, DisplayElement):
    '''Implementations of statistic display'''

    def __init__(self, weather_data):
        self.temperature = 0
        self.last_temp = 0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.last_temp = self.temperature
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        if not self.last_temp == 0:
            min_temp = self.last_temp
        else:
            min_temp = self.temperature
        print('Min/Avg/Max Temperature: {0}/{1}/{2}'.format(min(min_temp,
              self.temperature), (min_temp+self.temperature)//2, max(min_temp, self.temperature)))


class ForecastDisplay(Observer, DisplayElement):
    '''Implementations of forecast display'''

    def __init__(self, weather_data):
        self.temperature = 0
        self.humidity = 0.0
        self.last_humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.last_humidity = self.humidity
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        if self.humidity == self.last_humidity:
            print('Forecast: More of the same')
        elif self.humidity > 70:
            print('Forecast: Watch out for cooler, rainy weather')
        else:
            print('Forecast: Improving weather on the way!')
