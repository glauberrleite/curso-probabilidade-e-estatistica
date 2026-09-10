Este documento apresenta a demonstração de média e variância da distribuição uniforme discreta.

📚 Serve de material complementar para a aula de variáveis aleatórias discretas

Temos que uma variável $X$ que segue uma distribuição uniforme discreta $U(x; a, b)$ tem função de probabilidade:

$$f(x) = \frac{1}{n} \quad \quad \forall x \in [a, b]$$

Em que $n$ é o número de valores no intervalo, ou seja, $n = b - a + 1$ (💡 veja que apenas $b - a$ cortaria a contagem de $a$, por isso o $+1$).

## Cálculo da média

Usando a definição de valor esperado:

$$E[X] = \sum_{x = a}^{b} x f(x) = \sum_{x = a}^{b} x \frac{1}{n} =  \frac{1}{n} \sum_{x = a}^{b} x $$

Como $n = b - a + 1$

$$E[X] = \frac{1}{b - a + 1} \sum_{x = a}^{b} x$$

Conforme sugestão do aluno Yann Kevin (ykpcf@ic.ufal.br), podemos enxergar esse somatório como dois (tomando o cuidado de adicionar $a$ porque a subtração elimina o elemento e estamos em um intervalo fechado):

$$E[X] = \frac{1}{b - a + 1} \left[ \left( \sum_{x = 0}^{b} x \right) - \left( \sum_{x = 0}^{a} x \right) + a \right]$$

Podemos começar com $x = 1$ no somatório, já que $x = 0$ vai somar 0 em cada um dos itens.

$$E[X] = \frac{1}{b - a + 1} \left[ \left( \sum_{x = 1}^{b} x \right) - \left( \sum_{x = 1}^{a} x \right) + a \right]$$

