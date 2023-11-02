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
import plotly.graph_objects as go


#iniciando sessão
findspark.init()
spark = SparkSession.builder.master('local[*]').getOrCreate()

#layout
st.set_page_config(layout = 'wide')

#lendo a base de dados
df = spark.read.csv('dados/dados_exportados/dados_uteis/dados_uteis_gz/2023-11-01_pnad_covid_view.csv.gz', sep=',', inferSchema=True, header=True)
df_temp = df.createOrReplaceTempView('df_temp')

#figuras

#características gerais

#sexo

#qtd
df_qtd_testes_positivos_sexo = spark.sql(
    '''
        SELECT sexo, count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
        GROUP BY sexo
    '''
).toPandas()
fig_qtd_testes_positivos_sexo = px.bar(
    data_frame=df_qtd_testes_positivos_sexo.sort_values('qtd_testes_positivos', ascending=False), 
    x = 'sexo', 
    y = 'qtd_testes_positivos',
    color='sexo',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'sexo': 'Sexo'
    }
)
fig_qtd_testes_positivos_sexo.update_layout(
    title='<b>Quantidade de infectados por sexo</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual
df_qtd_testes_validos_sexo = spark.sql(
    '''
        SELECT sexo, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
        GROUP BY sexo
    '''
).toPandas()
df_taxa_incidencia_sexo = pd.merge(df_qtd_testes_validos_sexo, df_qtd_testes_positivos_sexo, on='sexo')
df_taxa_incidencia_sexo['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_sexo['qtd_testes_positivos'] / df_taxa_incidencia_sexo['qtd_testes_validos']) * 1000).round().astype(int)
fig_taxa_incidencia_sexo = px.pie(
    data_frame=df_taxa_incidencia_sexo.sort_values('taxa_incidencia_mil_habitantes', ascending=False), 
    values = 'taxa_incidencia_mil_habitantes', 
    names = 'sexo',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes':'Taxa de incidência por (mil habitantes)',
        'sexo':'Sexo'
    }
)
fig_taxa_incidencia_sexo.update_layout(
    title='<b>Diferença percentual da taxa de incidência por sexo</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)

#cor/raça

#qtd
df_qtd_testes_positivos_cor_raca = spark.sql(
    '''
        SELECT cor_raca, count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo' AND cor_raca != 'Ignorado'
        GROUP BY cor_raca
    '''
).toPandas()
fig_qtd_testes_positivos_cor_raca = px.bar(
    data_frame=df_qtd_testes_positivos_cor_raca.sort_values('qtd_testes_positivos', ascending=False), 
    x = 'cor_raca', 
    y = 'qtd_testes_positivos',
    color='cor_raca',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'cor_raca': 'Cor/raça'
    }
)
fig_qtd_testes_positivos_cor_raca.update_layout(
    title='<b>Quantidade de infectados por cor/raça</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual
df_qtd_testes_validos_cor_raca = spark.sql(
    '''
        SELECT cor_raca, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo') AND cor_raca != 'Ignorado'
        GROUP BY cor_raca
    '''
).toPandas()
df_taxa_incidencia_cor_raca = pd.merge(df_qtd_testes_validos_cor_raca, df_qtd_testes_positivos_cor_raca, on='cor_raca')
df_taxa_incidencia_cor_raca['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_cor_raca['qtd_testes_positivos'] / df_taxa_incidencia_cor_raca['qtd_testes_validos']) * 1000).round().astype(int)
fig_taxa_incidencia_cor_raca = px.pie(
    data_frame=df_taxa_incidencia_cor_raca.sort_values('taxa_incidencia_mil_habitantes', ascending=False), 
    values = 'taxa_incidencia_mil_habitantes', 
    names = 'cor_raca',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência por (mil habitantes)',
        'cor_raca': 'Cor/raça'
    }
)
fig_taxa_incidencia_cor_raca.update_layout(
    title='<b>Diferença percentual da taxa de incidência por cor/raça</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)

#escolaridade

#qtd
df_qtd_testes_positivos_escolaridade = spark.sql(
    '''
        SELECT escolaridade, count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
        GROUP BY escolaridade
    '''
).toPandas()
fig_qtd_testes_positivos_escolaridade = px.bar(
    data_frame=df_qtd_testes_positivos_escolaridade.sort_values('qtd_testes_positivos', ascending=False), 
    x = 'escolaridade', 
    y = 'qtd_testes_positivos',
    color='escolaridade',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'escolaridade': 'Escolaridade'
    }
)
fig_qtd_testes_positivos_escolaridade.update_layout(
    title='<b>Quantidade de infectados por escolaridade</b>',
    legend_title='Legenda',
    xaxis_visible=False,
    width=800, 
    height=600
)
fig_qtd_testes_positivos_escolaridade.update_xaxes(tickangle=45)
#percentual
df_qtd_testes_validos_escolaridade = spark.sql(
    '''
        SELECT escolaridade, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
        GROUP BY escolaridade
    '''
).toPandas()
df_taxa_incidencia_escolaridade = pd.merge(df_qtd_testes_validos_escolaridade, df_qtd_testes_positivos_escolaridade, on='escolaridade')
df_taxa_incidencia_escolaridade['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_escolaridade['qtd_testes_positivos'] / df_taxa_incidencia_escolaridade['qtd_testes_validos']) * 1000).round().astype(int)
fig_taxa_incidencia_escolaridade = px.bar(
    data_frame=df_taxa_incidencia_escolaridade.sort_values('taxa_incidencia_mil_habitantes', ascending=False),
    x='escolaridade',
    y='taxa_incidencia_mil_habitantes',
    color='escolaridade',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência por (mil habitantes)',
        'escolaridade': 'Escolaridade'
    }
)
fig_taxa_incidencia_escolaridade.update_layout(
    title='<b>Diferença percentual da taxa de incidência por escolaridade</b>',
    yaxis_title='%',
    legend_title='Legenda',
    xaxis_visible=False,
    width=800,  
    height=600
)
fig_taxa_incidencia_escolaridade.update_xaxes(tickangle=45)

#características geoespaciais

#nacional

#taxa de incidência
df_qtd_testes_validos = spark.sql(
    '''
        SELECT count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
    '''
).toPandas()
df_qtd_testes_positivos = spark.sql(
    '''
        SELECT count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
    '''
).toPandas()
df_taxa_incidencia = df_qtd_testes_validos
df_taxa_incidencia['taxa_incidencia_mil_habitantes'] = ((df_qtd_testes_positivos['qtd_testes_positivos'] / df_qtd_testes_validos['qtd_testes_validos']) * 1000).round().astype(int)

#zona de dimicílio

#qtd
df_qtd_testes_positivos_zona = spark.sql(
    '''
        SELECT situacao_domicilio, count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
        GROUP BY situacao_domicilio
    '''
).toPandas()
fig_qtd_testes_positivos_zona = px.bar(
    data_frame=df_qtd_testes_positivos_zona.sort_values('qtd_testes_positivos', ascending=False),
    x='situacao_domicilio',
    y='qtd_testes_positivos',
    color='situacao_domicilio',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'situacao_domicilio': 'Zona de domicílio'
    }
)
fig_qtd_testes_positivos_zona.update_layout(
    title='<b>Quantidade de infectados por zona de domicílio</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual
df_qtd_testes_validos_zona = spark.sql(
    '''
        SELECT situacao_domicilio, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
        GROUP BY situacao_domicilio
    '''
).toPandas()
df_taxa_incidencia_zona = pd.merge(df_qtd_testes_validos_zona, df_qtd_testes_positivos_zona, on='situacao_domicilio')
df_taxa_incidencia_zona['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_zona['qtd_testes_positivos'] / df_taxa_incidencia_zona['qtd_testes_validos']) * 1000).round().astype(int)
fig_taxa_incidencia_zona = px.pie(
    data_frame=df_taxa_incidencia_zona.sort_values('taxa_incidencia_mil_habitantes', ascending=False),
    values = 'taxa_incidencia_mil_habitantes', 
    names = 'situacao_domicilio',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'situacao_domicilio': 'Zona de domicílio'
    }
)
fig_taxa_incidencia_zona.update_layout(
    title='<b>Diferença percentual da taxa de incidência por zona de domicílio</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)

#região

#qtd
df_qtd_testes_positivos_regiao = spark.sql(
    '''
        SELECT regiao, count(teste_covid) AS qtd_testes_positivos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
        GROUP BY regiao
    '''
).toPandas()
fig_qtd_testes_positivos_regiao = px.bar(
    data_frame=df_qtd_testes_positivos_regiao.sort_values('qtd_testes_positivos', ascending=False),
    x='regiao',
    y='qtd_testes_positivos',
    color='regiao',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'regiao': 'Região'
    }
)
fig_qtd_testes_positivos_regiao.update_layout(
    title='<b>Quantidade de infectados por região</b>',
    showlegend=False,
    width=800, 
    height=600
)
fig_qtd_testes_positivos_regiao.update_xaxes(tickangle=45)
#percentual
df_qtd_testes_validos_regiao = spark.sql(
    '''
        SELECT regiao, count(teste_covid) AS qtd_testes_validos
        FROM df_temp 
        WHERE teste_covid = 'Sim' AND (resultado_teste = 'Positivo' OR resultado_teste = 'Negativo')
        GROUP BY regiao
    '''
).toPandas()
df_taxa_incidencia_regiao = pd.merge(df_qtd_testes_validos_regiao, df_qtd_testes_positivos_regiao, on='regiao')
df_taxa_incidencia_regiao['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_regiao['qtd_testes_positivos'] / df_taxa_incidencia_regiao['qtd_testes_validos']) * 1000).round().astype(int)
fig_taxa_incidencia_regiao = px.pie(
    data_frame=df_taxa_incidencia_regiao.sort_values('taxa_incidencia_mil_habitantes', ascending=False),
    values = 'taxa_incidencia_mil_habitantes', 
    names = 'regiao',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'regiao': 'Região'
    }
)
fig_taxa_incidencia_regiao.update_layout(
    title='<b>Diferença percentual da taxa de incidência por região</b>',
    width=600, 
    height=400
)

#estado

#qtd
df_qtd_testes_positivos_estado = spark.sql(
    '''
        SELECT uf, count(resultado_teste) AS qtd_testes_positivos
        FROM df_temp 
        WHERE resultado_teste = 'Positivo'
        GROUP BY uf
    '''
).toPandas()
fig_qtd_testes_positivos_estado = px.bar(
    data_frame=df_qtd_testes_positivos_estado.sort_values('qtd_testes_positivos', ascending=False),
    x='uf',
    y='qtd_testes_positivos',
    color='uf',
    color_discrete_sequence=['#67000d'],
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'uf': 'Estado'
    }
)
fig_qtd_testes_positivos_estado.update_layout(
    title='<b>Quantidade de infectados por estado</b>',
    yaxis_title='Quantidade de infectados',
    showlegend=False,
    width=800, 
    height=600
)
fig_qtd_testes_positivos_estado.update_xaxes(tickangle=45)
#mapa de risco por taxa de incidência
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
df_taxa_incidencia_estado = pd.merge(df_qtd_testes_validos_estado, df_qtd_testes_positivos_estado, on='sigla')
df_taxa_incidencia_estado['taxa_incidencia_mil_habitantes'] = ((df_taxa_incidencia_estado['qtd_testes_positivos'] / df_taxa_incidencia_estado['qtd_testes_validos']) * 1000).round().astype(int)
fig_mapa_risco_taxa_de_incidencia_estado = px.choropleth(
    data_frame=df_taxa_incidencia_estado,
    geojson=geojson,
    locations='sigla',
    color='taxa_incidencia_mil_habitantes',
    hover_name='sigla',
    scope='south america',
    color_continuous_scale=px.colors.sequential.Reds,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência',
        'sigla': 'Estado'
    }
)
fig_mapa_risco_taxa_de_incidencia_estado.add_scattergeo(
    geojson=geojson,
    locations=df_taxa_incidencia_estado['sigla'],
    text=df_taxa_incidencia_estado['sigla'],
    textposition='middle center',
    mode='text',
    textfont=dict(
        size=14,
        color='black',
        
    )
)
fig_mapa_risco_taxa_de_incidencia_estado.update_layout(
    title='<b>Mapa de risco de acordo com a taxa de incidência nos estados</b>',
    autosize=False,
    margin = dict(
        l=0,
        r=0,
        b=0,
        autoexpand=True
    ),
    width=800, 
    height=600
)

