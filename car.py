class car:
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
    