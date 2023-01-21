from manim import *

class circle(Scene):
    def construct(self):
        axes = Axes().add_coordinates()

        self.add(axes)
        x = [1,
            np.sqrt(3)/2,
            1/np.sqrt(2),
            1/2,
            0,
            -1/2,
            -1/np.sqrt(2),
            -np.sqrt(3)/2,
            -1
        ]
        y = [0,
            1/2,
            1/np.sqrt(2),
            np.sqrt(3)/2,
            1,
            np.sqrt(3)/2,
            1/np.sqrt(2),
            1/2,
            0
        ]
        for i in range(0,len(x)):
            x.append(-x[i])
        for i in range(0,len(y)):
            y.append(-y[i])
        # for i in np.linspace(-1,1,20):
        #     for j in np.linspace(-1,1,20):
        #         if i**2 + j**2 >= 1:
        #             self.play(
        #                 Create(
        #                     Dot(point= axes.c2p(i,j), color= BLUE).scale(0.5)
        #                     )
        #                 )
        #         elif i**2 + j**2 <= 1:
        #             self.play(
        #                 Create(
        #                     Dot(point= axes.c2p(i,j), color= YELLOW).scale(0.5)
        #                     )
        #                 )
        for i in range(0,len(x)):
            self.play(Create(Dot(axes.c2p(x[i], y[i]))))

        circle = ParametricFunction(
            lambda t: axes.c2p(
                np.cos(t), np.sin(t)
            ),
            t_range= [0,2*PI]
        )

        self.add(circle)
        self.wait(2)