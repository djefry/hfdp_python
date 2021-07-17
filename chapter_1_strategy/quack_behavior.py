from abc import ABC, abstractmethod

class QuackBehavior(ABC):
    '''Quack Behavior Interface'''
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    '''Quack.'''
    def quack(self):
        print('I\'m quacking.')

class Squeak(QuackBehavior):
    '''Squack.'''
    def quack(self):
        print('I\'m squacking.')

class MuteQuack(QuackBehavior):
    '''Mute quack.'''
    def quack(self):
        pass
