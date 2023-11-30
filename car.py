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
            raise Exception(f)