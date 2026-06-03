class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        self.__speed = speed if speed is not None else Fan.SLOW
        self.__radius = radius
        self.__color = color
        self.__on = on

    def getSpeed(self):
        return self.__speed

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def isOn(self):
        return self.__on

    def setSpeed(self, speed):
        self.__speed = speed

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def setOn(self, on):
        self.__on = on

    def __str__(self):
        speed_names = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}
        return (
            f"Speed  : {speed_names.get(self.__speed, self.__speed)}\n"
            f"Radius : {self.__radius}\n"
            f"Color  : {self.__color}\n"
            f"On     : {self.__on}"
        )
