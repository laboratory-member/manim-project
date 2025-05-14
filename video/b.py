from manim import *

class Complex(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        # 坐标轴
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-3, 3, 1],
            z_range=[-50, 50, 5],
            x_length=8,
            y_length=8,
            z_length=6,
        ).move_to([0,0,-1.5])
        def real_part(u, v):
            z = complex(u, v)
            fz = 0.05*z**5+5*z**2-1
            return fz.real

        # 曲面
        surface = Surface(
            lambda u, v: axes.c2p(u, v, real_part(u, v)),
            u_range=[-2.5, 3],
            v_range=[-3, 3],
            resolution=(101, 101),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_A, BLUE_D],
        )
        surface_frame = surface.copy().set_fill(color=BLUE,opacity=0)

        self.play(Create(axes))
        self.play(Create(surface),run_time=3)
        self.play(Transform(surface,surface_frame),run_time=3)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(3)

        a = ValueTracker(0.4)  # 可调参数 a

        def get_curve():
            return ParametricFunction(
                lambda t: axes.c2p(
                    a.get_value() * (t**2 - 4),  # x = a(y^2 + 4)
                    t,  # y
                    real_part(a.get_value() * (t**2 - 4),t)
                ),
                t_range=[-2, 2],
                color=YELLOW,
            )

        curve = always_redraw(get_curve)
        self.play(Create(curve))
        self.play(a.animate.set_value(-0.4), run_time=4)
        self.wait(2)

        dot = Dot3D(point=ORIGIN, color=RED).scale(0.7).move_to([0,0,-1.5])
        self.play(FadeIn(dot))
        self.play(a.animate.set_value(0), run_time=3)
        self.wait(2)

        curve1 = ParametricFunction(
            lambda t: axes.c2p(0.6*t * (t - 2) * (t + 2), t,real_part(0.6*t * (t - 2) * (t + 2),t) ),  # (x, y, z)
            t_range=[-2, 2],
            color=ORANGE
        )
        self.play(Create(curve1))
        self.wait(3)
        self.play(Uncreate(curve),Uncreate(curve1))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))



