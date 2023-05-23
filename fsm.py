"Finite state machine module"

import random

class DayFMS:
    'Daily routine in FMS form'
    def __init__(self):
        self.energy = 100
        self.hour = 8
        self.homework = False
        self.current_state = self._sleeping
        self.stopped = False

    def _sleeping(self) -> None:
        'Start state'
        value = random.random()
        if value <= 0.5:
            print('You woke up early and feel a little tired')
            self.current_state = self._awake
            self.energy -= 10
        else:
            print('You woke up lately and you feel good')
            self.hour += 2
            self.current_state = self._awake

    def _awake(self):
        "Awaken state"
        if self.hour == 8:
            print('You went at lesson as usual')
            self.current_state = self._on_lesson
            self.hour += 2
        else:
            print('You woke up to late, so you missed classes')
            self.current_state = self._free_in_ucu
            self.hour += 2

    def _on_lesson(self):
        'On lesson'
        value = random.random()
        if value <= 0.5:
            print('You decided to be active and gain points, but you spend some energy')
            self.energy -=20
        else:
            print("You wasn't too active at lesson")
        self.current_state = self._free_in_ucu
        self.hour += 2

    def _free_in_ucu(self):
        'Free in UCU state'
        value = random.random()
        if self.hour < 18:
            print('You are free at UCU and can do whatever')
            if value <= 0.3:
                print('You decided to spend time with friends, you feel refreshed')
                self.hour += 2
                self.energy += 10
            elif value <= 0.6:
                print('You decided to do homework. It took long')
                self.homework = True
                self.hour += 4
                self.energy -= 40
            else:
                print('You decided to eat at trapezna. You refilled some energy from food')
                self.energy += 20
                self.hour += 2
        else:
            print('If its 6 pm or later, no matter what, you go to the gym')
            self.current_state = self._gym

    def _gym(self):
        'Gym state'
        value = random.random()
        if value <= 0.3:
            print('You decided to do chest, it was fun')
            self.energy -= 20
        elif value <= 0.6:
            print('You decided to do back, it was fun')
            self.energy -= 20
        else:
            print('You decided to do legs, it was very tiredfull')
            self.energy -= 50
        self.hour += 3
        self.current_state = self._home

    def _home(self):
        'Home state'
        print('You are at home')
        if not self.homework and self.energy >= 50:
            self.hour += 4
            print("You haven't done homework yet, so you should do it now")
            self.homework = True
            self.energy -= 40
        elif not self.homework:
            self.hour += 2
            print("You haven't done homework yet, but you \
            feel to tired to do it, so you spend rest of the time watching youtube:(")
        elif self.hour <= 21:
            self.hour += 2
            print('You have nothing to do, so you played some games')
            self.energy += 20
        else:
            print('It is to late, so you go to the bed immideatly')
        self.current_state = self._go_to_bed

    def _go_to_bed(self):
        'Go to the bed state'
        print('You go to bed')
        print('You have done homework, so it is a success'if self.homework else
              "You haven't done homework, that's sad(")
        print("Also, you don't feel too tired" if self.energy > 50 else
              'Also, you are pretty tired')
        self.stopped = True

    def check_if_ended(self) -> bool:
        'Checks if day is ended'
        return self.stopped

    def get_time(self) -> str:
        'Gets current time'
        self.hour = self.hour - 24 if self.hour >= 24 else self.hour
        time = f'{self.hour}am:' if self.hour <= 12 else f'{self.hour - 12}pm:'
        print(time, end = ' ')

def simulation():
    "Simulates the day"
    day = DayFMS()
    status = day.check_if_ended()
    day.current_state()
    while not status:
        day.get_time()
        day.current_state()
        status = day.check_if_ended()
        print()

if __name__ == "__main__":
    simulation()
