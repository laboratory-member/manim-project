from manim import *
import numpy as np

class Laplace(Scene):
    def construct(self):
        text1 = Text("相信你对Taylor展开一定不陌生", font_size=36)
        self.wait(1)
        self.play(FadeIn(text1))
        self.play(text1.animate.shift(UP*1.5))
        formula1 = MathTex(
            r"f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x - a)^n + \cdots",
            font_size=36
        )
        self.play(Write(formula1))
        self.wait(1)
        text2 = Text("现在试着只取到二阶", font_size=36)
        text2.shift(UP*1.5)
        formula2 = MathTex(
            r"f_2(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 ",
            font_size=36
        )
        self.play(Transform(text1,text2),Transform(formula1,formula2))
        self.wait(2)
        text3 = Text("看个具体例子", font_size=36)
        text3.shift(UP*3)
        self.play(FadeOut(formula1),Transform(text1,text3))

        self.wait(0.5)

        formula3 = MathTex(
            r"f(x)=\frac{\ln(x)}{x}",
            font_size=36,
            color=BLUE_A
        )
        formula3.next_to(text3,DOWN,buff=0.3)
        formula4 = MathTex(
            r"f_2(x)=\frac{1}{e}-\frac{1}{2e^3}(x-e)^2",
            font_size=36,
            color=BLUE_B
        )
        formula4.next_to(formula3,DOWN,buff=0.15)
        self.play(Write(formula3))

        axes = Axes(
            x_range=[-1, 5],
            y_range=[-2, 2],
            axis_config={"unit_size": 1}
        )
        axes.shift(DOWN * 1,LEFT*1)  # 把坐标轴整体向下移动
        self.play(FadeIn(axes))

        graph1 = axes.plot(
            lambda x: np.log(x)/x,
            x_range=[0.1, 5],
            color=BLUE_A,
            stroke_width=3
        )
        graph_label1 = axes.get_graph_label(graph1, label="f(x)")
        graph_label1.shift(UP*0.3)
        self.play(Create(graph1), Write(graph_label1))

        self.wait(2)
        text4 = Text("在x=e处进行二阶的Taylor展开", font_size=36)
        text4.shift(UP*3)
        self.play(Transform(text1,text4))

        self.play(Write(formula4))
        graph2 = axes.plot(
            lambda x: 1/np.e-1/(2*np.e**3)*(x-np.e)**2,
            x_range=[0.1, 5],
            color=BLUE_B,
            stroke_width=3
        )
        graph_label2 = axes.get_graph_label(graph2, label="f_2(x)")
        graph_label2.shift(DOWN*0.3)

        point = Dot(axes.c2p(np.e, 1/np.e), color=PURPLE)
        pointlabel = MathTex(r"(e, \frac{1}{e})").scale(0.8).next_to(point, UP,buff=0.1)

        self.play(FadeIn(point), Write(pointlabel))
        self.play(Create(graph2), Write(graph_label2))
        self.wait(1)
        text5 = Text("可以看到在x=e附近有不错的拟合效果", font_size=36).shift(UP*3)
        self.play(Transform(text1,text5))
        self.wait(1)

        text6 = Text("现在我们进行一些有趣的操作", font_size=36).shift(UP*3+RIGHT*3.5)
        self.play(Transform(text1,text6),VGroup(formula3,formula4).animate.shift(RIGHT*3.5),VGroup(axes,graph1,graph2,graph_label1,graph_label2,point,pointlabel)
                  .animate.scale(0.6).shift(LEFT*3+UP*7))
        self.wait(2)

        text7 = Text("构造g(x)=exp(f(x))", font_size=36).shift(UP*3+RIGHT*3.5)
        self.play(Transform(text1,text7))
        self.wait(1)
        formula5 = MathTex(
            r"g(x)=e^{f(x)}",
            font_size=36,
            color=ORANGE
        ).next_to(formula4,DOWN,buff=0.15)
        formula6 = MathTex(
            r"g_2(x)=e^{f_2(x)}",
            font_size=36,
            color=YELLOW_A
        ).next_to(formula5,DOWN,buff=0.15)
        axes1 = Axes(
            x_range=[-1, 10],
            y_range=[-2, 2],
            axis_config={"unit_size": 1}
        ).scale(0.6).shift(LEFT*3.2,DOWN*0.3)

        lambda_tracker = ValueTracker(1)
        graph3 = always_redraw(lambda: axes1.plot(
            lambda x: np.exp(lambda_tracker.get_value() * (np.log(x)/x)),
            x_range=[0.1, 10],
            color=ORANGE,
            stroke_width=3
        ))

        graph4 = always_redraw(lambda: axes1.plot(
            lambda x: np.exp(lambda_tracker.get_value() * (1/np.e - 1/(2*np.e**3)*(x-np.e)**2)),
            x_range=[0.1, 10],
            color=YELLOW_A,
            stroke_width=3
        ))

        self.play(Write(formula5),Write(formula6),FadeOut(axes,graph1,graph2,graph_label1,graph_label2,point,pointlabel),
                  Create(VGroup(axes1,graph3,graph4)),run_time=2)
        self.wait(2)

        text8 = Text("可以发现在指数函数的作用下放大了极大值的效果，\n而同时减弱了其他值的效果", font_size=36).shift(UP*3+RIGHT*1)
        self.play(Transform(text1,text8))
        self.wait(2)
        text9 = Text("为了放大这个效应，我们引入参数λ，\n同时来计算定积分I1和I2", font_size=36,
                     t2c={"I1": ORANGE, "I2":YELLOW_A}).shift(UP*3+RIGHT*0.5)
        text10 = Text("可以看到当λ增大，\nI1/I2将逐渐向1收敛", font_size=36,
                     t2c={"I1": ORANGE, "I2":YELLOW_A}).scale(0.8).shift(UP*3.2+RIGHT*3.5)
        formula7 = MathTex(
            r"g(x)=e^{\lambda f(x)}",
            font_size=36,
            color=ORANGE
        ).next_to(formula4,DOWN,buff=0.15)
        formula8 = MathTex(
            r"g_2(x)=e^{\lambda f_2(x)}",
            font_size=36,
            color=YELLOW_A
        ).next_to(formula5,DOWN,buff=0.15)
        self.play(Transform(text1,text9),Transform(formula5,formula7),Transform(formula6,formula8))

        bar_axis = NumberLine(
            x_range=[1, 25, 1],   # λ 的范围，起始值到终止值之间的步长为 1
            length=4,              # 长度
            color=WHITE,
            include_numbers=False,  # 仅显示起始和终止的数值
            label_direction=DOWN,  # 数值标签的方向
            numbers_with_elongated_ticks=[1, 25],  # 仅在起始值和终止值位置显示刻度
        )
        bar_axis.next_to(axes1,DOWN).shift(UP*1.3+RIGHT*2) 
        dot = always_redraw(lambda: Dot(
            point=bar_axis.n2p(lambda_tracker.get_value()),  # 更新位置
            color=YELLOW,
            radius=0.1  # 圆点大小
        ))
        lambda_label = always_redraw(lambda: MathTex(
            r"\lambda = {:.2f}".format(lambda_tracker.get_value()), 
            font_size=36,
            color=YELLOW
        ).next_to(dot, DOWN))  # λ 数值显示在圆点下方

        formula9 = always_redraw(lambda: MathTex(
            r"I_1 = \displaystyle \int_0^{{10}} e^{{\lambda f(x)}} dx \approx {:.2f}".format(
                np.trapz(
                    [np.exp(lambda_tracker.get_value() * (np.log(x)/x)) for x in np.linspace(0.1, 10, 200)],
                    x=np.linspace(0.1, 10, 200)
                )
            ), font_size=36, color=ORANGE
        ).next_to(axes1, DOWN, buff=0.2))

        formula10 = always_redraw(lambda: MathTex(
            r"I_2 =\displaystyle \int_0^{{10}} e^{{\lambda f_2(x)}}dx \approx {:.2f}".format(
                np.trapz(
                    [np.exp(lambda_tracker.get_value() * (1/np.e - 1/(2*np.e**3)*(x-np.e)**2)) for x in np.linspace(0.1, 10, 200)],
                    x=np.linspace(0.1, 10, 200)
                )
            ), font_size=36, color=YELLOW_A
        ).next_to(formula9, RIGHT, buff=2))
        formula11 = always_redraw(lambda: (
            m := MathTex(
                r"\frac{{I_1}}{{I_2}} \approx {:.2f}".format(
                    np.trapz(
                        [np.exp(lambda_tracker.get_value() * (np.log(x)/x)) for x in np.linspace(0.1, 10, 200)],
                        x=np.linspace(0.1, 10, 200)
                    ) / np.trapz(
                        [np.exp(lambda_tracker.get_value() * (1/np.e - 1/(2*np.e**3)*(x-np.e)**2)) for x in np.linspace(0.1, 10, 200)],
                        x=np.linspace(0.1, 10, 200)
                    )
                ),
                font_size=36,
            ).next_to(bar_axis, RIGHT, buff=1.5)
        )).add_updater(lambda m: (
            m[0][0:2].set_color(ORANGE),
            m[0][3:5].set_color(YELLOW_A)
        ))
        self.play(FadeIn(dot), FadeIn(lambda_label), Create(bar_axis),Write(formula9),Write(formula10),Write(formula11))
        self.wait(2)
        self.play(Transform(text1,text10))
        self.play(lambda_tracker.animate.set_value(25), run_time=8, rate_func=linear)
        self.wait(1)

        text11 = Text("不妨记录一下I1/I2随λ的变化趋势", font_size=32,
                     t2c={"I1": ORANGE, "I2":YELLOW_A}).shift(UP*3)
        axes2 = Axes(
            x_range=[1, 100, 10],
            y_range=[0, 1.5, 0.25],
            x_length=8,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).next_to(text11,DOWN,buff=2)

        x_label = axes2.get_x_axis_label(Tex(r"$\lambda$"))
        y_label = axes2.get_y_axis_label(Tex(r"$I_1 / I_2$"))

        lambdas = np.linspace(1, 50, 500)
        I1 = lambda l: np.trapz([np.exp(l * (np.log(x)/x)) for x in np.linspace(0.1, 10, 300)], dx=0.03)
        I2 = lambda l: np.trapz([np.exp(l * (1/np.e - 1/(2*np.e**3)*(x-np.e)**2)) for x in np.linspace(0.1, 10, 300)], dx=0.03)
        ratio_values = [I1(l) / I2(l) for l in lambdas]

        # 绘制图像
        graph5 = axes2.plot_line_graph(
            x_values=lambdas,
            y_values=ratio_values,
            line_color=RED,
            add_vertex_dots=False
        )
        self.play(FadeOut(*self.mobjects))
        self.play(Write(text11))
        self.play(FadeIn(axes2), Write(x_label), Write(y_label),Create(graph5), run_time=2)
        self.wait(2)

        text12 = Text("可以看出I1与I2在λ增大时趋于相同，\n不难理解这是由于当λ很大时，由于指数函数的性质，\n积分的主要贡献来源于极值点附近区域。", font_size=32,
                     t2c={"I1": ORANGE, "I2":YELLOW_A}).shift(UP*3)
        self.play(Transform(text11,text12))
        self.wait(3)
        text13 = Text("受到这个思路影响，我们考虑如下形式的积分", font_size=32).shift(UP*3)
        formula12 =MathTex(
            r"I(\lambda) = \displaystyle \int_{-\infty}^{\infty} e^{\lambda f(x)} dx",
            font_size=40,
            color=BLUE_A
        )
        self.play(Transform(text11,text13),FadeOut(axes2,graph5,x_label,y_label))
        self.play(Write(formula12))
        self.wait(2)

        text13 = Text("当λ足够大时，对f(x)在最大值点x=a处泰勒只要展开到二阶，\n我们就可以近似认为下式成立", font_size=32).shift(UP*3)
        formula13 =MathTex(
            r"I(\lambda) = \displaystyle \int_{-\infty}^{\infty} e^{\lambda f(x)} dx \approx  \int_{-\infty}^{\infty} e^{\lambda (f(a) + \frac{f''(a)}{2!}(x - a)^2)}",
            font_size=40,
            color=BLUE_A
        )
        self.play(Transform(text11,text13))
        self.play(Transform(formula12,formula13))
        self.wait(2)
        text14 = Text("接着利用Gauss型积分的结论，化简式子", font_size=32).shift(UP*3)
        formula14 =MathTex(
            r"I(\lambda) \approx \displaystyle e^{\lambda f(a)} \int_{-\infty}^{\infty} e^{\frac{f''(a)}{2!}(x - a)^2} ",
            font_size=40,
            color=BLUE_A
        ).shift(UP*1.5)
        formula15 =MathTex(
            r"\displaystyle \int_{-\infty}^{\infty} e^{-a(x-x_0)^2} dx = \sqrt{\frac{\pi}{a}} ",
            font_size=40,
            color=BLUE_A
        )
        formula16 =MathTex(
            r"I(\lambda) \approx \displaystyle e^{\lambda f(a)} \sqrt{\frac{2\pi}{-\lambda f''(a)}}",
            font_size=40,
            color=BLUE_A
        ).shift(DOWN*1.5)
        rect = SurroundingRectangle(formula16, color=YELLOW_A, buff=0.2)
        path = VMobject()
        path.set_points_as_corners([
            rect.get_corner(UL),
            rect.get_corner(UR),
            rect.get_corner(DR),
            rect.get_corner(DL),
            rect.get_corner(UL), 
        ])
        path.set_stroke(width=4)

        self.play(Transform(formula12,formula14))
        self.play(Transform(text11,text14))
        self.play(Write(formula15))
        self.play(Write(formula16))
        self.play(ShowPassingFlash(path, time_width=0.3, run_time=3))
        self.wait(1)

        text17 = Text("我们可以简单讨论一些误差分析，不难猜想，\n误差主要来源于我们的二阶展开近似", font_size=30).shift(UP*3+LEFT*2)
        formula18 =MathTex(
            r"f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f^{(3)}(a)}{3!}(x - a)^3 + \frac{f^{(4)}(a)}{4!}(x - a)^4 + \cdots",
            font_size=32,
            color=RED_A
        ).shift(UP*1.5)
        formula19 =MathTex(
            r"I(\lambda) \approx \displaystyle \int_{-\infty}^{\infty}e^{\lambda (f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f^{(3)}(a)}{3!}(x - a)^3 + \frac{f^{(4)}(a)}{4!}(x - a)^4)}dx",
            font_size=36,
            color=RED_A
        )
        self.play(Transform(text11,text17),FadeOut(formula12,formula15),VGroup(rect,formula16).animate.to_corner(UR).scale(0.8))
        self.play(Write(formula18))
        self.wait(1)
        self.play(Write(formula19))
        self.wait(1)

        text17 = Text("当三阶导不为0，则可能引入误差", font_size=32).shift(DOWN*1+LEFT*1)
        formula20 =MathTex(
            r"O(\lambda^{-1})",
            font_size=36,
            color=RED_A
        ).next_to(text17,RIGHT)
        text18 = Text("当三阶导为0，则误差主要来自四阶项，贡献为", font_size=32).shift(DOWN*2+LEFT*1)
        formula21 =MathTex(
            r"O(\lambda^{-\frac{3}{2}})",
            font_size=36,
            color=RED_A
        ).next_to(text18,RIGHT)
        text18_ = Text("也就是说随着λ增大，相对误差会逐渐趋于0", font_size=32).shift(DOWN*3)
        self.play(FadeIn(text17,formula20))
        self.wait(1)
        self.play(FadeIn(text18,formula21))
        self.wait(1)
        self.play(Write(text18_))
        self.wait(3)

        text15 = Text("以上便是Laplace方法的核心思想，也有一些其他的表述形式如下", font_size=32).shift(UP*3)
        self.play(Transform(text11,text15),FadeOut(formula16,formula18,formula19,text17,text18,formula20,formula21,rect,text18_))
        formula17 =MathTex(
            r"I(\lambda) = \displaystyle \int_{-\infty}^{\infty} g(x) e^{\lambda f(x)} dx \approx g(a) \displaystyle e^{\lambda f(a)} \sqrt{\frac{2\pi}{-\lambda f''(a)}} ",
            font_size=40,
            color=BLUE_A
        ).next_to(text15,DOWN,buff=1.5)
        text16 = Text("不难看出，该式子的精确程度部分依赖于\ng(x)在x=a附近的变化程度", font_size=32).next_to(formula17,DOWN,buff=1.5)
        self.play(Write(formula17))
        self.wait(1)
        self.play(Write(text16))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        text19 = Text("那么，关于Laplace方法的讨论到此结束了吗？", font_size=32)
        text20 = Text("或许我们还可以稍稍扩展一下？", font_size=32)
        text21 = Text("比如………", font_size=32)
        text22 = Text("复数", font_size=32)
        self.play(Write(text19))
        self.wait(1)
        self.play(Transform(text19,text20))
        self.wait(1)
        self.play(Transform(text19,text21))
        self.wait(1)
        self.play(Transform(text19,text22))
        self.wait(1)
        self.play(FadeOut(text19))

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

