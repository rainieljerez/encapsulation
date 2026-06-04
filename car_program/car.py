class Car:

    MIN_SPEED = 0
    MAX_SPEED = 150
    STEP = 5

    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    @property
    def year_model(self) -> int:
        return self.__year_model

    @property
    def make(self) -> str:
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self) -> None:
        self.__speed = min(self.__speed + self.STEP, self.MAX_SPEED)

    def brake(self) -> None:
        self.__speed = max(self.__speed - self.STEP, self.MIN_SPEED)

    def reset(self) -> None:
        self.__speed = 0