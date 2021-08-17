#!/usr/bin/python3

from duck import MalardDuck, RubberDuck, ModelDuck
from fly_behavior import FlyWithRocketPower, FlyNoWay
from quack_behavior import MuteQuack, Squeak


def mini_duck_simulator():
    mallard = MalardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()
    print('-----------------------------')
    rubber_duck = RubberDuck()
    rubber_duck.display()
    rubber_duck.quack_behavior = Squeak()
    rubber_duck.fly_behavior = FlyNoWay()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()
    rubber_duck.swim()
    print('-----------------------------')
    model_duck = ModelDuck()
    print(' -- Before changing --')
    model_duck.display()
    # mute quack
    model_duck.perform_quack()
    # fly no way
    model_duck.perform_fly()
    print('-- After changing on the fly --')
    model_duck.display()
    model_duck.fly_behavior = FlyWithRocketPower()
    model_duck.perform_fly()


if __name__ == '__main__':
    mini_duck_simulator()
