# DataViz com Análise de Indicadores do PNAD-COVID-19 para o Planejamento de Ações de Combate ao Surto da Doença

## Descrição do Projeto

A pandemia da COVID-19 representou um teste de estresse sem precedentes para os sistemas de saúde em todo o mundo. No Brasil, mostrou diversas fragilidades na infraestrutura dos hospitais particulares e do SUS, mostrando que não estávamos preparados para um surto dessa magnitude. Diante disso, é fundamental extrairmos as lições aprendidas e nos prepararmos melhor para possíveis novas ondas que possam vir a aparecer. Nesse contexto, dados confiáveis são fundamentais para entender os principais gargalos e necessidades da população durante a pandemia.

A PNAD COVID-19, realizada pelo IBGE, é uma das principais fontes de informação sobre os brasileiros que dispomos para análise. Este projeto trás insights e ações que os hospitais podem tomar para o caso de um novo surto.

O projeto conta com as seguintes características:

- Utilização de no máximo 20 questionamentos realizados na pesquisa.
- Utilização de 3 meses para construção da solução.
- Caracterização dos sintomas clínicos da população.
- Caracterização do comportamento da população diante da doença.
- Caracterização de aspectos socioeconômicos.
- Características geoespaciais.

## Arquitetura do projeto

### Banco de dados

O banco de dados foi desenvolvido no MySQL com o objetivo de centralizar as informações disponíveis na pesquisa PNAD-COVID-19 do IBGE. Optou-se por incluir todos os dados da pesquisa no banco de dados e, desses, extrair para análise somente os dados referentes aos meses de setembro, outubro e novembro de 2020. O esquema foi desenhado de modo que fosse permitido a inclusão de novos dados, para o caso em que haja continuação da pesquisa.

**Estrutura do banco de dados**

O banco de dados é composto por uma tabela principal (dados_covid) que armazena todos os dados da pesquisa e tabelas auxiliares, que guardam as respostas obtidas para os questionamentos da pesquisa.

Todas as tabelas seguem como padrão o nome das colunas presentes na dados_covid, como por exemplo a coluna V1022, que representa a situação do domicílio, faz o relacionamento com a tabela V1022 na coluna V1022_id, o mesmo acontece para a tabela C016, que representa o principal motivo de não ter procurado trabalho na semana passada, faz o relacionamento com a tabela C016 na coluna C016_id, e assim por diante para as demais tabelas.

As tabelas auxiliares abaixo guardam múltiplos relacionamentos, pois muitos dos questionamentos da pesquisa têm como resposta um mesmo conjunto de opções.

depara_respostas: guarda o conjunto de respostas "Sim", "Não", "Não sabe", “Ignorado” e "Não aplicável".
depara_resultado_covid: guarda o conjunto de respostas "Positivo", "Negativo", "Inconclusivo", "Ainda não recebeu o resultado" e "Ignorado".
A tabela “dados_covid” possui chaves estrangeiras que relacionam os campos que possuem um mesmo conjunto de respostas às tabelas auxiliares acima. Houve a inserção de índices únicos (UNIQUE KEYS) nas tabelas para evitar duplicidade de dados, permitindo assim a inserção de novos dados. Cada linha da tabela dados_covid representa o conjunto de respostas de um entrevistado.

**Tabelas**

dados_covid - armazena os dados da pesquisa:

- id - chave primária;
- ano – ano da pesquisa;
- uf - sigla da unidade da federação;
- ...demais campos da pesquisa.

depara_respostas - armazena as respostas padronizadas:

- id - chave primária;
- respostas_id - valores;
- name - "Sim", "Não", "Não sabe", "Ignorado", "Não aplicável".

depara_resultado_covid - armazena os sintomas investigados:

- id - chave primária;
- respostas_id – valores;
- name - "Positivo", "Negativo", "Inconclusivo", "Ainda não recebeu o resultado" e "Ignorado".

V1022 – armazena a situação do domicílio depara_resultado_covid - armazena os sintomas investigados:

- id - chave primária;
- V1022_id – valores;
- name – “Urbana” e “Rural”.

Em síntese, o banco de dados foi modelado visando integridade e flexibilidade para as consultas. As tabelas auxiliares e a view agregam valor ao permitir padronização e consulta orientada para análise. A estrutura foi pensada para receber dados de pesquisas futuras, garantindo a continuidade do uso do banco.

### ETL dos dados

Os dados foram inseridos no MySQL por meio de uma conexão python utilizando a biblioteca SQLAlchemy.

```python
from sqlalchemy import create_engine


def mysql_connection(host, user, passwd, database=None):
    engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
    return engine.connect()
mysql = mysql_connection('127.0.0.1', 'root', '<senha>', 'pnad_covid')
```

Para melhorar a performance diante da grande quantidade de dados a serem processados, utilizou-se o framework Apache Spark para leitura, pré-processamento dos dados brutos e seguimentação dos mesmos. Assim foi possível realizar a inserção dos dados por meio da conexão python.

```python
from sqlalchemy.sql import text


df.to_sql('dados_covid', mysql, if_exists='append', index=False)
mysql.execute(text('COMMIT'))
```

### View

Uma view (pnad_covid_view) foi criada com o objetivo de facilitar consultas aos dados. Essa traz somente os dados os meses de setembro, outubro e novembro de campos consideradas mais relevantes para a análise, assim é possível manipular os dados de forma ágil, sem a necessidade de consultar a estrutura integral do banco.

### Processamento dos dados

A consulta dos dados da view foi realizada por meio da funcionalidade SQL do Apache Spark e, para otimizar o processamento, os resultados das queries foram exportados para arquivos CSV. Desse modo, evitou-se a leitura integral dos dados para geração de indicadores.

### Data Viz

Os indicadores gerados foram ilustrados por meio da biblioteca plotly. O plotly é uma biblioteca de Data Viz interativa, por meio da qual é possível acessar mais do que os dados aparentes e estáticos em gráficos convencionais, o que contribui com a compreensão dos mesmos.

## Tecnologias Utilizadas

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="50" height="50"/> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg" width="50" height="50"/> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" width="50" height="50"/>

## Fontes de Dados

Link para a base de dados: <a style="text-decoration:none;" href="https://covid19.ibge.gov.br/pnad-covid/" target="_blank">link</a>.

## Link para a Aplicação

Dashboard Streamlit: <a style="text-decoration:none;" href="https://postechtechchallengefase3-nvadkgperqxqkzu835k6er.streamlit.app/" target="_blank">link</a>.

## Colaboradores

https://github.com/mateus-albuquerque

https://github.com/adriellytsilva
