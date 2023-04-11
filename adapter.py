# Task: Write an adapter for the Speedometer to make it work with the CarDisplay
import random


class MphSpeedometer:
    """We are pretending this is a third-party class we can't change"""

    def __init__(self):
        pass

    def get_speed(self):
        """Returns speed in MPH"""
        speed = random.randint(0, 100)
        print("Speed in MPH: {}".format(speed))
        return speed


class MphToKphSpeedometerAdapter:
    raise NotImplementedError('Implement me!')


class CarDisplay:
    """TODO: change to take in the MphtoKphSpeedometerAdapter instead of the Speedometer"""

    def __init__(self, speedometer: MphSpeedometer):
        self.speedometer = speedometer

    def show_speed(self):
        speed = self.speedometer.get_speed()
        print(f'Speed: {speed}')


if __name__ == '__main__':
    """TODO: change as needed for your new adapter"""
    speedometer = MphSpeedometer()
    car_display = CarDisplay(speedometer)
    car_display.show_speed()