from duck import MalardDuck, RubberDuck, ModelDuck
from fly_behavior import FlyWithRocketPower


def mini_duck_simulator():
    mallard = MalardDuck()
    mallard.perform_quack()
    mallard.perform_fly()


if __name__ == '__main__':
    mini_duck_simulator()
