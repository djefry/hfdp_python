from abc import ABC, abstractmethod


class Beverage(ABC):
    '''Beverage abstract class'''

    def __init__(self, description):
        self.description = description

    @abstractmethod
    def get_description(self):
        pass

    @abstracmethod
    def cost(self):
        pass
