from gpiozero import Button, RotaryEncoder
from signal import pause


# Rotary Encoder 2
input_rotor = RotaryEncoder(19, 26, wrap=True, max_steps=12)
input_rotor.steps = 24


def encoder_test():
    def clockwise():

        turn_clockwise = input_rotor.steps
        input_rotor.steps = input_rotor.steps + 1
        print("Turned clockwise this much: ", turn_clockwise)

    def counter_clockwise():
        turn_counter = input_rotor.steps
        input_rotor.steps = input_rotor.steps - 1
        print("Turned counter clockwise this much: ", turn_counter)

    while True:

        input_rotor.when_rotated_clockwise = clockwise

        input_rotor.when_rotated_counter_clockwise = counter_clockwise

        pause()


if __name__ == "__main__":
    encoder_test()
