from manim import *

class color(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        Dot3D.set_default(color= YELLOW)
        dot =  Dot3D(axes.c2p(1,1,1))

        self.add(dot)
        self.play(AnimationGroup(
            Rotate(dot, angle= 2*PI, about_point= axes.c2p(0,0,0))
        ), run_time= 3)
        self.play(dot.animate.set_color(color= RED), run_time= 2)
        self.wait(2)