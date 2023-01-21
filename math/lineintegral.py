from manim import *

#config.background_color= WHITE

class so(Scene):
    def construct(self):
        tex = Text("Properties of Ferromagnetic Substances", color= BLACK).to_edge(UP)
        Axes.set_default(color= BLACK)
        axes = Axes(color= BLACK).add_coordinates(font_size= 30, color= BLACK)


        #Line.set_default(color= BLACK)
        line1 = Line(start= axes.c2p(0,0), end= axes.c2p(0,2))
        line2 = Line(start= axes.c2p(0,2), end= axes.c2p(1.5,2))
        line3 = Line(start= axes.c2p(0,1), end= axes.c2p(1,-2))
        line4 = Line(start= axes.c2p(1,-2), end= axes.c2p(2,-2))
        line5 = Line(start= axes.c2p(2,-2), end= axes.c2p(3,-1.5))
        line6 = Line(start= axes.c2p(3,-1.5), end= axes.c2p(3.5,0))
        line7 = Line(start= axes.c2p(3.5,0), end= axes.c2p(2.8,2))
        line8 = Line(start= axes.c2p(0,2), end= axes.c2p(-2,2))
        line9 = Line(start= axes.c2p(0,2), end= axes.c2p(-1,1))
        line10 = Line(start= axes.c2p(-1,1), end= axes.c2p(-1,-1))
        line11 = Line(start= axes.c2p(0,0), end= axes.c2p(-1,-1))
        line12 = Line(start= axes.c2p(-1,-1), end= axes.c2p(-2,-2))
        line13 = Line(start= axes.c2p(1.5,2), end= axes.c2p(1,0))
        line14 = Line(start= axes.c2p(1,0), end= axes.c2p(1,-2))
        line15 = Line(start= axes.c2p(1.5,2), end= axes.c2p(2,0))
        line16 = Line(start= axes.c2p(2,0), end= axes.c2p(2,-2))
        line17 = Line(start= axes.c2p(1.5,2), end= axes.c2p(2.8,2))
        line18 = Line(start= axes.c2p(-2,-2), end= axes.c2p(1,-2))
        line19 = Line(start= axes.c2p(-1,1), end= axes.c2p(-2,2))
        line20 = Line(start= axes.c2p(-2,2), end= axes.c2p(-2,-2))
        line21 = Line(start= axes.c2p(-2,0), end= axes.c2p(3.5,0))
        line22 = Line(start= axes.c2p(-1,-1), end= axes.c2p(2,-1))


        lines = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22)

        self.add(axes, lines)