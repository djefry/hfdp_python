from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    '''Fly Behaviour Interface'''
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    '''Flying with wings.'''
    def fly(self):
        print('I\'m fly with wings.')

class FlyNoWay(FlyBehavior):
    '''Canot fly.'''
    def fly(self):
        pass

class FlyWithRocketPower(FlyBehavior):
    '''Fly with rocket power.'''
    def fly(self):
        print('I\'m fly with rocket power.')
