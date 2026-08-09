"""
Paradoxo de Bertrand — simulacao Monte Carlo dos tres metodos.
"""

import argparse

import numpy as np

R = 1.0                      # raio do circulo C
LIMIAR = R * np.sqrt(3.0)    # lado do triangulo equilatero inscrito: l > r*sqrt(3)

def metodo_ponto_medio(n, rng):
    """Metodo I: o ponto medio M da corda e uniforme na area do disco.

    Amostrar uniformemente na area exige rho = R*sqrt(U) (senao o centro fica
    super-representado). A corda e perpendicular ao raio que passa por M.
    Favoravel  <=>  distancia do centro rho < R/2.
    """
    phi = rng.uniform(0.0, 2.0 * np.pi, n)
    rho = R * np.sqrt(rng.uniform(0.0, 1.0, n))      # distancia do centro
    mx, my = rho * np.cos(phi), rho * np.sin(phi)    # ponto medio M

    # direcao da corda = perpendicular ao raio (cos phi, sin phi)
    tx, ty = -np.sin(phi), np.cos(phi)
    meia = np.sqrt(np.maximum(R**2 - rho**2, 0.0))   # meio comprimento
    x1, y1 = mx + meia * tx, my + meia * ty
    x2, y2 = mx - meia * tx, my - meia * ty

    comprimento = 2.0 * meia
    favoravel = rho < R / 2.0
    return x1, y1, x2, y2, comprimento, favoravel


def metodo_extremos(n, rng):
    """Metodo II: um extremo A e fixo; o outro, B, e uniforme na circunferencia.

    Comprimento da corda com angulo central theta: l = 2*R*sin(theta/2).
    Favoravel  <=>  B cai no arco de 120 graus oposto a A.
    """
    ax, ay = R, 0.0                                  # A fixo em angulo 0
    theta = rng.uniform(0.0, 2.0 * np.pi, n)         # angulo de B
    bx, by = R * np.cos(theta), R * np.sin(theta)

    comprimento = np.hypot(bx - ax, by - ay)
    favoravel = comprimento > LIMIAR
    x1 = np.full(n, ax)
    y1 = np.full(n, ay)
    return x1, y1, bx, by, comprimento, favoravel


def metodo_raio(n, rng):
    """Metodo III: direcao fixa; a distancia do centro e uniforme no diametro.

    Cordas verticais; a posicao x = d e uniforme em [-R, R].
    Favoravel  <=>  |d| < R/2.
    """
    d = rng.uniform(-R, R, n)                         # distancia com sinal
    meia = np.sqrt(np.maximum(R**2 - d**2, 0.0))
    x1, y1 = d, meia
    x2, y2 = d, -meia

    comprimento = 2.0 * meia
    favoravel = np.abs(d) < R / 2.0
    return x1, y1, x2, y2, comprimento, favoravel


METODOS = [
    ("I  - ponto medio no disco", metodo_ponto_medio, 1 / 4),
    ("II - extremos na circunferencia", metodo_extremos, 1 / 3),
    ("III- distancia num diametro", metodo_raio, 1 / 2),
]


def simular(n, semente=42):
    rng = np.random.default_rng(semente)
    resultados = []
    print(f"\nParadoxo de Bertrand  (n = {n:,} cordas por metodo, r = {R})")
    print(f"Corda favoravel: comprimento l > r*sqrt(3) = {LIMIAR:.4f}\n")
    print(f"{'Metodo':<34}{'p estimado':>12}{'p teorico':>12}{'erro':>10}")
    print("-" * 68)
    for nome, funcao, teorico in METODOS:
        x1, y1, x2, y2, comprimento, favoravel = funcao(n, rng)
        p = favoravel.mean()
        print(f"{nome:<34}{p:>12.4f}{teorico:>12.4f}{abs(p - teorico):>10.4f}")
        resultados.append((nome, funcao, teorico, p))
    print("-" * 68)
    print("Mesmo problema, tres respostas diferentes: eis o paradoxo.\n")
    return resultados



def desenhar_figura(caminho, n_cordas=400, semente=1):
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(semente)
    fig, eixos = plt.subplots(1, 3, figsize=(15, 5.4))
    ang = np.linspace(0, 2 * np.pi, 400)

    cor_fav = "#1f77b4"   # azul: l > r*sqrt(3)
    cor_nao = "#d62728"   # vermelho: l <= r*sqrt(3)

    for eixo, (nome, funcao, teorico) in zip(eixos, METODOS):
        x1, y1, x2, y2, comprimento, favoravel = funcao(n_cordas, rng)

        # circulo C
        eixo.plot(R * np.cos(ang), R * np.sin(ang), color="black", lw=1.6)
        # triangulo equilatero inscrito (referencia do limiar r*sqrt(3))
        tri = np.array([0, 120, 240, 360]) * np.pi / 180 + np.pi / 2
        eixo.plot(R * np.cos(tri), R * np.sin(tri), color="0.5", lw=1.0, ls="--")

        # cordas (favoraveis por cima)
        for cor, mask in ((cor_nao, ~favoravel), (cor_fav, favoravel)):
            xs = np.column_stack([x1[mask], x2[mask], np.full(mask.sum(), np.nan)])
            ys = np.column_stack([y1[mask], y2[mask], np.full(mask.sum(), np.nan)])
            eixo.plot(xs.ravel(), ys.ravel(), color=cor, lw=0.6, alpha=0.35)

        # regiao caracteristica de cada metodo
        if funcao is metodo_ponto_medio:
            eixo.plot((R / 2) * np.cos(ang), (R / 2) * np.sin(ang),
                      color="green", lw=1.4)
        elif funcao is metodo_extremos:
            arco = np.linspace(120, 240, 100) * np.pi / 180
            eixo.plot(R * np.cos(arco), R * np.sin(arco), color="green", lw=3)
            eixo.plot([R], [0], "ko", ms=5)  # extremo fixo A
        else:
            for xv in (-R / 2, R / 2):
                eixo.axvline(xv, color="green", lw=1.2, ls=":")

        p = favoravel.mean()
        eixo.set_title(f"Metodo {nome.split('-')[0].strip()}\n"
                       f"p (sim) = {p:.3f}   |   p (teor) = {teorico:.3f}",
                       fontsize=11)
        eixo.set_aspect("equal")
        eixo.axis("off")

    fig.suptitle("Paradoxo de Bertrand: azul = corda favoravel (l > r$\\sqrt{3}$), "
                 "vermelho = nao", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(caminho, dpi=130)
    print(f"Figura salva em: {caminho}\n")


def main():
    parser = argparse.ArgumentParser(description="Simulacao do Paradoxo de Bertrand")
    parser.add_argument("--n", type=int, default=100_000,
                        help="numero de cordas por metodo (padrao: 100000)")
    parser.add_argument("--sem-figura", action="store_true",
                        help="nao gerar a figura, apenas os numeros")
    parser.add_argument("--saida", default="bertrand_simulacao.png",
                        help="arquivo da figura")
    args = parser.parse_args()

    simular(args.n)
    if not args.sem_figura:
        desenhar_figura(args.saida)


if __name__ == "__main__":
    main()
