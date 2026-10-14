"""
Densidade conjunta do exemplo do servidor — visualizacao 3D com Manim (Community Edition).

X = tempo (ms) ate o servidor conectar, Y = tempo (ms) ate autorizar o usuario,
sempre com X < Y. A densidade conjunta e

    f(x, y) = 6e-6 * exp(-0.001 x - 0.002 y),   0 < x < y

A animacao monta o grafico em etapas:
  1. o plano (x, y) visto de cima e o suporte 0 < x < y (um triangulo);
  2. a camera inclina e aparecem fatias f(x0, y) com x fixo;
  3. a superficie inteira preenche as fatias (com a "parede" sobre x = y);
  4. a camera gira para mostrar a forma;
  5. a regiao R = {x < 1000, y < 2000} e o volume P((X, Y) em R) ~ 0,915;
  6. a fatia vira marginal: a area de cada fatia e f_X(x0), uma exponencial.

Instalar o manim (uma vez):
    pip install manim
    # dependencias de sistema (macOS/Homebrew): brew install cairo pango pkg-config ffmpeg
    # Este script usa apenas Text (sem MathTex), entao NAO precisa de LaTeX.

Renderizar (qualidade media, -p abre o video ao final):
    manim -pqm servidor_manim.py ServidorDensidadeConjunta
"""

import numpy as np
from manim import (
    ORIGIN, UP, DOWN, LEFT, RIGHT, OUT, DEGREES,
    WHITE, GREY,
    ThreeDScene, ThreeDAxes, Surface, ParametricFunction, Polygon, Line, VGroup,
    Text, Create, FadeIn, FadeOut, Write, LaggedStart, ReplacementTransform,
    ManimColor,
)

# Mesmas cores das paginas de aula (tema escuro).
TEAL = ManimColor("#55c0d2")       # densidade, o teorico
TEAL_ESC = ManimColor("#2a7f8e")
AMBAR = ManimColor("#e2a355")      # regiao R / probabilidade calculada
AMBAR_ESC = ManimColor("#a8620a")
TINTA = ManimColor("#e3eaed")
MUDO = ManimColor("#8598a1")

M = 2000.0                         # quadro: 0 <= x, y <= M (ms)
ESCALA_Z = 1e6                     # eixo z em unidades de 10^-6


def f(x, y):
    """Densidade conjunta (sem o indicador de x < y), em unidades de 10^-6."""
    return 6.0 * np.exp(-0.001 * x - 0.002 * y)


def fX(x):
    """Marginal de X: exponencial com lambda = 0,003."""
    return 0.003 * np.exp(-0.003 * x)


