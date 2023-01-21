from manim import *

class chemistry(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        #<<<<<< Defining the centeral molecule >>>>>>>
        dot1, dot2, dot3, dot4, dot5, dot6 = Dot3D(axes.c2p(0,0,0), color= BLUE), Dot3D(axes.c2p(0.3,0,0), color= BLUE), Dot3D(axes.c2p(-0.2,0,0.1), color= BLUE), Dot3D(axes.c2p(0,-0.1,0.2), color= BLUE), Dot3D(axes.c2p(-0.1,0.2,-0.1), color= BLUE), Dot3D(axes.c2p(0.1,0.1,0.1), color= BLUE)
        dots_blue = VGroup(dot1, dot2, dot3, dot4, dot5, dot6).scale(2.5)


       # Dot3D.set_default(color= RED)
        dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8  = Dot3D(axes.c2p(0,0.2,0), color= RED), Dot3D(axes.c2p(0,0,0.2), color= RED), Dot3D(axes.c2p(0.1,0,0), color= RED), Dot3D(axes.c2p(0,-0.1,0), color= RED), Dot3D(axes.c2p(-0.1,0,0), color= RED), Dot3D(axes.c2p(-0.1,-0.1,0.1), color= RED), Dot3D(axes.c2p(-0.1,-0.1,0.1), color= RED), Dot3D(axes.c2p(-0.1,0.1,0.1), color= RED)
        dots_red = VGroup(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8).scale(2.5)
        dots = VGroup(dots_blue, dots_red)        


        #<<<<<<< Electrons revolving around the molecule >>>>>>>>
        Dot3D.set_default(color= BLUE)
        electron1, electron2, electron3, electron4, electron5, electron6 = Dot3D(axes.c2p(0,0,0)), Dot3D(axes.c2p(0,0,0)), Dot3D(axes.c2p(0,0,0)), Dot3D(axes.c2p(0,0,0)),Dot3D(axes.c2p(0,0,0)), Dot3D(axes.c2p(0,0,0))


        #<<<<<<< Poping new yellow points >>>>>>>
        dot_y_1, dot_y_2 = Dot3D(axes.c2p(0,-0.05,0.3), color= YELLOW), Dot3D(axes.c2p(0,-0.05,0.3), color= YELLOW)

        #<<<<<<< Setting camera for 3d scene >>>>>>>>>
        self.set_camera_orientation(phi= 1.2, theta= 0.16, zoom= 2)
        self.add(dots, dot8, dot_y_1, dot_y_2)
        

        #Electrons are evenly distributed over a circle of radius 3 and center as origin
        #The revolve around the circle
        self.play(
            AnimationGroup(
            Rotate(electron1.shift(RIGHT * 3 + UP * 0), angle= 2*PI, about_point= ORIGIN),
            Rotate(electron2.shift(RIGHT * (3/2) + UP * 3*(3**(1/3))/2 ), angle= 2*PI, about_point= ORIGIN),
            Rotate(electron3.shift(RIGHT * (-3/2) + UP * 3*(3**(1/3))/2 ), angle= 2*PI, about_point= ORIGIN),
            Rotate(electron4.shift(RIGHT *  (-3) + UP * 0), angle= 2*PI, about_point= ORIGIN),
            Rotate(electron5.shift(RIGHT * (-3/2) + UP * 3*(-3**(1/3))/2 ), angle= 2*PI, about_point= ORIGIN),
            Rotate(electron6.shift( RIGHT * (3/2) + UP * 3*(-3**(1/3))/2 ), angle= 2*PI, about_point= ORIGIN),
            dot2.animate.set_color(color= BLUE)
            ), run_time= 5)

        
        #self.play(dot2.animate.set_color(color= BLUE))

        self.wait(2)
        self.play(
            AnimationGroup(
            Rotate(electron1, angle= 2*PI, about_point= ORIGIN),
            Rotate(electron2, angle= 2*PI, about_point= ORIGIN),
            Rotate(electron3, angle= 2*PI, about_point= ORIGIN),
            Rotate(electron4, angle= 2*PI, about_point= ORIGIN),
            Rotate(electron5, angle= 2*PI, about_point= ORIGIN),
            Rotate(electron6, angle= 2*PI, about_point= ORIGIN),
            dot_y_1.animate.shift(axes.c2p(0,-2,4)),
            dot_y_2.animate.shift(axes.c2p(0,2,4))
            ), run_time= 5)