#características comportamentais

#busca por orientação médica

#qtd
df_sintomaticos_estabelecimento_saude = spark.sql(
    '''
        SELECT
            count(sintoma_covid) AS qtd_sintomaticos,
            CASE
            WHEN questao_estabelecimento_saude = 'Sim' THEN 'Buscou atendimento'
            WHEN questao_estabelecimento_saude = 'Não' THEN 'Não buscou atendimento'
            WHEN questao_estabelecimento_saude = 'Ignorado' THEN 'Ignorado'
            ELSE 'Não aplicável'
            END AS estabelecimento_saude
        FROM df_temp
        WHERE sintoma_covid = 'Sim' AND (questao_estabelecimento_saude != 'Não aplicável' AND questao_estabelecimento_saude != 'Ignorado')
        GROUP BY estabelecimento_saude
    '''
).toPandas()
fig_qtd_sintomaticos_estabelecimento_saude = px.bar(
    data_frame=df_sintomaticos_estabelecimento_saude.sort_values('qtd_sintomaticos', ascending=False), 
    x='estabelecimento_saude', 
    y='qtd_sintomaticos',
    color='estabelecimento_saude',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'estabelecimento_saude': 'Comportamento'
    }
)
fig_qtd_sintomaticos_estabelecimento_saude.update_layout(
    title='<b>Quantidade de sintomáticos que buscaram atendimento médico</b>',
    showlegend=False,
    width=600,
    height=400
)
#percentual
fig_percentual_sintomaticos_estabelecimento_saude = px.pie(
    data_frame=df_sintomaticos_estabelecimento_saude.sort_values('qtd_sintomaticos', ascending=False), 
    values='qtd_sintomaticos', 
    names='estabelecimento_saude',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'estabelecimento_saude': 'Comportamento'
    }
)
fig_percentual_sintomaticos_estabelecimento_saude.update_layout(
    title='<b>Percentual de sintomáticos que buscaram atendimento médico</b>',
    width=600,
    height=400
)

