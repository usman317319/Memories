from manim import *


class circle(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(PINK, opacity= 0.5)

        self.play(Create(circle), run_time= 3)
        self.wait(1)