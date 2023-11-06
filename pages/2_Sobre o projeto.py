import streamlit as st
import pandas as pd

df_amostra_view = pd.read_csv('dados/dados_streamlit/df_amostra_view.csv', sep=',')

st.image('img/fiap.png')
st.title('Sobre o projeto')
st.markdown(
    '''
        <div style='text-align: justify;'>
            <h3>Banco de dados</h3>
            <p>
                O banco de dados foi desenvolvido no MySQL com o objetivo de centralizar as informações disponíveis na pesquisa PNAD-COVID-19 do IBGE. Optou-se por incluir todos os dados da pesquisa no banco de dados e, desses, extrair para análise somente os dados referentes aos meses de setembro, outubro e novembro de 2020. O esquema foi desenhado de modo que fosse permitido a inclusão de novos dados, para o caso em que haja continuação da pesquisa. 
            </p>
            <h4>Estrutura</h4>
            <p>
                O banco de dados é composto por uma tabela principal (dados_covid) que armazena todos os dados da pesquisa e tabelas auxiliares, que guardam as respostas obtidas para os questionamentos da pesquisa. 
            </p>
            <p>
                Todas as tabelas seguem como padrão o nome das colunas presentes na dados_covid, como por exemplo a coluna V1022, que representa a situação do domicílio, faz o relacionamento com a tabela V1022 na coluna V1022_id, o mesmo acontece para a tabela C016, que representa o principal motivo de não ter procurado trabalho na semana passada, faz o relacionamento com a tabela C016 na coluna C016_id, e assim por diante para as demais tabelas.
            </p>
            <p>
                As tabelas auxiliares abaixo guardam múltiplos relacionamentos, pois muitos dos questionamentos da pesquisa têm como resposta um mesmo conjunto de opções.
                <ul>
                    <li>depara_respostas: guarda o conjunto de respostas "Sim", "Não", "Não sabe", “Ignorado” e "Não aplicável".</li>
                    <li>depara_resultado_covid: guarda o conjunto de respostas "Positivo", "Negativo", "Inconclusivo", "Ainda não recebeu o resultado" e "Ignorado".</li>
                </ul>
            </p>
            <p>
                A tabela “dados_covid” possui chaves estrangeiras que relacionam os campos que possuem um mesmo conjunto de respostas às tabelas auxiliares acima. Houve a inserção de índices únicos (UNIQUE KEYS) nas tabelas para evitar duplicidade de dados, permitindo assim a inserção de novos dados. Cada linha da tabela dados_covid representa o conjunto de respostas de um entrevistado.
            </p>
            <h4>Tabelas</h4>
            <p>
                dados_covid - armazena os dados da pesquisa:
                <ul>
                    <li>id - chave primária;</li>
                    <li>ano – ano da pesquisa;</li>
                    <li>uf - sigla da unidade da federação;</li>
                    <li>...demais campos da pesquisa.</li>
                </ul>
            </p>
            <p>
                depara_respostas - armazena as respostas padronizadas:
                <ul>
                    <li>id - chave primária;</li>
                    <li>respostas_id - valores;</li>
                    <li>name - "Sim", "Não", "Não sabe", "Ignorado", "Não aplicável".</li>
                </ul>
            </p>
            <p>
                depara_resultado_covid - armazena os sintomas investigados:
                <ul>
                    <li>id - chave primária;</li>
                    <li>respostas_id – valores;</li>
                    <li>name - "Positivo", "Negativo", "Inconclusivo", "Ainda não recebeu o resultado" e "Ignorado".</li>
                </ul>
            </p>
            <p>
                V1022 – armazena a situação do domicílio
                depara_resultado_covid - armazena os sintomas investigados:
                <ul>
                    <li>id - chave primária;</li>
                    <li>V1022_id – valores;</li>
                    <li>name – “Urbana” e “Rural”.</li>
                </ul>
            </p>
        </div>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <div style='text-align: justify;'>
        <p>
            Para mais informações acesse o <b><a style='text-decoration:none', href='https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Documentacao'>dicionário</a></b> de dados da PNAD-COVID-19.
        </p> 
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <p>
                Em síntese, o banco de dados foi modelado visando integridade e flexibilidade para as consultas. As tabelas auxiliares e a view agregam valor ao permitir padronização e consulta orientada para análise. A estrutura foi pensada para receber dados de pesquisas futuras, garantindo a continuidade do uso do banco.
            </p>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <h4>Inserção dos dados</h4>
            <p>
                Os dados foram inseridos no MySQL por meio de uma conexão python utilizando a biblioteca SQLAlchemy.
            </p>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        ```
        from sqlalchemy import create_engine

        
        def mysql_connection(host, user, passwd, database=None):
            engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
            return engine.connect()
        mysql = mysql_connection('127.0.0.1', 'root', '<senha>', 'pnad_covid')
        ```
    '''
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <p>
                Para melhorar a performance diante da grande quantidade de dados a serem processados, utilizou-se o framework Apache Spark para leitura, pré-processamento dos dados brutos e seguimentação dos mesmos. Assim foi possível realizar a inserção dos dados por meio da conexão python.
            </p>
        </div>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        ```
        from sqlalchemy.sql import text

        
        df.to_sql('dados_covid', mysql, if_exists='append', index=False)
        mysql.execute(text('COMMIT'))
        ```
    '''
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <h4>View</h4>
            <p>Uma view (pnad_covid_view) foi criada com o objetivo de facilitar consultas aos dados. Essa traz somente os dados os meses de setembro, outubro e novembro de campos consideradas mais relevantes para a análise, assim é possível manipular os dados de forma ágil, sem a necessidade de consultar a estrutura integral do banco.</p>
        </div>
    ''',
    unsafe_allow_html=True
)
df_amostra_view
st.markdown(
    '''
        <div style='text-align: justify;'>
            <h4>Processamento dos dados</h4>
            <p>A consulta dos dados da view foi realizada por meio da funcionalidade SQL do Apache Spark e, para otimizar o processamento, os resultados das queries foram exportados para arquivos CSV. Desse modo, evitou-se a leitura integral dos dados para geração de indicadores.</p>
        </div>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <h4>Data Viz</h4>
            <p>Os indicadores gerados foram ilustrados por meio da biblioteca plotly. O plotly é uma biblioteca de Data Viz interativa, por meio da qual é possível acessar mais do que os dados aparentes e estáticos em gráficos convencionais, o que contribui com a compreensão dos mesmos.</p>
        </div>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
        <div style='text-align: justify;'>
            <p>
                Acesse o <b><a style='text-decoration:none', href='https://github.com/jorgeplatero/postech_techchallenge_fase_3'>repositório</a></b> no GitHub para mais informações.
            </p>
        </div>
    ''',
    unsafe_allow_html=True
)