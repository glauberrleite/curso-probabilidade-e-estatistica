# Scripts — Paradoxo de Bertrand

Ilustram o Paradoxo de Bertrand (Papoulis, Fig. 1-1): dado um círculo de raio $r$,
qual a probabilidade $p$ de uma corda "escolhida ao acaso" ter comprimento
$l > r\sqrt{3}$ (o lado do triângulo equilátero inscrito)?

A resposta depende de **como** se sorteia a corda — daí o paradoxo:

| Método | Como sorteia a corda | $p$ |
|--------|----------------------|-----|
| I   | ponto médio uniforme na **área** do disco | $1/4$ |
| II  | extremos uniformes na **circunferência** | $1/3$ |
| III | distância ao centro uniforme num **diâmetro** | $1/2$ |

## 1. Simulação Monte Carlo — `bertrand_simulacao.py`

Requer `numpy` e `matplotlib`.

```bash
python bertrand_simulacao.py                 # simula e salva bertrand_simulacao.png
python bertrand_simulacao.py --n 500000      # mais amostras
python bertrand_simulacao.py --sem-figura    # só os números no terminal
```

Imprime as probabilidades estimadas ao lado das teóricas e gera uma figura com uma
amostra de cordas por método (azul = favorável, vermelho = não).

## 2. Animação — `bertrand_manim.py`

Requer `manim` (Community Edition). As dependências de sistema são `cairo`, `pango`,
`pkg-config` e `ffmpeg`. **Não precisa de LaTeX** — o script usa apenas `Text`.

No macOS (Homebrew):

```bash
brew install cairo pango pkg-config ffmpeg
pip install manim
```

Renderizar (`-pql` = preview, qualidade baixa; use `-pqm`/`-pqh` para média/alta):

```bash
manim -pqm bertrand_manim.py BertrandPontoMedio
manim -pqm bertrand_manim.py BertrandExtremos
manim -pqm bertrand_manim.py BertrandRaio
manim -pqm bertrand_manim.py BertrandResumo
```

Cada cena mostra a região favorável do método e a estimativa $\hat{p}$ convergindo
para o valor teórico à medida que as cordas são sorteadas.
