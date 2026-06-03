import tkinter as tk
from fan_class import Fan
from fan_widget import FanWidget


def main():

    fan1 = Fan()
    fan1.setSpeed(Fan.FAST)
    fan1.setRadius(10)
    fan1.setColor("yellow")
    fan1.setOn(True)

    fan2 = Fan()
    fan2.setSpeed(Fan.MEDIUM)
    fan2.setRadius(5)
    fan2.setColor("blue")
    fan2.setOn(False)

    root = tk.Tk()
    root.title("Fan Simulator")
    root.configure(bg="#12122a")
    root.resizable(False, False)

    tk.Label(root, text="⚙  FAN SIMULATOR",
             font=("Courier New", 16, "bold"),
             bg="#12122a", fg="#aaaaff").pack(pady=(18, 4))
    tk.Label(root, text="Encapsulation & Abstraction in action",
             font=("Courier New", 8),
             bg="#12122a", fg="#444466").pack(pady=(0, 12))

    container = tk.Frame(root, bg="#12122a")
    container.pack(padx=20, pady=(0, 20))

    FanWidget(container, fan1, "Fan 1  —  FAST / Yellow").grid(row=0, column=0, padx=12)
    FanWidget(container, fan2, "Fan 2  —  MEDIUM / Blue").grid(row=0, column=1, padx=12)

    root.mainloop()


if __name__ == "__main__":
    main()