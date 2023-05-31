# 1. Objetivo do Projeto

Implementar uma solução de ponta a ponta de um fluxo de dados.

A ideia foi executar um ETL com boas práticas de arquitetura 
de software, programação orientada à objetos, testes 
unitários e design patterns. O banco utilizado para armazenar
os dados foi o SQLite.

De forma mais especifica, o projeto consiste em extrair de
informações sobre o filmes da API do TMDB, armazenar e modelar 2 kpis e montar uma visualização para os mesmos.

API: https://developers.themoviedb.org/3/movies/get-movie-details

# 2. Proposta de solução

1. Construir um fluxo de ETL, com a separação de suas 
responsabilidades
2. Armazenar num banco de dados SQLite
3. Criar uma visualização como um dashboard do plotly

# 3. Como rodar o projeto

1. Clone esse repositório na sua máquina.
2. Crie um ambiente virtual.
3. Instale o arquivo `requirements.txt`

```
python3 -m pip install -r requirements.txt
```
4. Rode o arquivo `run.py`.
- Após isso, é esperado que:
    - 1. Um arquivo `myDb.db` seja criado.
    - 2. Uma mensagem `Dados carregados com sucesso!` apareça
    no seu terminal
    - 3. Apareça uma url do Flask como essa `http://127.0.0.1:8050/`. Basta copiar esse link e colocar no seu navegador.
# 4. Descrições
## 4.1 Colunas

1. **"title"** - Título do filme
2. **"genres"** - generos do filme
3. **"budget"** - Orçamento do filme
4. **"original_language"** - lingua original do filme
5. **"original_title"** - titulo original do filme
6. **"vote_average"** - A média de votos atribuídos ao filme pelos usuários do TMDb.
7. **"vote_count"** - O número total de votos recebidos pelo filme.
8. **"popularity"** - A popularidade do filme no TMDb em porcentagem
9. **"revenue"** - A receita gerada pelo filme em dólares
10. **"release_date"** - data de lancamento
11. **"status"** - O status de produção do filme (por exemplo, "Lançado", "Previsto", etc.).
12. **"runtime"** - duração do filme em minutos

## 4.2 KPIs

**Distribuição de Gêneros Mais Populares**: Esse KPI analisa a distribuição dos gêneros mais populares na base de dados do TMDB. Ele pode ajudar a identificar quais gêneros têm maior demanda e popularidade entre os usuários. 

**Lucro**: o Lucro é uma métrica importante para saber se o
filme de fato valeu a pena ser feito. Sendo ele a diferença
entre a receita e o orçamento.

## 4.3 Estrutura do Projeto

- src: Pasta principal
- drivers: Repositório relacionado as requisições e sua interface.
- Infra: Repositório relacionado a conecção e operação com o
banco de dados
- main: Repositório responsável por implementar o pipeline
principal
- stages: Relacionado aos estágio de extração, 
transformação, carregamento dos dados e visualização dos 
dados.
- tests: Testes unitários.


```.
├── app.py
├── install.sh
├── main.py
├── raw.py
├── README.md
├── requirements.txt
├── run.py
├── src
│   ├── drivers
│   ├── infra
│   ├── __init__.py
│   ├── main
│   ├── stages
│   └── tests
```