#medidas de isolamento social

#qtd
df_sintomaticos_permaneceu_casa = spark.sql(
    '''
        SELECT questao_permaneceu_casa, count(sintoma_covid) as qtd_sintomaticos
        FROM df_temp 
        WHERE sintoma_covid = 'Sim' AND (questao_permaneceu_casa = 'Sim' OR questao_permaneceu_casa = 'Não')
        GROUP BY questao_permaneceu_casa
    '''
).toPandas()
fig_qtd_sintomaticos_permaneceu_casa = px.bar(
    data_frame=df_sintomaticos_permaneceu_casa.sort_values('qtd_sintomaticos', ascending=False), 
    x='questao_permaneceu_casa', 
    y='qtd_sintomaticos',
    color='questao_permaneceu_casa',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'questao_permaneceu_casa': 'Isolamento'
    }
)
fig_qtd_sintomaticos_permaneceu_casa.update_layout(
    title='<b>Quantidade de pacientes sintomáticos que adotaram medida de isolamento social</b>',
    showlegend=False,
    width=600, 
    height=400
)
#percentual
fig_percentual_sintomaticos_permaneceu_casa = px.pie(
    data_frame=df_sintomaticos_permaneceu_casa, 
    values = 'qtd_sintomaticos', 
    names = 'questao_permaneceu_casa',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'questao_permaneceu_casa': 'Isolamento'
    }
)
fig_percentual_sintomaticos_permaneceu_casa.update_layout(
    title='<b>Percentual de pacientes sintomáticos que adotaram medida de isolamento social</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual região
df_sintomaticos_permaneceu_casa_regiao = spark.sql(
    '''
        SELECT regiao, questao_permaneceu_casa, count(sintoma_covid) as qtd_sintomaticos
        FROM df_temp 
        WHERE sintoma_covid = 'Sim' AND questao_permaneceu_casa = 'Sim'
        GROUP BY regiao, questao_permaneceu_casa
    '''
).toPandas()
fig_sintomaticos_permaneceu_casa_regiao = px.pie(
    data_frame=df_sintomaticos_permaneceu_casa_regiao, 
    values = 'qtd_sintomaticos', 
    names = 'regiao',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'regiao': 'Região'
    }
)
fig_sintomaticos_permaneceu_casa_regiao.update_layout(
    title='<b>Porcentagem de pacientes sintomáticos que adotaram medida de isolamento social por região</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual estado
df_sintomaticos_permaneceu_casa_estado = spark.sql(
    '''
        SELECT uf, questao_permaneceu_casa, count(sintoma_covid) as qtd_sintomaticos
        FROM df_temp 
        WHERE sintoma_covid = 'Sim' AND questao_permaneceu_casa = 'Sim'
        GROUP BY uf, questao_permaneceu_casa
    '''
).toPandas()
fig_sintomaticos_permaneceu_casa_estado = px.bar(
    data_frame=df_sintomaticos_permaneceu_casa_estado.sort_values('qtd_sintomaticos', ascending=False), 
    x='uf',
    y='qtd_sintomaticos',
    color='uf',
    color_discrete_sequence=['#67000D'],
    labels={
        'qtd_sintomaticos': 'Quantidade',
        'uf': 'Estado'
    }
)
fig_sintomaticos_permaneceu_casa_estado.update_layout(
    title='<b>Percentual de pacientes sintomáticos que adotaram medida de isolamento social por estado</b>',
    yaxis_title='%',
    showlegend=False,
    width=1000, 
    height=600
)
fig_sintomaticos_permaneceu_casa_estado.update_xaxes(tickangle=45)
#
df_testes_positivos_automedicacao = spark.sql(
    '''
        SELECT  
            questao_remedio_conta_propria AS resposta,
            count(questao_remedio_conta_propria) AS qtd_automedicacao
        FROM df_temp
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo' AND questao_remedio_conta_propria = 'Sim' AND questao_remedio_orientacao_medica = 'Não'
        GROUP BY resposta
    '''
).toPandas()
df_testes_positivos_medicacao_orientada = spark.sql(
    '''
        SELECT  
            questao_remedio_orientacao_medica AS resposta,
            count(questao_remedio_orientacao_medica) AS qtd_medicacao_orientada
        FROM df_temp
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo' AND questao_remedio_orientacao_medica = 'Sim' AND questao_remedio_conta_propria = 'Não'
        GROUP BY resposta
    '''
).toPandas()
df_testes_positivos_medicacao_ambos = spark.sql(
    '''
        SELECT  
            questao_remedio_orientacao_medica AS resposta,
            count(questao_remedio_orientacao_medica) AS questao_remedio_ambos
        FROM df_temp
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo' AND questao_remedio_orientacao_medica = 'Sim' AND questao_remedio_conta_propria = 'Sim'
        GROUP BY resposta
    '''
).toPandas()
df_testes_positivos_medicacao = df_testes_positivos_automedicacao.merge(df_testes_positivos_medicacao_orientada, on='resposta')
df_testes_positivos_medicacao = df_testes_positivos_medicacao.merge(df_testes_positivos_medicacao_ambos, on='resposta')
fig_testes_positivos_medicacao = go.Figure(data=[
    go.Bar(name='Automedicados', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.qtd_automedicacao),
    go.Bar(name='Medicados com orientação médica', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.qtd_medicacao_orientada),
    go.Bar(name='Ambos', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.questao_remedio_ambos)   
    ]
)
fig_testes_positivos_medicacao.update_layout(
    title='<b>Quantidade de infectados automedicados e medicados com orientacao médica</b>',
    legend_title='Legenda',
    yaxis_title='Quantidade',
    xaxis_visible=False,
    width=800,
    height=600
)
fig_testes_positivos_medicacao.data[0].marker.color = ['#67000d',] * 2
fig_testes_positivos_medicacao.data[1].marker.color = ['#A50F15',] * 2 
fig_testes_positivos_medicacao.data[2].marker.color = ['#FB6A4A',] * 2 


#características clínicas

#sintomátios e assintomáticos
#percentual
df_percentual_testes_positivos_sintomaticos = spark.sql(
    '''
        SELECT 
            CASE
            WHEN sintoma_covid = 'Sim' THEN 'Sintomáticos'
            ELSE 'Assintomáticos' 
            END AS sintoma_covid,
            count(resultado_teste) AS qtd_testes_positivos
        FROM df_temp
        WHERE teste_covid = 'Sim' AND resultado_teste = 'Positivo'
        GROUP BY sintoma_covid
    '''
).toPandas()
fig_percentual_testes_positivos_sintomaticos = px.pie(
    data_frame=df_qtd_testes_positivos_sintomaticos.sort_values('qtd_testes_positivos', ascending=False),
    values = 'qtd_testes_positivos',
    names = 'sintoma_covid',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos':'Quantidade',
        'sintoma_covid':'Condição'
    }
)
fig_percentual_testes_positivos_sintomaticos.update_traces(
    pull=[0.1, 0]

)
fig_percentual_testes_positivos_sintomaticos.update_layout(
    title='<b>Percentual de infectados sintomáticos e assintomáticos</b>',
    legend_title='Legenda',
    width=600,
    height=400
)