class ServidorDensidadeConjunta(ThreeDScene):
    def construct(self):
        self.camera.background_color = ManimColor("#0d1418")

        eixos = ThreeDAxes(
            x_range=[0, M, 500], y_range=[0, M, 500], z_range=[0, 6, 1],
            x_length=6, y_length=6, z_length=3.0,
            axis_config={"color": MUDO, "stroke_width": 2, "include_ticks": True},
        )

        def p(x, y, z=0.0):
            return eixos.c2p(x, y, z)

        # --- rotulos (Text sempre de frente para a camera) ---
        rot_x = Text("x  (conexão, ms)", font_size=22, color=TINTA).move_to(p(M * 1.02, -330))
        rot_y = Text("y  (autorização, ms)", font_size=22, color=TINTA).move_to(p(-200, M * 1.15))
        rot_z = Text("f(x, y)  ×10⁻⁶", font_size=22, color=TINTA).move_to(p(0, 0, 6.8))
        ticks = VGroup()
        for v in (500, 1000, 1500):
            ticks.add(Text(str(v), font_size=18, color=MUDO).move_to(p(v, -110)))
            ticks.add(Text(str(v), font_size=18, color=MUDO).move_to(p(-150, v)))

        titulo = Text("Servidor: densidade conjunta de X e Y", font_size=30, color=TINTA)
        formula = Text("f(x, y) = 6·10⁻⁶ · e^(−0,001x − 0,002y),   0 < x < y",
                       font_size=24, color=TEAL)
        cab = VGroup(titulo, formula).arrange(DOWN, buff=0.12).to_corner(UP + LEFT, buff=0.35)

        # ---------------------------------------------------------------
        # 1. o plano visto de cima e o suporte
        # ---------------------------------------------------------------
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=0.72,
                                    frame_center=OUT * 0.9)
        self.add_fixed_in_frame_mobjects(cab)
        self.remove(cab)
        self.play(FadeIn(cab))
        self.play(Create(eixos.x_axis), Create(eixos.y_axis), FadeIn(ticks),
                  FadeIn(rot_x), FadeIn(rot_y))

        diag = Line(p(0, 0), p(M, M), color=TINTA, stroke_width=3)
        suporte = Polygon(p(0, 0), p(0, M), p(M, M), stroke_width=0,
                          fill_color=TEAL, fill_opacity=0.28)
        rot_diag = Text("y = x", font_size=22, color=TINTA).move_to(p(M * 0.80, M * 0.66))
        nota = self._nota("Suporte: 0 < x < y — o servidor só autoriza depois de conectar")
        self.play(Create(diag), FadeIn(rot_diag))
        self.play(FadeIn(suporte), FadeIn(nota))
        self.wait(1.5)

        # ---------------------------------------------------------------
        # 2. inclina a camera; fatias com x fixo
        # ---------------------------------------------------------------
        self.play(FadeOut(rot_diag))
        self.move_camera(phi=65 * DEGREES, theta=-60 * DEGREES, zoom=0.75, run_time=2.5,
                         added_anims=[Create(eixos.z_axis)])
        for t in (*ticks, rot_x, rot_y):
            self.add_fixed_orientation_mobjects(t)
        self.add_fixed_orientation_mobjects(rot_z)
        self.play(FadeIn(rot_z))

        nota2 = self._nota("Fatias: fixe x = x₀ e varie y > x₀  →  curva f(x₀, y)")
        self.play(ReplacementTransform(nota, nota2))

        xs_fatia = np.arange(0, M, 250)
        fatias = VGroup()
        for x0 in xs_fatia:
            curva = ParametricFunction(lambda t, x0=x0: p(x0, t, f(x0, t)),
                                       t_range=[x0, M], color=TEAL, stroke_width=3)
            haste = Line(p(x0, x0, 0), p(x0, x0, f(x0, x0)), color=TEAL, stroke_width=2)
            fatias.add(VGroup(haste, curva))
        self.play(LaggedStart(*[Create(fa) for fa in fatias], lag_ratio=0.35), run_time=4)
        self.wait(0.8)

        # ---------------------------------------------------------------
        # 3. a superficie preenche as fatias
        # ---------------------------------------------------------------
        # (u, v) -> x = u, y = u + v (M - u): cobre exatamente o triangulo x < y < M
        superficie = Surface(
            lambda u, v: p(u, u + v * (M - u), f(u, u + v * (M - u))),
            u_range=[0, M * 0.999], v_range=[0, 1], resolution=(28, 22),
            checkerboard_colors=[TEAL, TEAL_ESC], fill_opacity=0.82,
            stroke_color=TEAL, stroke_width=0.4,
        )
        # parede vertical sobre a diagonal: a densidade salta de 0 para f(x, x)
        parede = Surface(
            lambda u, w: p(u, u, w * f(u, u)),
            u_range=[0, M * 0.999], v_range=[0, 1], resolution=(28, 2),
            checkerboard_colors=[TEAL_ESC, TEAL_ESC], fill_opacity=0.35,
            stroke_width=0,
        )
        nota3 = self._nota("A superfície inteira é f(x, y); volume total sob ela = 1")
        self.play(ReplacementTransform(nota2, nota3))
        self.play(Create(superficie), FadeIn(parede), fatias.animate.set_stroke(opacity=0.35),
                  run_time=3.5)
        self.play(FadeOut(fatias))

        # ---------------------------------------------------------------
        # 4. gira para ver a forma
        # ---------------------------------------------------------------
        self.begin_ambient_camera_rotation(rate=-0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=65 * DEGREES, theta=-60 * DEGREES, run_time=1.5)

        # ---------------------------------------------------------------
        # 5. regiao R e o volume = probabilidade
        # ---------------------------------------------------------------
        a, b = 1000.0, 2000.0 * 0.999
        caixa = Polygon(p(0, 0), p(a, 0), p(a, b), p(0, b), color=AMBAR, stroke_width=4,
                        fill_opacity=0)
        patch = Surface(
            lambda u, v: p(u, u + v * (b - u), f(u, u + v * (b - u))),
            u_range=[0, a], v_range=[0, 1], resolution=(16, 22),
            checkerboard_colors=[AMBAR, AMBAR_ESC], fill_opacity=0.92,
            stroke_color=AMBAR, stroke_width=0.4,
        )
        nota4 = self._nota("R = {x < 1000, y < 2000}:  P((X, Y) ∈ R) = volume sobre R ≈ 0,915",
                           cor=AMBAR)
        self.play(ReplacementTransform(nota3, nota4), Create(caixa))
        self.play(superficie.animate.set_fill(opacity=0.25), FadeIn(patch), run_time=2)
        self.wait(2.5)

        # ---------------------------------------------------------------
        # 6. de volta as fatias: a area de cada uma e a marginal f_X(x0)
        # ---------------------------------------------------------------
        self.play(FadeOut(patch), FadeOut(caixa),
                  superficie.animate.set_fill(opacity=0.55))
        nota5 = self._nota("Área de cada fatia = f_X(x₀) = 0,003·e^(−0,003x₀): a marginal de X",
                           cor=AMBAR)
        x0 = 400.0
        fatia = Polygon(
            *[p(x0, t, f(x0, t)) for t in np.linspace(x0, M, 60)],
            p(x0, M, 0), p(x0, x0, 0),
            stroke_color=AMBAR, stroke_width=3, fill_color=AMBAR, fill_opacity=0.55,
        )
        self.play(ReplacementTransform(nota4, nota5), FadeIn(fatia))
        # a marginal desenhada na parede do fundo (y = M), em escala propria
        k = 4.5 / fX(0)
        marginal = ParametricFunction(lambda t: p(t, M, k * fX(t)), t_range=[0, M],
                                      color=AMBAR, stroke_width=4)
        rot_m = Text("f_X(x)  (outra escala)", font_size=20, color=AMBAR).move_to(p(900, M, 3.2))
        self.add_fixed_orientation_mobjects(rot_m)
        self.remove(rot_m)
        self.play(Create(marginal), FadeIn(rot_m), run_time=2)
        self.wait(0.6)
        self.move_camera(phi=74 * DEGREES, theta=-78 * DEGREES, run_time=3)
        self.wait(2.5)

    def _nota(self, texto, cor=TINTA):
        nota = Text(texto, font_size=22, color=cor).to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(nota)
        self.remove(nota)
        return nota