Usando o conceito de [Soma dos Termos de uma Progressão Aritmética](https://www.todamateria.com.br/progressao-aritmetica/), temos:

- $\sum_{x = 1}^{b} x = \frac{(1 + b)b}{2}$
- $\sum_{x = 1}^{a} x = \frac{(1 + a)a}{2}$

Aplicando no cálculo do valor esperado:

$$E[X] = \frac{1}{b - a + 1} \left( \frac{(1 + b)b}{2} - \frac{(1 + a)a}{2} + a \right)$$

$$E[X] = \frac{1}{2} \cdot \frac{b^2 + b - a^2 + a}{b - a + 1}$$

Dividindo os dois elementos (usando a abordagem de [divisão de polinômios](https://mundoeducacao.uol.com.br/matematica/divisao-polinomio-por-polinomio.htm)), temos a relação:

$$b^2 + b - a^2 + a = (b + a)(b - a + 1) + 0$$

Ou seja:

$$E[X] = \frac{b + a}{2}$$

## Cálculo da variância

Para a variância vamos usar a forma computacional (aquela que costuma dar menos trabalho na hora da conta):

$$Var[X] = E[X^2] - \left( E[X] \right)^2$$

💡 Ela não é uma fórmula nova, é a definição $Var[X] = E[(X - \mu)^2]$ depois de abrir o quadrado:

$$E[(X - \mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2$$

Como já descobrimos que $\mu = E[X] = \frac{b + a}{2}$, o único que falta é $E[X^2]$.

Esta demonstração é mais trabalhosa do que a da média, por isso, decidi colocar no formato de passos para não se perder.

### Passo 1: calcular $E[X^2]$

Pela definição de valor esperado de uma função da variável aleatória:

$$E[X^2] = \sum_{x = a}^{b} x^2 f(x) = \sum_{x = a}^{b} x^2 \frac{1}{n} = \frac{1}{b - a + 1} \sum_{x = a}^{b} x^2$$

Repetimos exatamente o truque da média, quebrando o somatório em dois (e de novo devolvendo o termo que a subtração comeu, que agora é $a^2$, porque o intervalo é fechado em $a$):

$$E[X^2] = \frac{1}{b - a + 1} \left[ \left( \sum_{x = 1}^{b} x^2 \right) - \left( \sum_{x = 1}^{a} x^2 \right) + a^2 \right]$$

(já começamos em $x = 1$, porque $0^2 = 0$ e não muda nada)

### Passo 2: a soma dos quadrados

Na média usamos a soma dos termos de uma PA. Aqui precisamos da soma dos quadrados dos primeiros $m$ inteiros:

$$\sum_{x = 1}^{m} x^2 = \frac{m(m + 1)(2m + 1)}{6}$$

💡 Se você nunca viu essa fórmula aparecer do nada, dá para obtê-la. Note que $(x + 1)^3 - x^3 = 3x^2 + 3x + 1$. Somando dos dois lados, de $x = 1$ até $m$, o lado esquerdo colapsa (o $2^3$ cancela com o $2^3$, o $3^3$ com o $3^3$, e assim por diante), sobrando só as pontas:

$$(m + 1)^3 - 1 = 3 \sum_{x = 1}^{m} x^2 + 3 \sum_{x = 1}^{m} x + m$$

Usando a soma da PA $\sum_{x = 1}^{m} x = \frac{m(m+1)}{2}$ e isolando:

$$3 \sum_{x = 1}^{m} x^2 = m^3 + 3m^2 + 2m - \frac{3m^2 + 3m}{2} = \frac{2m^3 + 3m^2 + m}{2} = \frac{m(m + 1)(2m + 1)}{2}$$

$$\sum_{x = 1}^{m} x^2 = \frac{m(m + 1)(2m + 1)}{6}$$

Aplicando as duas somas no nosso valor esperado:

$$E[X^2] = \frac{1}{b - a + 1} \left( \frac{b(b + 1)(2b + 1)}{6} - \frac{a(a + 1)(2a + 1)}{6} + a^2 \right)$$

$$E[X^2] = \frac{1}{6} \cdot \frac{b(b + 1)(2b + 1) - a(a + 1)(2a + 1) + 6a^2}{b - a + 1}$$

Abrindo os produtos, com $m(m + 1)(2m + 1) = 2m^3 + 3m^2 + m$:

$$E[X^2] = \frac{1}{6} \cdot \frac{2b^3 + 3b^2 + b - 2a^3 - 3a^2 - a + 6a^2}{b - a + 1} = \frac{1}{6} \cdot \frac{2b^3 + 3b^2 + b - 2a^3 + 3a^2 - a}{b - a + 1}$$

### Passo 3: dividir os polinômios

De novo caímos numa [divisão de polinômios](https://mundoeducacao.uol.com.br/matematica/divisao-polinomio-por-polinomio.htm), tratando $b$ como a variável e $a$ como constante. Dividindo $2b^3 + 3b^2 + b - 2a^3 + 3a^2 - a$ por $b - a + 1$, passo a passo:

- $2b^3 \div b = 2b^2$; multiplicando de volta e subtraindo, sobra $(2a + 1)b^2 + b - 2a^3 + 3a^2 - a$
- $(2a + 1)b^2 \div b = (2a + 1)b$; multiplicando e subtraindo, sobra $(2a^2 - a)b - 2a^3 + 3a^2 - a$
- $(2a^2 - a)b \div b = 2a^2 - a$; multiplicando e subtraindo, o resto é $0$

Ou seja, a divisão é exata (como tinha que ser, já que o resultado é um valor esperado bem comportado):

$$2b^3 + 3b^2 + b - 2a^3 + 3a^2 - a = (b - a + 1)(2b^2 + 2ab + b + 2a^2 - a) + 0$$

E portanto:

$$E[X^2] = \frac{2b^2 + 2ab + b + 2a^2 - a}{6}$$

💡 Vale conferir com um caso fácil: se $a = b$ (a variável é uma constante $a$), a expressão vira $\frac{2a^2 + 2a^2 + a + 2a^2 - a}{6} = \frac{6a^2}{6} = a^2$, exatamente o que se espera de $E[X^2]$ quando $X$ vale sempre $a$.

### Passo 4: juntar tudo

$$Var[X] = E[X^2] - \left( E[X] \right)^2 = \frac{2b^2 + 2ab + b + 2a^2 - a}{6} - \left( \frac{b + a}{2} \right)^2$$

Colocando no denominador comum $12$ (multiplicando a primeira fração por $\frac{2}{2}$ e a segunda por $\frac{3}{3}$):

$$Var[X] = \frac{2(2b^2 + 2ab + b + 2a^2 - a) - 3(b + a)^2}{12}$$

$$Var[X] = \frac{4b^2 + 4ab + 2b + 4a^2 - 2a - 3b^2 - 6ab - 3a^2}{12}$$

Agrupando os termos semelhantes:

- $4b^2 - 3b^2 = b^2$
- $4ab - 6ab = -2ab$
- $4a^2 - 3a^2 = a^2$
- sobram ainda $2b - 2a$

$$Var[X] = \frac{b^2 - 2ab + a^2 + 2b - 2a}{12}$$

Repare que $b^2 - 2ab + a^2$ é o quadrado da diferença e que $2b - 2a = 2(b - a)$:

$$Var[X] = \frac{(b - a)^2 + 2(b - a)}{12}$$

Por fim, lembrando que $n = b - a + 1$, ou seja, $b - a = n - 1$:

$$Var[X] = \frac{(n - 1)^2 + 2(n - 1)}{12} = \frac{n^2 - 2n + 1 + 2n - 2}{12} = \frac{n^2 - 1}{12}$$

Chegando ao resultado que queríamos:

$$Var[X] = \frac{n^2 - 1}{12} = \frac{(b - a + 1)^2 - 1}{12}$$

💡 Duas leituras rápidas desse resultado:

1. A variância só depende de $n$, isto é, do **tamanho** do intervalo, e não de onde ele está na reta. Faz sentido: jogar um dado de faces $1$ a $6$ ou de faces $101$ a $106$ dá a mesma dispersão, só muda o centro.
2. Se $a = b$, temos $n = 1$ e $Var[X] = \frac{1 - 1}{12} = 0$. Também faz sentido: uma variável que só assume um valor não varia.

## Conferindo com o dado de seis faces

Para $X \sim U(x; 1, 6)$, temos $n = 6 - 1 + 1 = 6$:

$$E[X] = \frac{6 + 1}{2} = 3{,}5 \quad \quad Var[X] = \frac{6^2 - 1}{12} = \frac{35}{12} \approx 2{,}92$$

Na força bruta, $E[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15{,}17$, e $15{,}17 - 3{,}5^2 = 15{,}17 - 12{,}25 = 2{,}92$. ✅

O desvio padrão fica $\sigma = \sqrt{35/12} \approx 1{,}71$, o que é bem razoável para valores espalhados entre $1$ e $6$ em torno de $3{,}5$.
