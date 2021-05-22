from manim import *

class Introduction(Scene):
    def construct(self):
        intro = Tex('Hi there!')
        intro_two = Tex('This is a YouTube channel that will')
        intro_three = Tex("animate biology concepts using the").next_to(intro_two, DOWN)
        intro_four = Tex('Manim animation engine.').next_to(intro_three, DOWN)
        outro = Tex('More content will be uploaded as time goes by :)')
        self.play(Write(intro))
        self.wait()
        self.play(FadeOut(intro))
        self.play(Write(intro_two), Write(intro_three), Write(intro_four))
        self.wait(2)
        self.play(FadeOut(intro_four), FadeOut(intro_three), FadeOut(intro_two))
        self.wait()
        self.play(Write(outro))
        self.wait()