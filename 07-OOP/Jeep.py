class Jeep:

    def turn_on(self):
        print("You start the engin")
        return self # to use method chainning we need to return self otherwise each method is returning none

    def drive(self):
        print('You drive the car')
        return self

    def brake(self):
        print('You step on the brake')
        return self

    def turn_off(self):
        print('You turn off the engine')
        return self