class Saddle(Scene):
    def construct(self):
        text23 = Text("考虑这样一个复变积分，其中f(z)解析", font_size=32).shift(UP*3)
        formula22 = MathTex(
            r"I(\lambda) = \displaystyle \int_C e^{\lambda f(z)}dz",
            font_size=36,
            color=BLUE_A
        )
        self.play(Write(text23))
        self.play(Write(formula22))
        self.wait(1)
        self.play(formula22.animate.next_to(text23,DOWN))
        self.wait(4)
        text24 = Text("类似的，我们这里故技重施，在一阶导为0处进行展开", font_size=32).shift(UP*3)
        formula23 = MathTex(
            r"I(\lambda) = \displaystyle \int_C e^{\lambda f(z)}dz \approx \displaystyle \int_C e^{\lambda (f(z_0)+\frac{1}{2}(z-z_0)^2)}dz",
            font_size=36,
            color=BLUE_A
        ).next_to(text23,DOWN)
        text25 = Text("由于积分结果与路径C无关，我们有可能找到路径经过满足f'(z)=0的点", font_size=32).shift(UP*3)
        text25_ = Text("显然这样的路径并不唯一", font_size=32).shift(UP*3)
        text26 = Text("但为了使得原先的技巧能够用上，\n我们应该找到一条最“陡”的路线使得指数函数快速衰减", font_size=32).shift(UP*3.2)
        text27 = Text("因此接下来我们的目标是确定最速下降的方向，再进行高斯积分", font_size=32).shift(UP*3)
        self.play(Transform(text23,text24))
        self.play(Transform(formula22,formula23))
        self.wait(5)
        self.play(Transform(text23,text25))
        self.wait(10)
        self.play(Transform(text23,text25_))
        self.wait(3)
        self.play(Transform(text23,text26))
        formula24 = MathTex(
            r"f''(z_0)=|f''(z_0)|e^{i\alpha},z-z_0=|z-z_0|e^{i\beta}",
            font_size=36,
            color=BLUE_A
        ).next_to(formula23,DOWN)
        formula25 = MathTex(
            r"f(z)=f(z_0)+\frac{1}{2}|f''(z_0)|r^2 e^{i(\alpha+2\beta)}",
            font_size=36,
            color=BLUE_A,
        ).next_to(formula24,DOWN)
        formula25[0][28:32].set_color(YELLOW)
        text28 = Text("可见当 α + 2β = (2k + 1)π 时，高斯积分指数的实部\n下降最快，且虚部的贡献被消去。", font_size=32,
                      t2c={"α + 2β = (2k + 1)π":YELLOW}).shift(UP*3.3)
        text29 = Text("由此我们确定了最快下降的路线方向β", font_size=32).shift(UP*3)
        formula26 = MathTex(
            r"\beta = -\frac{arg(f''(z_0))}{2}+\pi \pm \frac{\pi}{2}",
            font_size=36,
            color=BLUE_A
        ).next_to(formula25,DOWN)
        self.wait(2.5)
        self.play(Transform(text23,text27))
        self.wait(1)
        self.play(Write(formula24))
        self.play(Write(formula25))
        self.wait(2)
        self.play(Transform(text23,text28))
        self.wait(2)
        self.play(Transform(text23,text29)) 
        self.play(Write(formula26))
        self.wait(2)
        text30 = Text("代入积分表达式", font_size=32).shift(UP*3)
        formula27 = MathTex(
            r"I(\lambda) = \displaystyle \int_C e^{\lambda f(z)}dz ",
            font_size=36,
            color=BLUE_A
        ).next_to(formula26,DOWN)
        formula28 = MathTex(
            r"I(\lambda) \approx \displaystyle \int_C e^{\lambda (f(z_0)+\frac{1}{2}|f''(z_0)|r^2 e^{i(\alpha+2\beta)}}dz",
            font_size=36,
            color=BLUE_A
        ).next_to(formula26,DOWN)
        formula29 = MathTex(
            r"I(\lambda) \approx e^{i\beta} e^{\lambda z_0} \sqrt{\frac{2\pi}{\lambda |f''(z_0)|}} ",
            font_size=36,
            color=BLUE_A
        ).next_to(formula26,DOWN)
        self.play(Transform(text23,text30))
        self.play(Write(formula27))
        self.play(Transform(formula27,formula28))
        self.play(Transform(formula27,formula29))
        rect = SurroundingRectangle(formula29, color=YELLOW_A, buff=0.2)
        path = VMobject()
        path.set_points_as_corners([
            rect.get_corner(UL),
            rect.get_corner(UR),
            rect.get_corner(DR),
            rect.get_corner(DL),
            rect.get_corner(UL), 
        ])
        path.set_stroke(width=4)
        self.play(ShowPassingFlash(path, time_width=0.3, run_time=3))
        self.play(FadeOut(formula22,formula24,formula25,formula26),VGroup(rect,formula27).animate.move_to(ORIGIN).scale(1.6))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        text31 = Text("举个小例子，令f(z)=z^2", font_size=32).shift(UP*3)
        formula30 = MathTex(
            r"\beta = -\frac{arg(f''(z_0))}{2}+\pi \pm \frac{\pi}{2}",
            font_size=36,
            color=BLUE_A
        ).next_to(text31,DOWN,buff=0.6)
        formula31 = MathTex(
            r"\beta = \frac{\pi}{2} or \frac{3\pi}{2}",
            font_size=36,
            color=BLUE_A
        ).next_to(text31,DOWN,buff=0.6)
        self.play(Write(text31))
        self.wait(0.5)
        self.play(Write(formula30))
        self.wait(5)
        self.play(Transform(formula30,formula31))
        text32 = Text("不难发现这个方向正好是实部下降最快的方向，\n且是虚部的等值线，这与先前的讨论一致。", font_size=32).shift(UP*3)
        self.play(Transform(text31,text32))
        self.wait(4)
        text33 = Text("由于f'(z)=0在复变函数中往往以鞍点的形式出现，\n因此先前的近似方法也被称作鞍点近似", 
                      t2c={"鞍点近似":YELLOW},font_size=32).shift(UP*2)
        self.play(Transform(text31,text33),FadeOut(formula30))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        self.wait(1)