#características econômicas

#visualização no streamlit

#logo fiap
st.image('img/fiap.png')

#título
st.title('DASHBOARD PNAD-COVID-19 IBGE :microscope:')

#layout do aplicativo
aba1, aba2, aba3, aba4, aba5 = st.tabs(['Características gerais', 'Características clínicas', 'Características comportamentais', 'Características econômicas', 'Caracteríticas geoespaciais'])

#aba características gerais
with aba1:
    #sexo
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        #bar
        st.plotly_chart(fig_qtd_testes_positivos_sexo, use_container_width=True)
    with coluna2:
        #pie
        st.plotly_chart(fig_taxa_incidencia_sexo, use_container_width=True)
    st.markdown(
        '''
            Verifica-se que houve mais contaminação no grupo de mulheres validamente testadas.
        '''
    )
    #cor/raça
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        #bar
        st.plotly_chart(fig_qtd_testes_positivos_cor_raca, use_container_width=True)
    with coluna4:
        #pie
        st.plotly_chart(fig_taxa_incidencia_cor_raca, use_container_width=True)
    st.markdown(
        '''
            Verifica-se que houve mais contaminação no grupo de mulheres validamente testadas.
        '''
    )

    st.plotly_chart(fig_qtd_testes_positivos_escolaridade, use_container_width =False)
    st.plotly_chart(fig_taxa_incidencia_escolaridade, use_container_width =False)

