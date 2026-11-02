import math
import tkinter as tk
from tkinter import ttk

class Link:
    def __init__(self, length, angle=0.0):
        self.length = length
        self.angle = angle

class Manipulator:
    def __init__(self, link1, link2):
        self.link1, self.link2 = link1, link2

    def forward_kinematics(self):
        r1, r2 = math.radians(self.link1.angle), math.radians(self.link1.angle + self.link2.angle)
        x1, y1 = self.link1.length * math.cos(r1), self.link1.length * math.sin(r1)
        return x1, y1, x1 + self.link2.length * math.cos(r2), y1 + self.link2.length * math.sin(r2)

    def __str__(self):
        _, _, x2, y2 = self.forward_kinematics()
        return f"Схват: X={x2:.2f} м, Y={y2:.2f} м"

class PlanarArm(Manipulator):
    def __init__(self, link1, link2):
        super().__init__(link1, link2)

    @property
    def angle1(self): return self.link1.angle
    @angle1.setter
    def angle1(self, val): self.link1.angle = val

    @property
    def angle2(self): return self.link2.angle
    @angle2.setter
    def angle2(self, val): self.link2.angle = val

class ManipulatorApp(tk.Tk):
    SCALE, SIZE = 80, 400

    def __init__(self, arm):
        super().__init__()
        self.arm = arm
        self.title("Манипулятор")
        self.resizable(False, False)
        
        self.a1_var = tk.DoubleVar(value=arm.angle1)
        self.a2_var = tk.DoubleVar(value=arm.angle2)
        self.info = tk.StringVar()

        self.canvas = tk.Canvas(self, width=self.SIZE, height=self.SIZE, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        panel = ttk.LabelFrame(self, text="Суставы")
        panel.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        for text, var, cmd, ticks in [
            ("Звено 1 (±180°):", self.a1_var, self._on_a1, "-180°    0°    180°"),
            ("Звено 2 (±180°):", self.a2_var, self._on_a2, "-180°    0°    180°")
        ]:
            ttk.Label(panel, text=text).pack(anchor="w", padx=5)
            ttk.Scale(panel, from_=-180, to=180, variable=var, command=cmd).pack(fill="x", padx=5)
            ttk.Label(panel, text=ticks, font=("Consolas", 8), foreground="#777").pack(pady=(0, 5))

        ttk.Button(panel, text="Сброс", command=self._reset).pack(fill="x", padx=5, pady=10)
        ttk.Label(self, textvariable=self.info, font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=2, pady=5)
        self._redraw()

    def _on_a1(self, v): self.arm.angle1 = float(v); self._redraw()
    def _on_a2(self, v): self.arm.angle2 = float(v); self._redraw()

    def _reset(self):
        for var, arm_attr in [(self.a1_var, "angle1"), (self.a2_var, "angle2")]:
            var.set(0.0)
            setattr(self.arm, arm_attr, 0.0)
        self._redraw()

    def _px(self, x, y):
        c = self.SIZE / 2
        return c + x * self.SCALE, c - y * self.SCALE

    def _redraw(self):
        self.canvas.delete("all")
        x1, y1, x2, y2 = self.arm.forward_kinematics()
        p0, p1, p2 = self._px(0, 0), self._px(x1, y1), self._px(x2, y2)

        self.canvas.create_line(0, self.SIZE/2, self.SIZE, self.SIZE/2, fill="#eee")
        self.canvas.create_line(self.SIZE/2, 0, self.SIZE/2, self.SIZE, fill="#eee")
        
        self.canvas.create_line(*p0, *p1, width=6, fill="blue", capstyle="round")
        self.canvas.create_line(*p1, *p2, width=4, fill="green", capstyle="round")

        for p, color, r in [(p0, "red", 6), (p1, "black", 5), (p2, "magenta", 4)]:
            self.canvas.create_oval(p[0]-r, p[1]-r, p[0]+r, p[1]+r, fill=color)

        self.info.set(f"{self.arm} | Углы: {self.arm.angle1:.1f}°, {self.arm.angle2:.1f}°")

def main():
    ManipulatorApp(PlanarArm(Link(1.3), Link(1.0))).mainloop()

if __name__ == "__main__":
    main()
