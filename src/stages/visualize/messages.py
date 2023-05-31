msg1 = """
    Esse primeiro grafico é referente aos generos que mais aparecem
    nos filmes. """

msg2 = """
    Esse KPI analisa os gêneros dos filmes presentes na
    base de dados do TMDB e identifica qual gênero possui
    a maior quantidade de filmes. Pode ser útil para 
    entender as preferências do público em relação aos 
    gêneros cinematográficos. Vemos por exemplo que o gênero 'Drama'
    está associado à uma grande quantidade de filmes. Pode sugerir que as 
    pessoas tem uma preferência para filmes que entreguem tal experiência.
"""

msg3 = """
    Como foi obtida essa informação:
        Sabemos que cada filme possue mais de um gênero associado.
        Dito isso, separei de forma única cada gênero presente em cada
        filme e fiz essa contagem. Ou seja, para o filme "Vingadores" 
        por exemplo,
        que tem como gênero "ação" e "drama", foi contabilizado 1 uma contagem
        para "ação" e uma para "drama"
"""

msg4 = """
    Esse Gráfico é referente à quantidade de filmes que foi
    lucrativo, prejuízo ou nenhum dos dois.
"""

msg5 = """
    Serve para ter uma ideia do quão lucrativa está sendo
    a plataforma que hospeda tais filmes e definir metas. Vemos que temos uma
    quantidade bem maior de filmes que dão lucro
    em compração às outras categorias.
    Então a ideia para esse KPI é tentar máximizar essa diferença. 
    Em outras palavras,
    fazer filmes que de fato vão dar lucro.
"""

msg6 = """
    Como foi obtida essa informação:
    Temos no banco de dados informações sobre a receita e sobre o
    orçamento, fazendo uma subtração da receita pelo orçamento temos o lucro.
    Então classifiquei os filmes com essa informação.
"""
