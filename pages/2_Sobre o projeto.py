import streamlit as st
import pandas as pd

df_amostra_view = pd.read_csv('dados/dados_streamlit/df_amostra_view.csv', sep=',')

st.image('img/fiap.png')
st.title('Sobre o projeto')
st.markdown(
    '''
        ### Banco de dados

        O banco de dados foi desenvolvido no MySQL com o objetivo de centralizar as informações disponíveis na pesquisa PNAD-COVID-19 do IBGE. Optou-se por incluir todos os dados da pesquisa no banco de dados e, desses, extrair para análise somente os dados referentes aos meses de setembro, outubro e novembro de 2020. O esquema foi desenhado de modo que fosse permitido a inclusão de novos dados, para o caso em que haja continuação da pesquisa. 

        #### Estrutura

        O banco de dados é composto por uma tabela principal (dados_covid) que armazena todos os dados da pesquisa e tabelas auxiliares, que guardam as respostas obtidas para os questionamentos da pesquisa. As tabelas auxiliares abaixo guardam multiplos relacionamentos, pois muitos dos questionamentos da pesquisa têm como resposta um mesmo conjunto de opções.
            
        - depara_respostas: guarda o conjunto de respostas "Sim", "Não", "Não sabe", “Ignorado” e "Não aplicável".
        - depara_resultado_covid: guarda o conjunto de respostas "Positivo", "Negativo", "Inconclusivo", "Ainda não recebeu o resultado" e "Ignorado".

        A tabela dados_covid possui chaves estrangeiras que relacionam os campos que possuem um mesmo conjunto de respostas às tabelas auxiliares acima. Houve a inserção de índices únicos (UNIQUE KEYS) nas tabelas para evitar duplicidade de dados, permitindo assim a inserção de novos dados. Cada linha da tabela dados_covid representa o conjunto de respostas de um entrevistado.

        #### Tabelas

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

        #### View

        Uma view (pnad_covid_view) foi criada com o objetivo de facilitar consultas aos dados. Essa traz somente os dados os meses de setembro, outubro e novembro de campos consideradas mais relevantes para a análise, assim é possível manipular os dados de forma ágil, sem a necessidade de consultar a estrutura integral do banco.
    '''
)
df_amostra_view
st.markdown(
    '''
        Em síntese, o banco de dados foi modelado visando integridade e flexibilidade para as consultas. As tabelas auxiliares e a view agregam valor ao permitir padronização e consulta orientada para análise. A estrutura foi pensada para receber dados de pesquisas futuras, garantindo a continuidade do uso do banco.
    '''
)
st.image('img/diagrama.png')
st.markdown('Repositório no **GitHub**: https://github.com/jorgeplatero/postech_techchallenge_fase_3')