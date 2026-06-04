
import tkinter as tk

from car import Car
from car_view import CarView
from car_control import CarController

def main():
    root = tk.Tk()
    car  = Car(3789, "Bugatti")
    view = CarView(root)
    CarController(car, view)
    root.mainloop()

if __name__ == "__main__":
    main()