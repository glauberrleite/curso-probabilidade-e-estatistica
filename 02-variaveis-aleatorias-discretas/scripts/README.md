# Scripts — Variáveis aleatórias discretas

## Simulação da geométrica — `geometrica_simulacao.py`

Fecha o exercício das pastilhas (§ 06 da aula): inspeciona-se uma pastilha por vez até
achar a primeira com cinco ou mais partículas contaminadas. Com $P(\text{5 ou mais}) = 0{,}20$
e pastilhas independentes, $X$ é **geométrica** com $p = 0{,}20$:

$$f(x) = (1-p)^{x-1}p \qquad \mu = \tfrac{1}{p} = 5 \qquad \sigma = \sqrt{\tfrac{1-p}{p^2}} \approx 4{,}47$$

O desvio padrão é quase igual à média. A simulação mostra o que isso significa na prática:
a moda é **1**, e **cerca de 33 %** das vezes são necessárias mais tentativas que a própria média.

Requer `numpy` e `matplotlib`.

```bash
python geometrica_simulacao.py                # simula e salva ../media/geometrica_simulacao.png
python geometrica_simulacao.py --n 500000     # mais repetições
python geometrica_simulacao.py --p 0.05       # outra probabilidade de sucesso
python geometrica_simulacao.py --sem-figura   # só os números no terminal
```

A figura tem três painéis:

| Painel | O que mostra |
|--------|--------------|
| (a) | histograma simulado com a $f(x)$ exata por cima — a moda em 1, bem à esquerda da média |
| (b) | a média acumulada convergindo para 5, com a faixa $\mu \pm \sigma$ |
| (c) | a cauda $P(X > k)$, empírica e exata, destacando os ~33 % acima da média |
