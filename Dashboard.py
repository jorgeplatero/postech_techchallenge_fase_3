#para rodar o aplicativo a aplicação: python -m streamlit run Dashboard.py

#libs
import streamlit as st
import pandas as pd
import json
from pyspark.sql import SparkSession
from pyspark import SparkConf

#libs gráficas
import plotly.express as px
from plotly.subplots import make_subplots


#funções
def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'


def _initialize_spark() -> SparkSession:
    conf = SparkConf().setAppName('Dashboard').setMaster('local')
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    return spark


#iniciando sessão
spark = _initialize_spark()

#layout
st.set_page_config(layout = 'wide')

#lendo a base de dados
df = spark.read.csv('dados/dados_exportados/dados_uteis/dados_uteis_gz/2023-10-31_pnad_covid_view.csv.gz', sep=',', inferSchema=True, header=True)
df_temp = df.createOrReplaceTempView('df_temp') #criando view temporária na sessão Spark SQL

#tabelas

#aba geral

#mapa de risco
geojson = json.load(open('dados/dados_importados/brasil_estados.json'))
df_qtd_testes_validos_estado = spark.sql(
    '''
        SELECT uf, sigla, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
        GROUP BY uf, sigla
    '''
).toPandas()
df_qtd_testes_positivos_estado = spark.sql(
    '''
        SELECT sigla, count(resultado_teste) AS qtd_testes_positivos
        FROM df_temp 
        WHERE resultado_teste = 'Positivo'
        GROUP BY sigla
    '''
).toPandas()
df_taxa_de_contagio_estado = pd.merge(df_qtd_testes_validos_estado, df_qtd_testes_positivos_estado, on='sigla')
df_taxa_de_contagio_estado['taxa_de_contagio_mil_habitantes'] = ((df_taxa_de_contagio_estado['qtd_testes_positivos'] / df_taxa_de_contagio_estado['qtd_testes_validos']) * 1000).round().astype(int)

#figuras

#aba geral

#mapa de risco
fig_mapa_de_risco = px.choropleth(
    data_frame=df_taxa_de_contagio_estado,
    geojson=geojson,
    locations='sigla',
    color='taxa_de_contagio_mil_habitantes',
    hover_name='sigla',
    scope='south america',
    color_continuous_scale=px.colors.sequential.Reds,
    labels={
        'taxa_de_contagio_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'sigla': 'Estado'
    }
)
fig_mapa_de_risco.add_scattergeo(
    geojson=geojson,
    locations = df_taxa_de_contagio_estado['sigla'],
    text = df_taxa_de_contagio_estado['sigla'],
    textposition='middle center',
    mode = 'text',
    textfont=dict(
        size=14,
        color='black',
    )
)
fig_mapa_de_risco.update_layout(
    title='<b>Mapa de risco conforme taxa de incidência nos estados</b>',
    autosize=False,
    margin = dict(
        l=0,
        r=0,
        b=0,
        t=50,
        autoexpand=True
    )
)

#visualização no streamlit

#título
st.title('DASHBOARD PNAD_COVID 19 IBGE :mask:')

#layout do aplicativo
aba1 , aba2, aba3, aba4 = st.tabs(['Geral', 'Características clínicas', 'Características comportamentais', 'Características econômicas'])

#aba geral
with aba1:
    #mapa de risco
    st.plotly_chart(fig_mapa_de_risco, use_container_width = True)

#aba características clínicas

#aba características comportamentais

#aba características econômicas