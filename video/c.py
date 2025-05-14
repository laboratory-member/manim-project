from manim import *

class Compare(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # 实部坐标轴（左）
        axes_re = ThreeDAxes().scale(0.5).move_to([3,0,0])
        surface_re = Surface(
            lambda u, v: axes_re.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        ).scale(0.8)

        # 虚部坐标轴（右）
        axes_im = ThreeDAxes().scale(0.5).move_to([0,3,0])
        surface_im = Surface(
            lambda u, v: axes_im.c2p(u, v,  u * v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[GREEN_D, GREEN_E],
        ).scale(0.8)

        # 添加
        self.play(Create(axes_im),Create(axes_re))
        self.play(Create(surface_im),Create(surface_re),run_time=3)
        self.wait(2)

        # 实部上的 x=0 曲线（Re(z^2) = -y^2）
        line_re = ParametricFunction(
            lambda t: axes_re.c2p(0, t, -t**2),
            t_range=[-2, 2],
            color=RED,
            stroke_width=4,
        )

        # 虚部上的 x=0 曲线（Im(z^2) = 0）
        line_im = ParametricFunction(
            lambda t: axes_im.c2p(0, t, 0),
            t_range=[-2, 2],
            color=RED,
            stroke_width=4,
        )

        self.play(Create(line_re),Create(line_im))
        self.wait(2)
        self.move_camera(phi=30 * DEGREES, theta=45 * DEGREES,run_time=6)
        self.wait(3)
        self.play(FadeOut(*self.mobjects))