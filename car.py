class Car:
    def __init__(self, top_speed):
        self.settopspeed(top_speed)
        self.speed = 0

    def settopspeed(self, top_speed):
        if top_speed < 0:
            raise ValueError(f"Invalid top speed: {top_speed}")
        self.topspeed = top_speed

    def gettopspeed(self):
        return self.gettopspeed
    
    def getspeed(self):
        return self.speed

    def accelerate(self):
        if self.speed + 10 > self.topspeed:
            self.speed = self.topspeed
            raise Exception(f"Cannot accelerate above top speed: {self.topspeed}")
        
    def decelerate(self):
        if self.speed - 10 < 0:
            self.speed = 0
            raise Exception("Cannot decelerate below zero")
        self.speed -= 10

    def __str__(self):
        return f"Car going {self.speed}/{self.topspeed} kmph"

car1 = Car(250)
print(car1)

try:
    car2 = Car(-99)
    print(car2)
except Exception as e:
    print(e)

try:
    for _ in range(30):
        car1.accelerate()
        print(car1)
except Exception as e:
    print(e)

    for _ in range(30):
        try:
            car1.decelerate()
            print(car1)
        except Exception as e:
            print(e)
try:
    new_top_speed = float(input("Enter a new top speed: "))
    car1.settopspeed(new_top_speed)
except ValueError as e:
    print(e)

#3.1
class SpeedException(Exception):
    pass

class Car:
    def __init__(self, top_speed):
        self.speed = 0
        self.settopspeed(top_speed)

    def settopspeed(self, top_speed):
        if top_speed > 0:
            self.topspeed = top_speed
        else:
            raise SpeedException(f"Invalid top speed: {top_speed}")

    def getTopSpeed(self):
        return self.topspeed

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        if self.speed + 10 > self.topspeed:
            self.speed = self.topspeed
            raise SpeedException(f"Cannot accelerate above top speed: {self.topSpeed}")
        else:
            self.speed += 10

    def decelerate(self):
        if self.speed - 10 < 0:
            self.speed = 0
            raise SpeedException("Cannot decelerate below zero")
        else:
            self.speed -= 10

    def __str__(self):
        return f"Car going {self.speed}/{self.topspeed} kmph"

#3.2
class NoDriverException(Exception):
    def __init__(self):
        super().__init__("Cannot drive without a Driver")

class Car:
    def __init__(self, top_speed):
        self.speed = 0
        self.settopspeed(top_speed)
        self.driver = None

    def accelerate(self):
        if self.driver is None:
            raise NoDriverException()

    def decelerate(self):
        if self.driver is None:
            raise NoDriverException()
    
    def setDriver(self, driver):
        self.driver = driver
