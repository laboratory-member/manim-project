from manim import *
import numpy as np

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
