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
    locations=df_taxa_de_contagio_estado['sigla'],
    text=df_taxa_de_contagio_estado['sigla'],
    textposition='middle center',
    mode='text',
    textfont=dict(
        size=14,
        color='black',
        
    )
)
fig_mapa_de_risco.update_layout(
    title='<b>Taxa de incidência nos estados (por mil habitantes)</b>',
    autosize=False,
    margin = dict(
        l=0,
        r=0,
        b=0,
        autoexpand=True
    ),
    width=1600, 
    height=800
)

#iniciando sessão
spark = SparkSession.builder.master('local[*]').getOrCreate()

#visualização no streamlit

#logo fiap
st.image('img/fiap.png')

#título
st.title('DASHBOARD PNAD-COVID-19 IBGE :mask:')

st.plotly_chart(fig_mapa_de_risco, use_container_width = True)