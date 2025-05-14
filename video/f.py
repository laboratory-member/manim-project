from manim import *

class Show(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # 坐标轴
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=8,
            y_length=8,
            z_length=5,
        ).move_to([0,0,-1.5])
        def real_part(u, v):
            if (u==0 and v ==0):
                return 0
            z = complex(u, v)
            fz = np.log(z)-z
            return fz.real

        # 曲面
        surface = Surface(
            lambda u, v: axes.c2p(u, v, real_part(u, v)),
            u_range=[-1.5, 2.5],
            v_range=[-2.5, 2],
            resolution=(101, 101),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_A, BLUE_D],
        )

        dot = Dot3D(point=ORIGIN, color=RED).scale(0.7).move_to([1,0,-2.4])
        self.play(Create(axes))
        self.play(Create(surface),run_time=3)
        self.play(FadeIn(dot))

        self.wait(2)

        curve1 = ParametricFunction(
            lambda t: axes.c2p(t, 0,real_part(t,0) ),  # (x, y, z)
            t_range=[0.1, 2],
            color=ORANGE
        )
        self.play(Create(curve1))
        self.wait(3)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        self.play(FadeOut(*self.mobjects))



