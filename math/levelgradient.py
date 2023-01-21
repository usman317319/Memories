from manim import *
import math
import manim as numpy

class fun(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(lambda u, v: axes.c2p(
            u, v, math.log(u**2 + v**2)
        ) if not u == v == 0 else ORIGIN,
        u_range= [-TAU, TAU], v_range= [-TAU, TAU], color= WHITE, fill_opacity= 0.5)
        levelcurve = ParametricFunction(lambda u: axes.c2p(
            1.2190 * np.cos(u), 1.2190 * np.sin(u)
        ), t_range= [-TAU, TAU])
        vector = Line(start=axes.c2p(1,1), end= axes.c2p(2,2)).add_tip(tip_length= 0.1)
        

        self.set_camera_orientation(phi= PI/4, theta= PI/4)
        self.add(axes, surface, levelcurve, vector)
        self.begin_ambient_camera_rotation(rate= 0.9)
        self.wait(5)
        