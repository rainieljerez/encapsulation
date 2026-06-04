import tkinter as tk
from car import Car

class CarView:
    BG = "#0f0f0f"
    PANEL_BG = "#1a1a1a"
    ACCENT = "#e8ff00"
    TEXT_LT = "#f0f0f0"
    TEXT_DIM = "#666666"
    GAUGE_BG = "#2a2a2a"
    GAUGE_FG = "#e8ff00"
    BTN_ACCEL = "#e8ff00"
    BTN_BRAKE = "#ff3c3c"
    BTN_RESET = "#333333"

    MAX_SPEED = Car.MAX_SPEED

    def __init__(self, root: tk.Tk):
        self.root = root
        self._build_window()
        self._build_header()
        self._build_gauge()
        self._build_log()
        self._build_buttons()

    def _build_window(self):
        self.root.title("Car")
        self.root.configure(bg = self.BG)
        self.root.resizable(False, False)
        self.root.geometry("460x620")

    def _build_header(self):
        hdr = tk.Frame(self.root, bg = self.BG)
        hdr.pack (fill = "x", padx = 28, pady = (28, 0))

        tk.Label(
            hdr, text = "Car",
            bg = self.BG, fg = self.ACCENT,
            font = ("Courier New", 11, "bold"), anchor = "w"
        ).pack(side = "left")

        self._car_lbl = tk.Label(
            hdr, text="",
            bg=self.BG, fg=self.TEXT_DIM,
            font=("Courier New", 10), anchor="e"
        )
        self._car_lbl.pack(side="right")

    def set_car_label(self, text: str):
        self._car_lbl.config(text=text)

    def _build_gauge(self):
        frame = tk.Frame(self.root, bg = self.BG)
        frame.pack(padx =28, pady = 20)

        self._canvas = tk.Canvas(
            frame, width = 400, height = 200,
            bg = self.PANEL_BG, highlightthickness = 0, bd = 0
        )
        self._canvas.pack()

        self._canvas.create_text(200, 22, text = "SPEED",
             fill = self. TEXT_DIM, font = ("Courier New", 9, "bold"))
        self._canvas.create_text(200, 170, text = "mph",
             fill = self.TEXT_DIM, font = ("Courier New", 9,))
        self._canvas.create_rectangle(40, 80, 360, 110,
             fill = self.GAUGE_BG, outline = "")

        self._bar = self._canvas.create_rectangle(
            40, 80, 40, 110, fill = self.GAUGE_FG, outline = "")

        self._speed_text = self._canvas.create_text(
            200, 140, text = "0",
            fill = self.TEXT_LT, font = ("Courier New", 48, "bold"), anchor = "center"
        )

        for i in range(0, self.MAX_SPEED + 1, 25):
            x = 40 + (i / self.MAX_SPEED) * 320
            self._canvas.create_line(x, 75, x, 115, fill=self.TEXT_DIM, width=1)
            self._canvas.create_text(x, 68, text=str(i),
                                     fill=self.TEXT_DIM, font=("Courier New", 7))

    def update_gauge(self, speed: int):
        ratio = speed / self.MAX_SPEED
        fill_x = 40 + ratio * 320
        if ratio < 0.5:
            r, g = int(ratio * 2 * 200), 220
        else:
            r, g = 220, int((1 - ratio) * 2 * 220)
        self._canvas.coords(self._bar, 40, 80, fill_x, 110)
        self._canvas.itemconfig(self._bar, fill=f"#{r:02x}{g:02x}00")
        self._canvas.itemconfig(self._speed_text, text=str(speed))

    def _build_log(self):
        frame = tk.Frame(self.root, bg=self.BG)
        frame.pack(fill="both", padx=28, pady=(0, 14))

        tk.Label(frame, text="LOG",
                 bg=self.BG, fg=self.TEXT_DIM,
                 font=("Courier New", 8, "bold"), anchor="w"
                 ).pack(fill="x")

        self._log = tk.Text(
            frame, height=7, width=48,
            bg=self.PANEL_BG, fg=self.TEXT_LT,
            insertbackground=self.ACCENT,
            font=("Courier New", 9),
            relief="flat", bd=0, state="disabled", wrap="word"
        )
        self._log.pack()

    def log(self, message: str):
        self._log.config(state="normal")
        self._log.insert("end", message + "\n")
        self._log.see("end")
        self._log.config(state="disabled")

    def clear_log(self):
        self._log.config(state="normal")
        self._log.delete("1.0", "end")
        self._log.config(state="disabled")

    def _build_buttons(self):
        frame = tk.Frame(self.root, bg=self.BG)
        frame.pack(padx=28, pady=(0, 28), fill="x")

        cfg = dict(font=("Courier New", 11, "bold"),
                   relief="flat", bd=0, cursor="hand2", pady=12)

        self.btn_accel = tk.Button(frame, text="▲  ACCELERATE",
                                   bg=self.BTN_ACCEL, fg=self.BG,
                                   activebackground="#c8df00", activeforeground=self.BG, **cfg)
        self.btn_accel.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        self.btn_brake = tk.Button(frame, text="▼  BRAKE",
                                   bg=self.BTN_BRAKE, fg=self.TEXT_LT,
                                   activebackground="#cc2020", activeforeground=self.TEXT_LT, **cfg)
        self.btn_brake.grid(row=0, column=1, sticky="ew", padx=(6, 0))

        self.btn_reset = tk.Button(frame, text="↺  RESET",
                                   bg=self.BTN_RESET, fg=self.TEXT_DIM,
                                   activebackground="#444", activeforeground=self.TEXT_LT, **cfg)
        self.btn_reset.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)



