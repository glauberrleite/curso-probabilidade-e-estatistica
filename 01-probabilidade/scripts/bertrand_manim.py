"""
Paradoxo de Bertrand — visualizacao com Manim (Community Edition).

Anima os tres metodos classicos de sortear uma corda AB num circulo de raio r e
mostra, ao vivo, a fracao de cordas "favoraveis" (comprimento l > r*sqrt(3), o
lado do triangulo equilatero inscrito) convergindo para 1/4, 1/3 e 1/2.

Instalar o manim (uma vez):
    pip install manim
    # dependencias de sistema (macOS/Homebrew): brew install cairo pango pkg-config ffmpeg
    # Este script usa apenas Text (sem MathTex), entao NAO precisa de LaTeX.

Renderizar (qualidade media, -p abre o video ao final):
    manim -pqm bertrand_manim.py BertrandPontoMedio
    manim -pqm bertrand_manim.py BertrandExtremos
    manim -pqm bertrand_manim.py BertrandRaio
    manim -pqm bertrand_manim.py BertrandResumo

Renderizar as tres animacoes de uma vez:
    manim -pqm bertrand_manim.py BertrandPontoMedio BertrandExtremos BertrandRaio
"""

import numpy as np
from manim import (
    ORIGIN, UP, DOWN, LEFT, RIGHT,
    BLUE, RED, GREEN, WHITE, YELLOW, GREY,
    Scene, Circle, Line, DashedLine, Dot, Arc, Polygon, VGroup,
    Text, DecimalNumber, Integer, ValueTracker,
    Create, FadeIn, FadeOut, LaggedStart,
)

R = 2.5                       # raio do circulo, em unidades de cena
COR_FAV = BLUE                # corda favoravel: l > r*sqrt(3)
COR_NAO = RED                 # corda nao favoravel
N_CORDAS = 150                # cordas amostradas por animacao
TAMANHO_LOTE = 15             # cordas por passo de animacao
SEMENTE = 7


def p3(x, y):
    """Ponto 2D -> vetor 3D que o manim espera."""
    return np.array([x, y, 0.0])


# ---------------------------------------------------------------------------
# Amostradores: devolvem (inicio, fim, favoravel) para cada corda.
# ---------------------------------------------------------------------------

def amostra_ponto_medio(rng):
    """Metodo I: ponto medio M uniforme na AREA do disco."""
    phi = rng.uniform(0, 2 * np.pi)
    rho = R * np.sqrt(rng.uniform(0, 1))         # rho = R*sqrt(U) => uniforme na area
    mx, my = rho * np.cos(phi), rho * np.sin(phi)
    tx, ty = -np.sin(phi), np.cos(phi)           # perpendicular ao raio
    meia = np.sqrt(max(R**2 - rho**2, 0.0))
    inicio = p3(mx + meia * tx, my + meia * ty)
    fim = p3(mx - meia * tx, my - meia * ty)
    return inicio, fim, rho < R / 2


def amostra_extremos(rng):
    """Metodo II: extremo A fixo; extremo B uniforme na circunferencia."""
    theta = rng.uniform(0, 2 * np.pi)
    inicio = p3(R, 0.0)                            # A fixo
    fim = p3(R * np.cos(theta), R * np.sin(theta))
    favoravel = 2 * np.pi / 3 < theta < 4 * np.pi / 3   # arco de 120 graus
    return inicio, fim, favoravel


def amostra_raio(rng):
    """Metodo III: direcao fixa; distancia do centro uniforme no diametro."""
    d = rng.uniform(-R, R)
    meia = np.sqrt(max(R**2 - d**2, 0.0))
    inicio = p3(d, meia)
    fim = p3(d, -meia)
    return inicio, fim, abs(d) < R / 2


# ---------------------------------------------------------------------------
# Cena base compartilhada pelos tres metodos.
# ---------------------------------------------------------------------------

