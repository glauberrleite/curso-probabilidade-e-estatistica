# Motivação

❗️ Trazer um exemplo prático que mostre uma coisa disruptiva, como a probabilidade de um intervalo ter valor, mas de X assumir um valor específico é zero.

Uma variável aleatória contínua é uma variável aleatória com um intervalo (finito ou infinito) de números reais para a sua faixa.

⚠️ O número de valores possíveis de $X$ é infinito incontável.

Precisamos adaptar a teoria para contemplar as funções de probabilidade, valor esperado, média e variância, além de ver distribuições que podemos reusar.

Como grande parte dos conceitos podem ser reaproveitados, naturalmente, o ritmo da disciplina neste assunto e no próximo será um pouco mais acelerado.

# Funções densidade de probabilidade

> Definição: Para uma variável aleatória contínua $X$, uma função densidade de probabilidade é uma função tal que:
> 1. $f(x) \geq 0$
> 2. $\int_{-\infty}^\infty f(x) dx = 1$
> 3. $P(a \leq X \leq b) = \int_{a}^b f(x) dx$

🤔Veja que, considerando a definição, quem seria $P(X = a)$?
Aplicando, temos:

$$P(X = a) = P(a \leq X \leq a) = \int_a^a f(x)dx = F(x) - F(x) = 0$$

⚠️Então sempre vamos estar observando a probabilidade de um intervalo contínuo, ao invés de assumir um valor único, como no caso discreto.

> Quando uma medida particular de corrente for observada, tal como 14,47 miliampères, esse resultado poderá ser interpretado como o valor arredondado de uma medida da corrente, que está realmente na faixa $14,465 \leq x \leq 14,475$.

⚠️Uma vez que cada ponto tem probabilidade zero, não é necessário distinguir entre desigualdades, tais como $<$ ou $\leq$, para variáveis aleatórias contínuas.

💡Um histograma é uma aproximação da função densidade de probabilidade.

## Função de Distribuição Cumulativa

> Definição: A função de distribuição cumulativa de uma variável aleatória contínua $X$ é
> $$F(x) = P(X \leq x) = \int_{\infty}^x f(u) du$$

Uma grande vantagem é que podemos usar o [Teorema Fundamental do Cálculo](https://pt.wikipedia.org/wiki/Teorema_fundamental_do_c%C3%A1lculo) para estabelecer a relação entre a função cumulativa e a função densidade de probabilidade:

$$\frac{d}{dx} F(x) = \frac{d}{dx} \int_{\infty}^x f(u) du = f(x)$$

---

Exemplo: O tempo (em milissegundos) até que uma reação química esteja completa é aproximado pela função de distribuição cumulativa.

$$F(x) = \begin{cases}0, & x < 0 \\ 1 - e^{-0,01x}, & 0 \leq x\end{cases}$$

- Que proporção de reações é completada dentro de 200 milissegundos?
- Determine a função densidade de probabilidade de $X$.

---

# Valor esperado

> Definição: Se $X$ é uma variável aleatória contínua, com função densidade de probabilidade $f(x)$,
> $$ E[h(X)] = \int_{-\infty}^{\infty} h(x) f(x) dx $$


Com isso, temos o valor esperado (como medida resumo) para posição esperada de $X$ (a média $\mu$) e para a dispersão (a variância $\sigma^2$)

- $\mu = E(X) = \int_{-\infty}^{\infty} x f(x) dx $
- $\sigma^2 = V(X) = E[(X - \mu)^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx $
- O desvio padrão se mantém $\sigma = \sqrt{\sigma^2} = \sqrt{V(X)}$

Veja que faz sentido o valor espera ser um único valor ao invés de um intervalo, pois é uma integral definida.

# Distribuições de probabilidade

Agora vamos passar por algumas distribuições conhecidas, permitindo que façamos reuso das características delas quando possível.

## Distribuição Contínua Uniforme

Uma variável aleatório contínua $X$, com função densidade de probabilidade
$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

tem uma distribuição contínua uniforme ($X \sim U(x; a, b)$).

- Média: $\mu = E(X) = \frac{a + b}{2}$
- Variância: $\sigma^2 = \frac{(b - a)^2}{12}$

## Distribuição Normal (ou Gaussiana)

Indubitavelmente, o modelo mais largamente utilizado para uma medida contínua é uma variável aleatória normal. Toda vez que um experimento aleatório for replicado, a variável aleatória que for igual ao resultado médio (ou total) das réplicas tenderá a ter uma distribuição normal, à medida que o número de réplicas se torne grande.

Aqui, a própria média $\mu$ e a variância $\sigma^2$ assumem o papel de parâmetros da função densidade. Podemos ver como mexem no formato da curva, que lembra um sino (*bell-shaped*).
![](https://thumb.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/3840px-Normal_Distribution_PDF.svg.png)

Uma variável aleatória $X$, com função densidade de probabilidade
$$f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}}e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$$

é uma variável aleatória normal ($X \sim \mathcal{N}(x; \mu, \sigma^2)$).

Claramente:
- Média: $E(X) = \mu$
- Variância: $E[(X-\mu)^2]= \sigma^2$

🤔Distribuições binomiais e de poisson podem ser sintonizadas (através dos seus parâmetros) para se tornar gaussianas.

### Teorema central do limite
💡A distribuição normal será muito importante no futuro, quando discutirmos o teorema central do limite.
> [(Wikipedia)](https://en.wikipedia.org/wiki/Normal_distribution) It states that the average of many statistically independent samples (observations) of a random variable with finite mean and variance is itself a random variable—whose distribution converges to a normal distribution as the number of samples increases. 
> Therefore, physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have distributions that are nearly normal

### Explorando a simetria da distribuição gaussiana

Um resultado útil é explorar a simetria... De forma geral, temos:

$$P(\mu - \sigma < X < \mu + \sigma) = 0,6827$$
$$P(\mu - 2\sigma < X < \mu + 2\sigma) = 0,9545$$
$$P(\mu - 3\sigma < X < \mu + 3\sigma) = 0,9973$$

![](https://www.mathsisfun.com/data/images/normal-distrubution-large.svg)

⚠️A distribuição normal padrão (ou *Standard Normal Distribuition*) nada mais é do que $\mathcal{N}(x; 0, 1)$. Isso facilita algumas tomadas de decisões.

### z-score

Por conta da simetria, uma métrica interessante é o z-score, que diz, usando o desvio padrão como unidade, quão longe um valor de $X$ está de sua média.
Também é usado para normalização (escalonamento/*"standardzation"*).

Se $X$ é uma variável aleatória normal com $E(X) = \mu$ e $V(X) = \sigma^2$, a variável aleatória
$$Z = \frac{X - \mu}{\sigma}$$

será uma variável aleatória normal, com $E(Z) = 0$ e $V(Z) = 1$. Ou seja, $Z$ é uma variável aleatória padrão.

## Distribuição Exponencial

## Distribuição de Erlang e Gama

## Distribuição de Weibull

## Distribuição Lognormal

## Distribuição Beta