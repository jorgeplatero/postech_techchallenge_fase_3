#para rodar o aplicativo a aplicação: python -m streamlit run Dashboard.py

#libs
import streamlit as st
import pandas as pd
import json
from pyspark.sql import SparkSession
import findspark

#libs gráficas
import plotly.express as px
from plotly.subplots import make_subplots


#iniciando sessão
spark = SparkSession.builder.master('local[*]').getOrCreate()

#layout
st.set_page_config(layout = 'wide')


#lendo a base de dados
@st.cache(suppress_st_warning=True)
def expensive_computation():
    df = spark.read.csv('dados/dados_exportados/dados_uteis/dados_uteis_gz/2023-11-01_pnad_covid_view.csv.gz', sep=',', inferSchema=True, header=True)
    return df.createOrReplaceTempView('df_temp')


df_temp = expensive_computation()

#tabelas

#economia
df_testes_validos_sexo = spark.sql(
    '''
        SELECT sexo, count(resultado_teste) AS qtd_testes_validos
        FROM df_temp 
        WHERE resultado_teste = 'Positivo' OR resultado_teste = 'Negativo' 
        GROUP BY sexo
    '''
    ).toPandas()

df_testes_positivos_sexo = spark.sql(
    '''
        SELECT sexo, count(resultado_teste) AS qtd_testes_positivos
        FROM df_temp 
        WHERE resultado_teste = 'Positivo'
        GROUP BY sexo
    '''
).toPandas()

df_infectados_sexo = pd.merge(df_testes_validos_sexo, df_testes_positivos_sexo, on='sexo')
df_infectados_sexo['percentual_testes_positivos'] = ((df_infectados_sexo.qtd_testes_positivos / df_infectados_sexo.qtd_testes_validos) * 100).round(decimals=2)

fig = px.pie(
    data_frame=df_infectados_sexo.sort_values('percentual_testes_positivos', ascending=False), 
    values = 'percentual_testes_positivos', 
    names = 'sexo',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'percentual_testes_positivos':'Percentual de testes positivos',
        'sexo':'Sexo'
    }
)

fig.update_layout(
    title='<b>Porcentagem de infectados por sexo</b>',
    legend_title='Legenda',
    width=800, 
    height=600
)

#visualização no streamlit

#logo fiap
st.image('img/fiap.png')

#título
st.title('DASHBOARD PNAD-COVID-19 IBGE :mask:')

#layout do aplicativo
aba1, aba2, aba3 = st.tabs(['Características clínicas', 'Características comportamentais', 'Características econômicas'])

#aba características clínicas
with aba3:
    #mapa de risco
    st.plotly_chart(fig, use_container_width = True)
#aba características comportamentais
