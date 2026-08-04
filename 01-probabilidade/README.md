# Definições de probabilidade

O início do livro *Probability, Random Variables, And Stochastic Processes* (4 ed.) do Papoulis (1921), Pillai (2002) diz:
> The theory of probability deals with averages of mass phenomena occurring sequentially and simultaneously, e.g. electron emission, system failure, turbulence, among many others. It has been **observed** that in these and other fields certain averages **approach a constant value** as the number of observation increases and this value remains the same (...).

## Espaços amostrais e eventos

## Definição baseada na frequência relativa

A probabilidade $P(E)$ de um evento $E$ é o limite:
$$P(E) = \lim_{n \rightarrow \infty} \frac{n_e}{n}$$
Em que $n_e$ é o número de ocorrências de $E$ e $n$ é o número de tentativas.
Essa abordagem pode ser usada apenas como hipótese, mas não como base de construção da teoria probabilística, por mais que sejam feitos muitos experimentos.

Problema: Vamos fazer um paralelo com a definição de uma resistência $R$. Podemos usar o limite:
$$R = \lim_{n \rightarrow \infty} \frac{v(t)}{i_n (t)}$$
Em que $v(t)$ é uma fonte de tensão e $i_n(t)$ são as correntes de uma sequência de resistores reais que tendem a um elemento (de dois terminais) reais.
🧮 A teoria resultante é complexa demais, melhor usar uma abordagem axiomática baseada nas leis de Kirchoff.

## Definição clássica

A probabilidade $P(E)$ de um evento $E$ é determinada, a priori, sem experimentação, a partir da razão:
$$P(E) = \frac{N_E}{N}$$
Em que $N$ é o número de resultados possíveis *(dispostos de maneira igualmente apresentadas)* e $N_E$ é o número de resultados favoráveis para o evento $E$.

⚠️ O problema desta abordagem é a possibilidade de ambiguidade.

# Técnicas de contagem

Vamos resolver o problema do *dispostos de maneira igualmente apresentada* da definição clássica.
💡Para isso, vamos usar combinatória.

# Axiomas de probabilidade

Axiomas propostos por Kolmogorov (1933).
Probabilidade é um número que é atribuído a cada membro de uma coleção de eventos, a partir de um experimento aleatório que satisfaça as seguintes propriedades:
1. $P(S) = 1$ em que $S$ é o espaço amostral
2. $0 \leq P(E) \leq 1$ para qualquer evento $E$
3. Para dois eventos $E_1$ e $E_2$ com $E_1 \cap E_2 = \varnothing$, temos que $P(E_1 \cup E_2) = P(E_1) + P(E_2)$

# Álgebra da probabilidade

# Probabilidade condicional

# Interseção de eventos

# Independência

# Teorema de Bayes

# Variáveis aleatórias