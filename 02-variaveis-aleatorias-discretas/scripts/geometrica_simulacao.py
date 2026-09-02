"""
Distribuicao geometrica — simulacao Monte Carlo do exercicio das pastilhas.

Fecha o exercicio do paragrafo 06 da aula: pastilhas sao inspecionadas uma a uma
ate encontrar a primeira com cinco ou mais particulas contaminadas. Como
P(5 ou mais) = 0,20 e as pastilhas sao independentes, X = numero de pastilhas
inspecionadas e geometrica com p = 0,20:

    f(x) = (1 - p)^(x-1) * p        mu = 1/p = 5        sigma = sqrt((1-p)/p^2) ~ 4,47

A conta fecha, mas o resultado e contra-intuitivo: o desvio padrao e quase igual
a media. Esta simulacao mostra o que isso significa na pratica.

Uso:
    python geometrica_simulacao.py                # simula e salva a figura em ../media/
    python geometrica_simulacao.py --n 500000     # numero de repeticoes
    python geometrica_simulacao.py --p 0.05       # outra probabilidade de sucesso
    python geometrica_simulacao.py --sem-figura   # so os numeros no terminal
"""

import argparse
import os

import numpy as np


def simular(p, n, rng):
    """Sorteia n realizacoes de X ~ geometrica(p), contagem comecando em 1.

    numpy.random.Generator.geometric ja usa essa convencao (numero de tentativas
    ate o primeiro sucesso, inclusive), entao nao ha ajuste de indice a fazer.
    """
    return rng.geometric(p, size=n)


def teorico(p):
    """Media, variancia e desvio padrao exatos da geometrica."""
    mu = 1.0 / p
    var = (1.0 - p) / p**2
    return mu, var, np.sqrt(var)


def relatorio(p, amostras):
    mu, var, sd = teorico(p)
    n = amostras.size
    print(f"\nGeometrica com p = {p}  (n = {n:,} repeticoes)")
    print("-" * 62)
    print(f"{'':<22}{'simulado':>14}{'exato':>14}")
    print(f"{'media':<22}{amostras.mean():>14.4f}{mu:>14.4f}")
    print(f"{'variancia':<22}{amostras.var():>14.4f}{var:>14.4f}")
    print(f"{'desvio padrao':<22}{amostras.std():>14.4f}{sd:>14.4f}")
    print("-" * 62)
    print("Cauda — proporcao que precisou de MAIS que k tentativas:")
    for k in (1, 5, 10, 15, 20):
        emp = (amostras > k).mean()
        exa = (1 - p) ** k
        marca = "   <- mais que a propria media" if abs(k - mu) < 1e-9 else ""
        print(f"  P(X > {k:2d}) : simulado {emp:.4f}   exato {exa:.4f}{marca}")
    print("-" * 62)
    print(f"A moda e 1 (P(X = 1) = {p:.2f}), embora a media seja {mu:.0f}:")
    print("a distribuicao e assimetrica, com cauda longa a direita.\n")


def desenhar_figura(caminho, p, amostras):
    import matplotlib.pyplot as plt

    mu, var, sd = teorico(p)
    n = amostras.size

    cor_sim = "#a8620a"   # ambar: medido/simulado
    cor_teo = "#0d6e7d"   # teal: exato/teorico

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.6))

    # (a) histograma simulado com a f(x) exata por cima
    corte = int(np.ceil(mu + 4 * sd))
    bins = np.arange(0.5, corte + 1.5, 1.0)
    ax1.hist(amostras, bins=bins, density=True, color=cor_sim, alpha=0.55,
             label="simulado")
    xs = np.arange(1, corte + 1)
    ax1.plot(xs, (1 - p) ** (xs - 1) * p, "o-", color=cor_teo, ms=3.5, lw=1.4,
             label="f(x) exata")
    ax1.axvline(mu, color=cor_teo, ls="--", lw=1.2)
    ax1.text(mu, ax1.get_ylim()[1] * 0.92, f"  mu = {mu:.0f}", color=cor_teo, fontsize=9)
    ax1.set_title("(a) Distribuicao de X", fontsize=11)
    ax1.set_xlabel("pastilhas inspecionadas")
    ax1.set_ylabel("frequencia relativa")
    ax1.legend(fontsize=9, frameon=False)

    # (b) media acumulada convergindo, com a faixa mu +- sigma
    acum = np.cumsum(amostras) / np.arange(1, n + 1)
    ax2.axhspan(mu - sd, mu + sd, color=cor_teo, alpha=0.12, label="mu ± sigma")
    ax2.axhline(mu, color=cor_teo, ls="--", lw=1.2, label=f"mu = {mu:.0f}")
    ax2.plot(acum, color=cor_sim, lw=1.0, label="media acumulada")
    ax2.set_xscale("log")
    # X e uma contagem: nao faz sentido o eixo descer abaixo de zero
    ax2.set_ylim(max(0.0, mu - 2.2 * sd), mu + 2.2 * sd)
    ax2.set_title("(b) A media converge", fontsize=11)
    ax2.set_xlabel("repeticoes (escala log)")
    ax2.legend(fontsize=9, frameon=False, loc="upper right")

    # (c) cauda: proporcao que precisou de mais que k tentativas
    ks = np.arange(0, corte + 1)
    emp = np.array([(amostras > k).mean() for k in ks])
    ax3.plot(ks, (1 - p) ** ks, color=cor_teo, lw=1.6, label="exato  (1-p)^k")
    ax3.plot(ks, emp, "o", color=cor_sim, ms=3, label="simulado")
    ax3.axvline(mu, color="0.5", ls=":", lw=1.2)
    ax3.annotate(f"{(1 - p) ** mu:.1%} precisam de\nmais que a media",
                 xy=(mu, (1 - p) ** mu), xytext=(mu + 3.2, 0.55),
                 fontsize=9, color="#9d332e",
                 arrowprops=dict(arrowstyle="->", color="#9d332e", lw=1.1))
    ax3.set_title("(c) A cauda e longa", fontsize=11)
    ax3.set_xlabel("k")
    ax3.set_ylabel("P(X > k)")
    ax3.legend(fontsize=9, frameon=False)

    for ax in (ax1, ax2, ax3):
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(
        f"Pastilhas ate a primeira contaminada — geometrica com p = {p}:  "
        f"media {mu:.0f}, desvio padrao {sd:.2f}",
        fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(caminho, dpi=130)
    print(f"Figura salva em: {caminho}\n")


def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    padrao = os.path.join(aqui, "..", "media", "geometrica_simulacao.png")

    parser = argparse.ArgumentParser(
        description="Simulacao Monte Carlo da geometrica (exercicio das pastilhas)")
    parser.add_argument("--p", type=float, default=0.20,
                        help="probabilidade de sucesso em cada tentativa (padrao: 0.20)")
    parser.add_argument("--n", type=int, default=200_000,
                        help="numero de repeticoes (padrao: 200000)")
    parser.add_argument("--semente", type=int, default=42, help="semente do gerador")
    parser.add_argument("--sem-figura", action="store_true",
                        help="nao gerar a figura, apenas os numeros")
    parser.add_argument("--saida", default=os.path.normpath(padrao),
                        help="arquivo da figura")
    args = parser.parse_args()

    if not 0 < args.p <= 1:
        parser.error("--p deve estar em (0, 1]")

    rng = np.random.default_rng(args.semente)
    amostras = simular(args.p, args.n, rng)
    relatorio(args.p, amostras)
    if not args.sem_figura:
        desenhar_figura(args.saida, args.p, amostras)


if __name__ == "__main__":
    main()
