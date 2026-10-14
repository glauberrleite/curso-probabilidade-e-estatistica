# Scripts — Densidade conjunta do servidor

$X$ é o tempo (ms) até um servidor conectar e $Y$ o tempo (ms) até ele autorizar o usuário,
com $X < Y$. A densidade conjunta é

$$f_{XY}(x,y) = 6 \times 10^{-6} \exp(-0{,}001x - 0{,}002y), \quad 0 < x < y$$

## Animação — `servidor_manim.py`

Requer `manim` (Community Edition). As dependências de sistema são `cairo`, `pango`,
`pkg-config` e `ffmpeg`. **Não precisa de LaTeX**: o script usa apenas `Text`.

```bash
manim -pqm servidor_manim.py ServidorDensidadeConjunta
```

A cena monta o gráfico 3D em etapas:

1. o plano $(x, y)$ visto de cima e o suporte $0 < x < y$;
2. a câmera inclina e aparecem as fatias $f(x_0, y)$ com $x$ fixo;
3. a superfície preenche as fatias, com a "parede" sobre a diagonal $y = x$;
4. a câmera gira para mostrar a forma;
5. a região $R = \{x < 1000,\ y < 2000\}$ e o volume $P((X,Y) \in R) \approx 0{,}915$;
6. a área de cada fatia vira a marginal $f_X(x) = 0{,}003\,e^{-0{,}003x}$.

O vídeo renderizado fica em `../media/ServidorDensidadeConjunta.mp4` e é usado em `../aula.html`.
