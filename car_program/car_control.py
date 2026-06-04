from car import Car
from car_view import CarView

class CarController:
    HOLD_DELAY = 400
    HOLD_INTERVAL = 100

    def __init__(self, car: Car, view: CarView):
        self._car = car
        self._view = view
        self._held_job = None
        self._view.set_car_label(f"{car.year_model} {car.make}")
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[INIT] {car.year_model} {car.make} — ready to go.")
        self._view.btn_accel.bind("<ButtonPress-1>", self._on_accel_press)
        self._view.btn_accel.bind("<ButtonRelease-1>", self._on_release)
        self._view.btn_brake.bind("<ButtonPress-1>", self._on_brake_press)
        self._view.btn_brake.bind("<ButtonRelease-1>", self._on_release)
        self._view.btn_reset.config(command=self._on_reset)

    def _start_hold(self, action_fn):
        action_fn()
        self._held_job = self._view.root.after(
            self.HOLD_DELAY, self._repeat, action_fn)

    def _repeat(self, action_fn):
        action_fn()
        self._held_job = self._view.root.after(
            self.HOLD_INTERVAL, self._repeat, action_fn)

    def _on_release(self, event=None):
        if self._held_job is not None:
            self._view.root.after_cancel(self._held_job)
            self._held_job = None

    def _on_accel_press(self, event=None):
        self._start_hold(self._do_accelerate)

    def _do_accelerate(self):
        self._car.accelerate()
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[ACCEL] Speed → {self._car.get_speed()} mph")

    def _on_brake_press(self, event=None):
        self._start_hold(self._do_brake)

    def _do_brake(self):
        self._car.brake()
        self._view.update_gauge(self._car.get_speed())
        self._view.log(f"[BRAKE] Speed → {self._car.get_speed()} mph")


    def _on_reset(self):
        self._on_release()  # cancel any active hold first
        self._car.reset()
        self._view.update_gauge(0)
        self._view.clear_log()
        self._view.log(f"[RESET] {self._car.year_model} {self._car.make} — ready.")