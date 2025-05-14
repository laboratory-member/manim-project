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

    