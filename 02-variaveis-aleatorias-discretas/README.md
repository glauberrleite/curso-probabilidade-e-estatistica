# Motivação

# Distribuições de Probabilidade

A ideia é que podemos reusar a distribuição que uma variável aleatória é apresentada em um experimento para um outro domínio (ou sistema físico). Reusamos as propriedades e características, por isso é importante entender distribuições conhecidas, como a gaussiana, uniforme, hipergeométrica, entre outras.

> Definição: Distribuição de probabilidades de uma variável aleatória $X$ é uma descrição das probabilidades associadas aos valores possíveis de $X$.

Para uma variável aleatória discreta, a distribuição é frequentemente especificada por apenas uma lista de valores possíveis, juntamente com a probabilidade de cada um.


## Funções de Probabilidade

> Definição: Para uma variável aleatória discreta $X$, com valores possíveis $x_1$, $x_2$, $\cdots$, $x_n$, a função de probabilidade é uma função tal que:
> 1. $f(x_i) \geq 0$
> 2. $\sum_{i=1}^{n} f(x_i) = 1$
> 3. $f(x_i) = P(X = x_i)$

---
**Exemplo:** Seja a variável aleatória X o número de pastilhas de semicondutores que necessitam ser analisadas, de modo a detectar uma grande partícula de contaminação. Considere que a probabilidade de uma pastilha conter uma grande partícula seja 0,01 e que as pastilhas sejam independentes. Determine a distribuição de probabilidades de X.

**Solução:** Seja p uma pastilha em que uma grande partícula esteja presente e seja a uma pastilha em que essa partícula esteja ausente. O espaço amostral do experimento é infinito, podendo ser representado como todas as sequências possíveis que comecem com um conjunto de caracteres de a’s e terminem com p. Ou seja,
$$s = \{ p, ap, aap, \cdots \}$$

Temos que $P(p) = 0.01 \Rightarrow P(a) = 1 - P(p) = 0.99$
Fazemos os casos especiais $P(X = 1) = P(p) = 0.1$ e $P(X = 2) = P(ap) = P(a) \times P(p) = 0.99 \times 0.01$ (pela noção de independência)
Podemos induzir que 
$$P(X = x) = P(aaa\cdots ap) = 0.99^{x-1} \times 0.01$$

Vemos que $f(x) = P(X = x) \geq 0 \ \forall x \in \mathbb{Z}^+ $

Também temos que $\sum_{x=1}^{\infty} f(x)
  = \sum_{x=1}^{\infty} 0.99^{\,x-1} \times 0.01 = 0.01 \sum_{x=1}^{\infty} 0.99^{\,x-1}$

Se colocamos $k = x - 1$, Sobrou uma série geométrica de razão $r = 0.99$. Como $|r| < 1$ a série converge para $\frac{1}{1 - r}$.

Com isso, $\sum_{x=1}^{\infty} f(x) = 0.01 \times \frac{1}{0.01} = 1$

**Interpretação Prática:** O experimento aleatório aqui tem um número ilimitado de resultados, mas ele pode ser convenientemente modelado com uma variável aleatória discreta com uma faixa infinita (contável).

---


# Funções de distribuição cumulativa

Em geral, para qualquer variável aleatória com valores possíveis $x_1$, $x_2$, $\cdots$, $x_n$, os eventos $\{X = x_1\}$, $\{X = x_2 \}$, … são mutuamente excludentes.

> Definição: A função de distribuição cumulativa de uma variável aleatória discreta $X$, denotada por $F(x)$, é:
> $$F(x) = P(X \leq x) = \sum_{x_i \leq x} P(X  = x_i) = \sum_{x_i \leq x} f(x_i)$$



# Média e Variância

