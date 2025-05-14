from manim import *
import numpy as np

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