#aba características clínicas
with aba2:
    st.plotly_chart(fig_percentual_testes_positivos_sintomaticos, use_container_width=True)
    st.markdown(
        '''
            texto.
        '''
    )

#aba características comportamentais
with aba3:
    #busca por orientação médica
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        #bar
        st.plotly_chart(fig_qtd_sintomaticos_estabelecimento_saude, use_container_width=True)
    with coluna2:
        #pie
        st.plotly_chart(fig_percentual_sintomaticos_estabelecimento_saude, use_container_width=True)
    st.markdown(
        '''
            texto.
        '''
    )
    #medidas de isolamento social
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        #bar
        st.plotly_chart(fig_qtd_sintomaticos_permaneceu_casa, use_container_width=True)
    with coluna4:
        #pie
        st.plotly_chart(fig_percentual_sintomaticos_permaneceu_casa, use_container_width=True)
    st.markdown(
        '''
            texto.
        '''
    )
    st.plotly_chart(fig_sintomaticos_permaneceu_casa_regiao, use_container_width=True)
    st.plotly_chart(fig_sintomaticos_permaneceu_casa_estado, use_container_width=True)
    st.markdown(
        '''
            texto.
        '''
    )
    st.plotly_chart(fig_testes_positivos_medicacao, use_container_width=False)

