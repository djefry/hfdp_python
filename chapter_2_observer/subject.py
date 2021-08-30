from abc import ABC


class Subject(ABC):
    '''Abstract class for Subject so we can create many subject'''

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        '''Attach the observer to the object'''

        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        '''Remove observer from object'''

        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'{observer} not found')

    def notify_observers(self):
        '''Notify all observer abount change in the subject's state'''

        for observer in self.observers:
            observer.update()


class WeatherData(Subject):
    '''Weather O Rama Subject'''

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0.0
        self.pressure = 0.0

    def measurement_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurement_changed()
