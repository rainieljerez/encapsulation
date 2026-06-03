import tkinter as tk
from tkinter import ttk
from fan_class import Fan


class FanWidget(tk.Frame):
    SPEED_DELAY = {Fan.SLOW: 30, Fan.MEDIUM: 12, Fan.FAST: 4}
    SPEED_STEP  = {Fan.SLOW: 2,  Fan.MEDIUM: 5,  Fan.FAST: 12}
    BLADE_COUNT = 4
    BLADE_ARC   = 50

    def __init__(self, parent, fan_class: Fan, label: str):
        super().__init__(parent, bg="#1a1a2e", padx=16, pady=16)
        self.fan    = fan_class
        self._angle = 0
        self._job   = None

        tk.Label(self, text=label, font=("Courier New", 13, "bold"),
                 bg="#1a1a2e", fg="#e0e0ff").pack(pady=(0, 8))

        self.canvas_size = 220
        self.cx = self.cy = self.canvas_size // 2
        self.cv = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size,
                            bg="#0d0d1a", highlightthickness=2,
                            highlightbackground="#3a3a6e")
        self.cv.pack()

        ctrl = tk.Frame(self, bg="#1a1a2e")
        ctrl.pack(pady=10, fill="x")
        self._build_controls(ctrl)

        self.status_lbl = tk.Label(self, font=("Courier New", 8),
                                   bg="#1a1a2e", fg="#555588")
        self.status_lbl.pack(pady=(6, 0))

        self._refresh_button()
        self._draw_fan()
        if fan_class.isOn():
            self._animate()

    def _build_controls(self, ctrl):
        self.toggle_btn = tk.Button(ctrl, font=("Courier New", 10, "bold"),
                                    width=8, cursor="hand2",
                                    command=self._toggle_power)
        self.toggle_btn.grid(row=0, column=0, columnspan=2, pady=(0, 8))

        tk.Label(ctrl, text="Speed", font=("Courier New", 9),
                 bg="#1a1a2e", fg="#8888bb").grid(row=1, column=0, sticky="w")
        self.speed_var = tk.IntVar(value=self.fan.getSpeed())
        spd_frame = tk.Frame(ctrl, bg="#1a1a2e")
        spd_frame.grid(row=1, column=1, sticky="e")
        for text, val in [("S", Fan.SLOW), ("M", Fan.MEDIUM), ("F", Fan.FAST)]:
            tk.Radiobutton(spd_frame, text=text, variable=self.speed_var, value=val,
                           command=self._update_speed,
                           bg="#1a1a2e", fg="#ccccff", selectcolor="#2a2a5e",
                           activebackground="#1a1a2e",
                           font=("Courier New", 9, "bold")).pack(side="left")

        tk.Label(ctrl, text="Radius", font=("Courier New", 9),
                 bg="#1a1a2e", fg="#8888bb").grid(row=2, column=0, sticky="w", pady=4)
        self.radius_var = tk.DoubleVar(value=self.fan.getRadius())
        tk.Scale(ctrl, variable=self.radius_var, from_=3, to=15,
                 orient="horizontal", resolution=1, length=130,
                 bg="#1a1a2e", fg="#ccccff", troughcolor="#2a2a5e",
                 highlightthickness=0,
                 command=lambda e: self._update_radius()
                 ).grid(row=2, column=1, sticky="e")

        tk.Label(ctrl, text="Color", font=("Courier New", 9),
                 bg="#1a1a2e", fg="#8888bb").grid(row=3, column=0, sticky="w")
        self.color_var = tk.StringVar(value=self.fan.getColor())
        colors = ["blue", "yellow", "red", "green", "orange", "white", "cyan", "magenta"]
        color_menu = ttk.Combobox(ctrl, textvariable=self.color_var,
                                  values=colors, width=10, state="readonly",
                                  font=("Courier New", 9))
        color_menu.grid(row=3, column=1, sticky="e")
        color_menu.bind("<<ComboboxSelected>>", lambda e: self._update_color())

    def _blade_color(self):
        c = self.fan.getColor()
        dim = {"blue": "#1a1a66", "yellow": "#555500", "red": "#550000",
               "green": "#005500", "orange": "#553300", "white": "#333333",
               "cyan": "#005555", "magenta": "#550055"}
        return c if self.fan.isOn() else dim.get(c, "#333333")

    def _draw_fan(self):
        self.cv.delete("all")
        cx, cy = self.cx, self.cy
        r_px = max(30, min(int(self.fan.getRadius() * 7), cx - 10))

        self.cv.create_oval(cx - r_px, cy - r_px, cx + r_px, cy + r_px,
                            outline="#3a3a6e", width=2)

        bc = self._blade_color()
        for i in range(self.BLADE_COUNT):
            start = self._angle + i * (360 / self.BLADE_COUNT)
            self.cv.create_arc(cx - r_px, cy - r_px, cx + r_px, cy + r_px,
                               start=start, extent=self.BLADE_ARC,
                               fill=bc, outline="#0d0d1a", width=1, style="pie")

        hub_r = max(8, r_px // 6)
        self.cv.create_oval(cx - hub_r, cy - hub_r, cx + hub_r, cy + hub_r,
                            fill="#0d0d1a", outline="#ccccff", width=2)

        if self.fan.isOn():
            glow = {Fan.SLOW: "#002266", Fan.MEDIUM: "#003388", Fan.FAST: "#0044cc"}
            self.cv.create_oval(cx - r_px - 6, cy - r_px - 6,
                                cx + r_px + 6, cy + r_px + 6,
                                outline=glow.get(self.fan.getSpeed(), "#002266"), width=3)

        status = "● ON" if self.fan.isOn() else "○ OFF"
        self.cv.create_text(cx, self.canvas_size - 12, text=status,
                            font=("Courier New", 9, "bold"),
                            fill="#00ff88" if self.fan.isOn() else "#444466")

        self._update_status()

    def _animate(self):
        if not self.fan.isOn():
            return
        self._angle = (self._angle + self.SPEED_STEP.get(self.fan.getSpeed(), 2)) % 360
        self._draw_fan()
        self._job = self.after(self.SPEED_DELAY.get(self.fan.getSpeed(), 30), self._animate)

    def _stop_animation(self):
        if self._job:
            self.after_cancel(self._job)
            self._job = None

    def _toggle_power(self):
        self.fan.setOn(not self.fan.isOn())
        self._refresh_button()
        if self.fan.isOn():
            self._animate()
        else:
            self._stop_animation()
            self._draw_fan()

    def _update_speed(self):
        self.fan.setSpeed(self.speed_var.get())

    def _update_radius(self):
        self.fan.setRadius(self.radius_var.get())
        self._draw_fan()

    def _update_color(self):
        self.fan.setColor(self.color_var.get())
        self._draw_fan()

    def _refresh_button(self):
        if self.fan.isOn():
            self.toggle_btn.config(text="Turn OFF", bg="#cc2244", fg="white",
                                   activebackground="#aa1133")
        else:
            self.toggle_btn.config(text="Turn ON", bg="#22aa44", fg="white",
                                   activebackground="#119933")

    def _update_status(self):
        speed_names = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}
        self.status_lbl.config(
            text=f"speed={speed_names.get(self.fan.getSpeed())}  "
                 f"radius={self.fan.getRadius():.0f}  "
                 f"color={self.fan.getColor()}"
        )