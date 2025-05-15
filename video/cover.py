from manim import *
import numpy as np

class Example(Scene):
    def construct(self):
        
        text0 = Text("Laplace方法？鞍点近似？",font_size=48,t2c={"Laplace方法":RED,"鞍点近似":BLUE}).shift(UP*2)

                # 定义函数 g_n(x) 和 T_n(x)
        def g_n(x, n):
            return np.exp(n * (np.log(x) - x))

        def T_n(x, n):
            return np.exp(n * (-1 - 0.5 * (x - 1)**2))

        # 创建左图：n=1
        axes_left = Axes(
            x_range=[0.1, 2.5, 0.5],
            y_range=[0, 0.5],
            x_length=3,
            y_length=3,
            tips=False,
        ).shift(LEFT * 4)

        g1 = axes_left.plot(lambda x: g_n(x, 1), color=BLUE)
        t1 = axes_left.plot(lambda x: T_n(x, 1), color=RED)
        dot1 = Dot(axes_left.coords_to_point(1, g_n(1, 1)), color=YELLOW)

        label1 = Text("n = 1").next_to(axes_left, DOWN)

        # 创建中图：n=10
        axes_middle = Axes(
            x_range=[0.1, 2.5, 0.5],
            y_range=[0, 0.000065],
            x_length=3,
            y_length=3,
            tips=False,
        )

        g10 = axes_middle.plot(lambda x: g_n(x, 10), color=BLUE)
        t10 = axes_middle.plot(lambda x: T_n(x, 10), color=RED)
        dot10 = Dot(axes_middle.coords_to_point(1, g_n(1, 10)), color=YELLOW)

        label10 = Text("n = 10").next_to(axes_middle, DOWN)

        # 创建右图：n=20
        axes_right = Axes(
            x_range=[0.1, 2.5, 0.5],
            y_range=[0, 3e-9],
            x_length=3,
            y_length=3,
            tips=False,
        ).shift(RIGHT * 4)

        g20 = axes_right.plot(lambda x: g_n(x, 20), color=BLUE)
        t20 = axes_right.plot(lambda x: T_n(x, 20), color=RED)
        dot20 = Dot(axes_right.coords_to_point(1, g_n(1, 20)), color=YELLOW)

        label20 = Text("n = 20").next_to(axes_right,DOWN)

        self.add(
            text0,
            axes_left, g1, t1, dot1, label1,
            axes_middle, g10, t10, dot10, label10,
            axes_right, g20, t20, dot20, label20
        )
        self.wait(3)