class Example(Scene):
    def construct(self):
        
        text33 = Text("最后我们来看看鞍点近似的具体应用",font_size=32).shift(UP*1.5)
        self.play(Write(text33))
        self.wait(1)
        text34 = Text("或许你曾经见过这个公式",font_size=32).shift(UP*1.5)
        formula32 = MathTex(
            r"n! \approx \sqrt{2\pi n}(\frac{n}{e})^n \\ ( \ when \ n \gg 1 \ )",
            font_size=40,
            color=BLUE_A
        )
        self.play(Transform(text33,text34))
        self.play(Write(formula32))

        text35 = Text("不妨将阶乘用Gamma函数表示",font_size=32).shift(UP*1.5)
        formula33 = MathTex(
            r"n! = \Gamma(n+1) \approx \sqrt{2\pi n}(\frac{n}{e})^n ",
            font_size=40,
            color=BLUE_A
        )
        formula34 = MathTex(
            r"\Gamma(n+1) \approx \sqrt{2\pi n}(\frac{n}{e})^n ",
            font_size=40,
            color=BLUE_A
        )
        formula35 = MathTex(
            r"\Gamma(n+1) = \displaystyle \int_0^{\infty}t^{n}e^{-t}dt \approx \sqrt{2\pi n}(\frac{n}{e})^n ",
            font_size=40,
            color=BLUE_A
        )
        formula36 = MathTex(
            r" \displaystyle \int_0^{\infty}t^{n}e^{-t}dt \approx \sqrt{2\pi n}(\frac{n}{e})^n ",
            font_size=40,
            color=BLUE_A
        )
        self.play(Transform(text33,text35))
        self.wait(1)
        self.play(Transform(formula32,formula33))
        self.wait(1)
        self.play(Transform(formula32,formula34))
        self.wait(1)
        self.play(Transform(formula32,formula35))
        self.wait(1)
        self.play(Transform(formula32,formula36))
        self.wait(2)
        text36 = Text("即证",font_size=32).shift(UP*3+LEFT*3.2)
        formula37 = MathTex(
            r" \displaystyle \int_0^{\infty}e^{n\ln t-t}dt \approx \sqrt{2\pi n}(\frac{n}{e})^n ",
            font_size=40,
            color=BLUE_A
        ).shift(UP*3)
        self.play(Transform(text33,text36),Transform(formula32,formula37))
        self.wait(2)
        formula38 = MathTex(
            r" t=zn \Rightarrow LHS =  \displaystyle \int_0^{\infty}e^{n(\ln n+\ln z)-nz} n dz ",
            font_size=40,
            color=BLUE_A
        ).next_to(formula37,DOWN)
        formula39 = MathTex(
            r" = n^{n+1}\displaystyle \int_0^{\infty}e^{n(\ln z-z)}dz ",
            font_size=40,
            color=BLUE_A
        ).next_to(formula38,RIGHT).shift(LEFT*2)
        self.play(Write(formula38))
        self.wait(0.5)
        self.play(formula38.animate.shift(LEFT*2),Write(formula39))
        self.wait(1.5)
        text37 = Text("是不是看着有点眼熟？",font_size=32)
        text38 = Text("没错，这正是鞍点近似的典型形式！",font_size=32)
        self.play(Write(text37))
        self.wait(1)
        self.play(Transform(text37,text38))
        self.wait(2)
        text38 = Text("令",font_size=32).shift(UP*3+LEFT*2)
        formula40 = MathTex(
            r" f(z)= lnz-z",
            font_size=40,
            color=BLUE_A
        ).shift(UP*3)
        self.play(Transform(text33,text38),Transform(formula32,formula40),FadeOut(text37,formula38,formula39))
        self.wait(2)
        text39 = Text("求出鞍点",font_size=32).shift(UP*3+LEFT*4)
        formula41 = MathTex(
            r" f'(z)= 1/z-1=0 \Rightarrow z=1",
            font_size=40,
            color=BLUE_A
        ).shift(UP*3)
        text40 = Text("下降方向",font_size=32).shift(UP*2.2+LEFT*4)
        formula42 = MathTex( 
            r"\beta = -\frac{arg(f''(z_0))}{2}+\pi \pm \frac{\pi}{2} \Rightarrow \beta = 0 \ or \ \pi",
            font_size=40,
            color=BLUE_A
        ).shift(UP*2.2+RIGHT*1.2)
        self.play(VGroup(text33,formula32).animate.shift(UP*0.5))
        self.play(Write(text39),Write(formula41))
        self.wait(3)
        self.play(Write(text40),Write(formula42))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        text40 = Text("可以直观比较一下不同n对应的下降曲线",font_size=32).shift(UP*2)
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

        # 动画展示
        self.play(Write(text40))
        self.play(Create(axes_left), Write(label1))
        self.play(Create(g1), Create(t1), FadeIn(dot1))

        self.play(Create(axes_middle), Write(label10))
        self.play(Create(g10), Create(t10), FadeIn(dot10))

        self.play(Create(axes_right), Write(label20))
        self.play(Create(g20), Create(t20), FadeIn(dot20))

        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        text40 = Text("最后我们代入公式",font_size=32).shift(UP*2)
        formula43 = MathTex(
            r"I(\lambda) = e^{i\beta} e^{\lambda z_0} \sqrt{\frac{2\pi}{\lambda |f''(z_0)|}} ",
            font_size=36,
            color=BLUE_A
        ).next_to(text40,DOWN).shift(DOWN*1)
        rect = SurroundingRectangle(formula43, color=YELLOW_A, buff=0.2)
        self.play(Write(text40))
        self.play(Write(formula43),Create(rect))
        self.wait(1)
        formula44 = MathTex(
            r"I(n) = \int_0^{\infty}e^{n(\ln z-z)}dz=e^{0} e^{-n} \sqrt{\frac{2\pi}{n}} ",
            font_size=36,
            color=BLUE_A
        ).next_to(text40,DOWN).shift(DOWN*1)
        formula45 = MathTex(
            r"I(n)=e^{-n} \sqrt{\frac{2\pi}{n}}  ",
            font_size=36,
            color=BLUE_A
        ).next_to(text40,DOWN).shift(DOWN*1)
        self.play(Uncreate(rect),Transform(formula43,formula44))
        self.play(Transform(formula43,formula45))
        self.wait(1)
        formula46 = MathTex(
            r"n! \approx n^{n+1} e^{-n} \sqrt{\frac{2\pi}{n}}   ",
            font_size=36,
            color=BLUE_A
        ).next_to(text40,DOWN).shift(DOWN*1.5)
        formula47 = MathTex(
            r"n! \approx \sqrt{2\pi n} (\frac{n}{e})^n  ",
            font_size=36,
            color=BLUE_A
        ).next_to(text40,DOWN).shift(DOWN*1.5)
        self.play(formula43.animate.shift(UP*0.5),Write(formula46))
        self.wait(1)
        self.play(Transform(formula46,formula47))
        self.wait(1)
        text41 = Text("这就是大名鼎鼎的Stirling公式",font_size=32).scale(1.2).shift(UP*2)
        self.play(Transform(text40,text41),FadeOut(formula43),formula46.animate.scale(1.8).move_to([0,0,0]).set_color(BLUE))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        text42 = Text("另一个例子是Airy函数Ai(x)",font_size=32).shift(UP*2)
        formula48 = MathTex(
            r"Ai(x)=\displaystyle \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i(\frac{t^3}{3}+xt)} dt ",
            font_size=36,
            color=BLUE_A
        ).scale(1.5)
        text43 = Text("现在我们来分析其在±∞的渐进行为",font_size=32).shift(UP*2)
        self.play(Write(text42))
        self.play(Write(formula48))
        self.wait(1)
        self.play(Transform(text42,text43))
        self.wait(2)
        text44 = Text("注意到被积函数的定义也与鞍点近似的严格形式有所不同,\n但我们可以采用广义形式下的鞍点近似。",font_size=32).shift(UP*2)
        formula49 = MathTex(
            r"f(z,x) = i(\frac{z^3}{3}+xz)",
            font_size=36,
            color=BLUE_A
        ).shift(DOWN*0.5)
        formula50 = MathTex(
            r"I=e^{i\beta}\sqrt{\frac{2\pi}{|f''(z_0,\lambda)|}} e^{f(z_0,\lambda)}",
            font_size=36,
            color=BLUE_A
        ).shift(DOWN*1.6)
        text45 = Text("与先前不同，此时的鞍点位置与x有关",font_size=32).shift(UP*2)
        self.play(Transform(text42,text44))
        self.wait(1)
        self.play(formula48.animate.scale(0.7).shift(UP*0.5),Write(formula49))
        self.wait(1)
        self.play(Write(formula50))
        self.wait(1)
        self.play(Transform(text42,text45))
        self.wait(2)

        text46 = Text("对x>0的情况",font_size=32).shift(UP*3+RIGHT*3)
        img1 = ImageMobject("1.png").scale(0.5)
        img1.move_to([-4,2,0])  
        img2 = ImageMobject("2.png").scale(0.5)
        img2.move_to([-4,-2,0])  
        img3 = ImageMobject("3.png").scale(0.5)
        img3.move_to([-4,2,0])  
        img4 = ImageMobject("4.png").scale(0.5)
        img4.move_to([-4,-2,0]) 

        self.play(Transform(text42,text46),FadeOut(formula48,formula49,formula50))
        self.play(FadeIn(img1,img2))
        self.wait(2)

        formula51 = MathTex(
            r"f'(z_0,x)=i(z_0^2+x)=0 \ \Rightarrow \ z_0= \pm i \sqrt{x}",
            font_size=36,
            color=BLUE_A
        ).shift(UP*2+RIGHT*3)
        formula52 = MathTex(
            r"f''(z_0,x)=2iz_0=\mp 2\sqrt{x} \ \Rightarrow \ \beta= 0 \ or \ \pi",
            font_size=36,
            color=BLUE_A
        ).shift(UP*1.3+RIGHT*3)
        self.play(Write(formula51))
        self.wait(1.5)
        self.play(Write(formula52))
        self.wait(1.5)
        text47 = Text("选取经过上方鞍点的最速下降路径",font_size=32).shift(UP*0.5+RIGHT*3)
        formula53 = MathTex(
            r"I=\displaystyle \int_{i\sqrt{x}-\infty}^{i\sqrt{x}+\infty}e^{-\frac{2}{3}x^{3/2}-\sqrt{x}(z-i\sqrt{x})^2}dz",
            font_size=36,
            color=BLUE_A
        ).shift(DOWN*0.5+RIGHT*3)
        formula54 = MathTex(
            r"\sim \frac{e^{-\frac{2}{3}x^{3/2}}}{x^{1/4}}",
            font_size=36,
            color=BLUE_B
        ).scale(1.4).shift(DOWN*1.7+RIGHT*3)
        self.play(Write(text47))
        self.wait(1)
        self.play(Write(formula53))
        self.wait(1.5)
        self.play(Write(formula54))
        self.wait(1.5)
        text48 = Text("可见Airy 函数在 x>0 时\n渐近行为为指数衰减",font_size=32).shift(DOWN*3+RIGHT*3)
        self.play(Write(text48))
        self.wait(1.5)
        text49 = Text("对x<0的情况",font_size=32).shift(UP*3+RIGHT*3)
        self.play(Transform(text42,text49),FadeOut(img1,img2),FadeIn(img3,img4),
                  FadeOut(text47,formula51,formula52,formula53,formula54,text48))
        self.wait(1.5)
        formula55 = MathTex(
            r"f'(z_0,x)=i(z_0^2+x)=0 \ \Rightarrow \ z_0= \pm \sqrt{|x|}",
            font_size=36,
            color=BLUE_A
        ).shift(UP*2+RIGHT*3)
        formula56 = MathTex(
            r"f''(z_0,x)=2iz_0=\mp 2i\sqrt{|x|} \ \Rightarrow \ \beta= \frac{\pi}{4} \ or \ \frac{3\pi}{4}",
            font_size=36,
            color=BLUE_A
        ).shift(UP*1.3+RIGHT*3)
        self.play(Write(formula55))
        self.wait(1.5)
        self.play(Write(formula56))
        self.wait(1.5)
        text50 = Text("构造路径如左图",font_size=32).shift(UP*0.5+RIGHT*3)
        line = VMobject(color=BLUE)
        line.set_points_as_corners([
            [-4.88-0.5, -1.1+0.5, 0],
            [-3.88, -2.1, 0],
            [-2.88+0.5, -1.1+0.5, 0]
        ])
        formula57 = MathTex(
            r"I_1=\displaystyle \int_{-\infty}^{-i\sqrt{|x|}}e^{\frac{2i}{3}|x|^{3/2}-i\sqrt{|x|}(z+\sqrt{|x|})^2}dz",
            font_size=36,
            color=BLUE_A
        ).shift(DOWN*0.5+RIGHT*3)
        formula58 = MathTex(
            r"I_2=\displaystyle \int_{-i\sqrt{|x|}}^{+\infty}e^{-\frac{2i}{3}|x|^{3/2}+i\sqrt{|x|}(z-\sqrt{|x|})^2}dz",
            font_size=36,
            color=BLUE_A
        ).shift(DOWN*1.6+RIGHT*3)
        formula59 = MathTex(
            r"I=I_1+I_2=2\sqrt{\frac{\pi}{|x|^{1/2}}}\sin(\frac{2}{3}|x|^{3/2}+\frac{3\pi}{4})",
            font_size=36,
            color=BLUE_B
        ).shift(DOWN*2.6+RIGHT*3)
        self.play(Write(text50))
        self.play(Create(line),run_time=1)
        self.wait(1)
        self.play(Write(formula57))
        self.wait(1.5)
        self.play(Write(formula58))
        self.wait(1.5)
        self.play(Write(formula59))
        self.wait(1.5)
        text51 = Text("渐近行为为振荡衰减",font_size=32).shift(DOWN*3.5+RIGHT*3)
        self.play(Write(text51))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        text52 = Text("还有许多有（hui）趣（se）的应用就不一一列举啦",font_size=36)
        text53 = Text("那么这个视频就到此结束喽",font_size=36)
        text54 = Text("感谢看完的每位观众！",font_size=40,color=RED_A)
        path = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t)**3,
                13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t),
                0
            ]) * 0.05,  # 缩小比例
            t_range=[0, TAU],
            color=RED_A,
            stroke_width=2
        ).scale(0.5).next_to(text54,RIGHT)

        self.wait(1)
        self.play(Write(text52))
        self.wait(1)
        self.play(Transform(text52,text53))
        self.wait(1)
        self.play(Transform(text52,text54))
        self.play(Create(path),run_time = 2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.wait(1)

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

