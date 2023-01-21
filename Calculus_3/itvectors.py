from manim import *


class vectors(Scene):
    def construct(self):

        Tex.set_default(font_size= 30)
        title = Tex("Introduction to Vectors", font_size= 35).to_edge(UP)
        vector_def = Tex("Vectors have both speed (magnitude) and a direction.").next_to(title, DOWN)
        
        ex = Tex("Exercise").shift(LEFT * 5 + UP * 2)
        axes = Axes(
            x_range= [-2,2],
            y_range= [-2,2],
            x_length= 4,
            y_length= 4,
            x_axis_config= {
                "include_tip": False
            },
            y_axis_config= {
                "include_tip": False
            }
        ).shift(LEFT * 2)

        pointA, pointB = Point(axes.c2p(-1,-1)), Point(axes.c2p(1,1))
        pointC, pointD = Point(axes.c2p(2,1)), Point(axes.c2p(3,-1))

        A, B, C, D = Dot(point= axes.c2p(-1,-1)), Dot(point= axes.c2p(1,1)), Dot(point= axes.c2p(2,1)), Dot(point= axes.c2p(3,-1))
        AB = Line(start= pointA, end= pointB, color= RED)
        CD = Line(start= pointC, end= pointD).add_tip(tip_length= 0.1)

        #self.add(title, vector_def, ex, axes, A, B, C, D, AB, CD)
        self.play(Write(title))
        self.wait(2)
        self.play(Write(vector_def))
        self.wait(2)
        self.play(Write(ex))
        self.wait(2)
        self.play(Create(
            VGroup(A, B)
            ))
        self.wait(2)
        self.play(Create(AB))
        self.wait(2)
        self.play(AB.animate.add_tip(), run_time= 2)
        self.wait(2)
        self.play(Create(
            VGroup(C, D)
            ))
        self.wait(2)
        self.play(Create(CD))
        self.wait(2)