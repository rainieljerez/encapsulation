import tkinter as tk
from tkinter import ttk
from fan_class import Fan

class FanWidget(tk.Frame):
    speed_delay = {Fan.SLOW: 30, Fan.MEDIUM: 12, Fan.FAST: 4}
    speed_step = {Fan.SLOW: 2, Fan.MEDIUM: 5, Fan.FAST: 12}
    blade_count = 4
    blade_arc = 50

    def __init__(self, parent, fan_class: Fan, label: str):
        super().__init__(parent, bg = "#1a1a2e", padx = 16, pady = 16)
        self.fan_class = fan_class
        self._angle = 0
        self,_job = None

        tk.Label(self, text = label, font = ("Courier New", 13 , "bold"),
                 bg = "#1a1a2e", fg = "#e0e0ff").pack(pady = (0,0))
        
        self.canvas_size = 220
        self.cx = self. cy = self.canvas // 2
        self.cv = tk.Canvas(self, width = self.canvas.size, height = self.canvas_size,
                            bg = "#0d0d1a", highlightthickness = 2,
                            highlightbackground = "#3a3a6e")
        self.cv.pack()

        ctrl = tk.Frame(self, bg = "#1a1a2e")
        ctrl.pack(pady = 10, fill = "x")
        self._build_controls(ctrl)

        self.status_1b1 = tk.Label(self, font = ("Courier New", 8),
                                   bg = "#1a1a2e", fg = "#555588")
        self.status_1b1.pack(pady = (6,0))

        self._refresh_button()
        self._draw_fan()
        if fan_class.isOn():
            self._animate()