#aba características econômicas
with aba4:
    #m
    st.plotly_chart(fig_taxa_incidencia_sexo, use_container_width=True)

#aba características geoespaciais
with aba5:
    st.markdown(
        '''
            ## Indicadores geoespaciais
            Essa seção é dedicada aos indicadores geoespaciais obtidos por meio da análise de dados da pesquisa
        '''
    )
    #nacional
    st.metric('Média da taxa de incidência nos estados', df_taxa_incidencia['taxa_incidencia_mil_habitantes'].mean().astype(int))
    #zona de domicílio
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        #bar
        st.plotly_chart(fig_qtd_testes_positivos_zona, use_container_width=True)
    with coluna2:
        #pie
        st.plotly_chart(fig_taxa_incidencia_zona, use_container_width=True)
    #região
    st.metric('Média da taxa de incidência nas regiões', df_taxa_incidencia_regiao['taxa_incidencia_mil_habitantes'].mean().astype(int))
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        #bar
        st.plotly_chart(fig_qtd_testes_positivos_regiao, use_container_width=True)
    with coluna4:
        #pie
        st.plotly_chart(fig_taxa_incidencia_regiao, use_container_width=True)
    st.markdown(
        '''
            As regiões norte obteve...
        '''
    )
    #estado
    st.metric('Média da taxa de incidência nos estados', df_taxa_incidencia_estado['taxa_incidencia_mil_habitantes'].mean().astype(int))
    #bar
    st.plotly_chart(fig_qtd_testes_positivos_estado, use_container_width=False)
    #choropleth
    #mapa de risco
    st.plotly_chart(fig_mapa_risco_taxa_de_incidencia_estado, use_container_width=True)