class _BertrandBase(Scene):
    amostrador = None
    titulo = ""
    p_teorico = 0.0
    texto_regiao = ""

    def regiao(self):
        """Mobjects que destacam a regiao favoravel; sobrescrito por cada cena."""
        return VGroup()

    def construct(self):
        rng = np.random.default_rng(SEMENTE)

        # --- cenario: circulo C + triangulo equilatero inscrito ---
        circulo = Circle(radius=R, color=WHITE, stroke_width=3)
        vert = [p3(R * np.cos(a), R * np.sin(a))
                for a in np.deg2rad([90, 210, 330])]
        triangulo = Polygon(*vert, color=GREY, stroke_width=2)
        regiao = self.regiao()

        titulo = Text(self.titulo, font_size=30).to_edge(UP)
        limiar = Text("favoravel:  l > r√3", font_size=28).next_to(titulo, DOWN, buff=0.15)

        self.play(FadeIn(titulo), FadeIn(limiar))
        self.play(Create(circulo), Create(triangulo))
        self.play(Create(regiao), FadeIn(
            Text(self.texto_regiao, font_size=22, color=GREEN).to_edge(DOWN)))
        self.wait(0.4)

        # --- placar ao vivo (p simulado e numero de amostras) ---
        p_track = ValueTracker(0.0)
        n_track = ValueTracker(0.0)
        # mob_class=Text renderiza os digitos via Pango (sem depender de LaTeX)
        p_num = DecimalNumber(0, num_decimal_places=3, font_size=34,
                              color=COR_FAV, mob_class=Text)
        p_num.add_updater(lambda m: m.set_value(p_track.get_value()))
        n_num = Integer(0, font_size=30, mob_class=Text)
        n_num.add_updater(lambda m: m.set_value(int(n_track.get_value())))

        rot_p = VGroup(Text("p (sim) =", font_size=30, color=COR_FAV), p_num).arrange(RIGHT, buff=0.15)
        rot_teo = Text(f"p (teor) = {self._frac()}", font_size=30, color=YELLOW)
        rot_n = VGroup(Text("amostras:", font_size=26), n_num).arrange(RIGHT, buff=0.15)
        placar = VGroup(rot_p, rot_teo, rot_n).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        placar.to_corner(RIGHT + UP).shift(DOWN * 0.3)
        self.play(FadeIn(placar))

        # --- amostragem incremental das cordas ---
        favoraveis = 0
        for i in range(0, N_CORDAS, TAMANHO_LOTE):
            linhas = []
            for _ in range(TAMANHO_LOTE):
                inicio, fim, fav = self.amostrador(rng)
                favoraveis += int(fav)
                linhas.append(Line(inicio, fim,
                                   color=COR_FAV if fav else COR_NAO,
                                   stroke_width=2, stroke_opacity=0.55))
            n = i + TAMANHO_LOTE
            self.play(
                LaggedStart(*[Create(l) for l in linhas], lag_ratio=0.15),
                p_track.animate.set_value(favoraveis / n),
                n_track.animate.set_value(n),
                run_time=0.9,
            )

        self.wait(1.5)


class BertrandPontoMedio(_BertrandBase):
    amostrador = staticmethod(amostra_ponto_medio)
    titulo = "Metodo I: ponto medio uniforme no disco"
    p_teorico = 1 / 4
    texto_regiao = "corda favoravel  <=>  ponto medio dentro do circulo de raio r/2"

    def _frac(self):
        return "1/4"

    def regiao(self):
        return Circle(radius=R / 2, color=GREEN, stroke_width=4)


class BertrandExtremos(_BertrandBase):
    amostrador = staticmethod(amostra_extremos)
    titulo = "Metodo II: extremos uniformes na circunferencia"
    p_teorico = 1 / 3
    texto_regiao = "corda favoravel  <=>  extremo B no arco de 120 graus"

    def _frac(self):
        return "1/3"

    def regiao(self):
        arco = Arc(radius=R, start_angle=np.deg2rad(120),
                   angle=np.deg2rad(120), color=GREEN, stroke_width=8)
        a_fixo = Dot(p3(R, 0.0), color=WHITE)
        rotulo_a = Text("A", font_size=24).next_to(a_fixo, RIGHT, buff=0.1)
        return VGroup(arco, a_fixo, rotulo_a)


class BertrandRaio(_BertrandBase):
    amostrador = staticmethod(amostra_raio)
    titulo = "Metodo III: distancia uniforme num diametro"
    p_teorico = 1 / 2
    texto_regiao = "corda favoravel  <=>  centro entre as retas (|d| < r/2)"

    def _frac(self):
        return "1/2"

    def regiao(self):
        linhas = VGroup()
        for xv in (-R / 2, R / 2):
            h = np.sqrt(max(R**2 - xv**2, 0.0))
            linhas.add(DashedLine(p3(xv, -h), p3(xv, h), color=GREEN, stroke_width=4))
        return linhas


# ---------------------------------------------------------------------------
# Cena de resumo: os tres resultados lado a lado.
# ---------------------------------------------------------------------------

class BertrandResumo(Scene):
    def construct(self):
        titulo = Text("Paradoxo de Bertrand: 3 respostas para o mesmo problema",
                      font_size=30).to_edge(UP)
        self.play(FadeIn(titulo))

        dados = [
            ("Metodo I", "ponto medio\nno disco", "1/4", COR_FAV),
            ("Metodo II", "extremos na\ncircunferencia", "1/3", GREEN),
            ("Metodo III", "distancia num\ndiametro", "1/2", YELLOW),
        ]
        colunas = VGroup()
        for nome, descricao, frac, cor in dados:
            circ = Circle(radius=1.0, color=WHITE, stroke_width=3)
            n = Text(nome, font_size=26, color=cor)
            d = Text(descricao, font_size=18, line_spacing=0.8)
            p = Text(f"p = {frac}", font_size=40, color=cor)
            colunas.add(VGroup(n, circ, d, p).arrange(DOWN, buff=0.3))
        colunas.arrange(RIGHT, buff=1.2).next_to(titulo, DOWN, buff=0.6)

        self.play(LaggedStart(*[FadeIn(c) for c in colunas], lag_ratio=0.4))
        moral = Text('"Ao acaso" precisa ser definido: nao existe um unico p.',
                     font_size=24, color=RED).to_edge(DOWN)
        self.play(FadeIn(moral))
        self.wait(2)
