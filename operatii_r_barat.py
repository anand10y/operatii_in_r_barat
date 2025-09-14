from manim import *

class OperatiiRBaratMathTex(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Titlu
        titlu = MathTex(r"\text{Operații în } \overline{\mathbb{R}}", font_size=60)
        self.play(Write(titlu))
        self.wait(2)
        self.play(FadeOut(titlu))

        # Adunare infinit
        adunare = MathTex(r"+\infty + (-\infty) = \text{nedeterminat}", font_size=50)
        self.play(Write(adunare))
        self.wait(3)
        self.play(FadeOut(adunare))

        # Scădere infinit
        scadere = MathTex(r"+\infty - (+\infty) = \text{nedeterminat}", font_size=50)
        self.play(Write(scadere))
        self.wait(3)
        self.play(FadeOut(scadere))

        # Înmulțire infinit
        inmultire = MathTex(r"(-\infty) \cdot (-3) = +\infty", font_size=50)
        self.play(Write(inmultire))
        self.wait(3)
        self.play(FadeOut(inmultire))

        # Înmulțire cu zero (nedeterminat)
        inmultire_zero = MathTex(r"0 \cdot (+\infty) = \text{nedeterminat}", font_size=50)
        self.play(Write(inmultire_zero))
        self.wait(3)
        self.play(FadeOut(inmultire_zero))

        # Împărțire la infinit
        impartire = MathTex(r"\frac{5}{+\infty} = 0", font_size=50)
        self.play(Write(impartire))
        self.wait(3)
        self.play(FadeOut(impartire))

        # Ridicare la putere
        putere = MathTex(r"(+\infty)^2 = +\infty, \quad (-\infty)^3 = -\infty", font_size=50)
        self.play(Write(putere))
        self.wait(3)
        self.play(FadeOut(putere))

        # Rezumat final
        final = MathTex(r"\text{Rezumat: Operațiile cu infinit în } \overline{\mathbb{R}}", font_size=50)
        self.play(Write(final))
        self.wait(3)
