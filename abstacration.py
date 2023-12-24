from abc import abstractmethod, ABC

class Vehicle(ABC):
    def __init__(self, speed, year):
        self.speed = speed
        self.year = year

    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def __init__(self, canClimbMountains, speed, year):
        Vehicle.__init__(self, speed, year)
        self.canClimbMountains = canClimbMountains

    def drive(self):
        print("Car is in drive mode")
print(Car("Can climb mountains",50,2010).start())