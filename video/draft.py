from manim import *

class ExpSaddleApprox(Scene):
    def construct(self):
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
        self.play(Write(text54))
        self.play(Create(path),run_time = 2)

        self.play(FadeOut(*self.mobjects))
        self.wait(1)