"""
Duck module specify the type of the duck
"""

from abc import ABC, abstractmethod
from fly_behavior import FlyBehavior, FlyWithWings, FlyNoWay
from quack_behavior import QuackBehavior, Quack, MuteQuack


class Duck(ABC):
    '''Duck abstrac class'''

    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    def _check_behavior(self):
        if not self._fly_behavior:
            raise AttributeError('The fly behaviour is not set.')

        if not self._quack_behavior:
            raise AttributeError('The quack behaviour is not set.')

    @property
    def fly_behavior(self):
        raise AttributeError('This is private attribute.')

    @property
    def quack_behavior(self):
        raise AttributeError('This is private attribute.')

    @fly_behavior.setter
    def fly_behavior(self, fb):
        if isinstance(fb, FlyBehavior):
            self._fly_behavior = fb
        else:
            raise TypeError('The argument is not instance of FlyBehavior.')

    @quack_behavior.setter
    def quack_behavior(self, qb):
        if isinstance(qb, QuackBehavior):
            self._quack_behavior = qb
        else:
            raise TypeError('The argument is not instance of QuackBehavior.')

    @abstractmethod
    def display(self):
        raise NotImplementedError()

    def swim(self):
        print("All ducks are float, even decoys!")

    def perform_fly(self):
        self._check_behavior()
        self._fly_behavior.fly()

    def perform_quack(self):
        self._check_behavior()
        self._quack_behavior.quack()


class MalardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print('I\'m a real Mallard duck')


class DecoyDuck(Duck):
    def display(self):
        print('I\'m Decoy duck')


class RubberDuck(Duck):
    def display(self):
        print('I\'m Rubber duck')


class ModelDuck(Duck):
    def __init__(self):
        self._fly_behavior = FlyNoWay()
        self._quack_behavior = MuteQuack()

    def display(self):
        print('I\'m Model duck')


class RedHeadDuck(Duck):
    def display(self):
        print('I\'m RedHead duck')
