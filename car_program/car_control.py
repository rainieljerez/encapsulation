from car import Car
from car_view import CarView

class CarController:

    def __init__(self, car: Car, view: CarView):
        self._car = car
        self._view = view
        self._view.set_car_label(f"{car.year_model} {car.make}")
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[INIT] {car.year_model} {car.make} — ready to go.")
        self._view.btn_accel.config(command=self._on_accelerate)
        self._view.btn_brake.config(command=self._on_brake)
        self._view.btn_reset.config(command=self._on_reset)

    def _on_accelerate(self):
        self._car.accelerate()
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[ACCEL] Speed → {self._car.get_speed()} mph")

    def _on_brake(self):
        self._car.brake()
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[BRAKE] Speed → {self._car.get_speed()} mph")

    def _on_reset(self):
        self._car.reset()
        self._view.update_gauge(0)
        self._view.clear_log()
        self._view.log(f"[RESET] {self._car.year_model} {self._car.make} — ready.")