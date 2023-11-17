from abc import ABC, abstractmethod
import pandas as pd

class Observer(ABC):
    @abstractmethod
    def update(self, representation):
        pass


class PowerRepresentationObserver(Observer):
    def update(self, powers_of_ten):
        print(pd.Series(powers_of_ten))


class NumberRepresentationSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, representation):
        for observer in self._observers:
            observer.update(representation)

    def calculate_powers_of_ten_representation(self, number):
        number_str = str(number)
        dot_index = number_str.find(".")

        representation = []
        for i, digit in enumerate(number_str):
            if i == dot_index:
                continue

            exponent = dot_index - (i if i > dot_index else i + 1)
            representation.append(f"{digit}x10^{exponent}")

        self.notify_observers(representation)

try:
    user_number = float(input("Enter a number: "))
    subject = NumberRepresentationSubject()
    observer = PowerRepresentationObserver()
    subject.add_observer(observer)

    subject.calculate_powers_of_ten_representation(user_number)
except ValueError:
    print("Please enter a valid number")
