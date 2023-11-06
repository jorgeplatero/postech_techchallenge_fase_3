#para rodar o aplicativo a aplicação: python -m streamlit run Dashboard.py

#libs
import streamlit as st
import pandas as pd
import json

#libs gráficas
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


#layout
st.set_page_config(layout = 'wide')

#figuras

#aba características gerais

#qtd de infectados
df_qtd_testes_positivos = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos.csv', sep=',')
#qtd de infectados por sexo
df_qtd_testes_positivos_sexo = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_sexo.csv', sep=',')
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
    title='<b>Casos confirmados de COVID-19 por sexo</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#diferença percentual de infectados por sexo
df_taxa_incidencia_sexo = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_sexo.csv', sep=',')
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
#qtd de infectados por cor/raça
df_qtd_testes_positivos_cor_raca = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_cor_raca.csv', sep=',')
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
    title='Casos confirmados de COVID-19 por cor/raça</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#diferença percentual de infectados por cor/raça
df_taxa_incidencia_cor_raca = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_cor_raca.csv', sep=',')
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
#qtd de infectados por escolaridade
df_qtd_testes_positivos_escolaridade = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_escolaridade.csv', sep=',')
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
    title='<b>Casos confirmados de COVID-19 por escolaridade</b>',
    legend_title='Legenda',
    xaxis_visible=False,
    width=600, 
    height=500
)
fig_qtd_testes_positivos_escolaridade.update_xaxes(tickangle=45)
#diferença percentual de infectados por escolaridade
df_taxa_incidencia_escolaridade = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_escolaridade.csv', sep=',')
fig_taxa_incidencia_escolaridade = px.pie(
    data_frame=df_taxa_incidencia_escolaridade.sort_values('taxa_incidencia_mil_habitantes', ascending=False), 
    values = 'taxa_incidencia_mil_habitantes', 
    names = 'escolaridade',
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
    width=600,  
    height=400
)
fig_taxa_incidencia_escolaridade.update_xaxes(tickangle=45)

#aba características clínicas

#qtd de infectados assintomáticos
df_qtd_infectados_sintomaticos = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_sintomaticos.csv', sep=',')
#qtd de infectados assintomáticos
df_qtd_infectados_assintomaticos = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_assintomaticos.csv', sep=',')
#qtd de infectados internados
df_qtd_infectados_internados = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_internados.csv', sep=',')
#qtd de infectados internados com respiração artificial
df_qtd_infectados_internados_respiracao_artificial = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_internados_respiracao_artificial.csv', sep=',')
#percentual de infectados sintomáticos e assintomáticos
df_qtd_testes_positivos_sintomaticos = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_sintomaticos.csv', sep=',')
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
    title='<b>Percentual de casos sintomáticos e assintomáticos de COVID-19</b>',
    legend_title='Legenda',
    width=600,
    height=400
)
#percentual dos fatores de risco nos grupos de risco
df_percentual_testes_positivos_fator_risco = pd.read_csv('dados/dados_streamlit/df_percentual_testes_positivos_fator_risco.csv', sep=',')
fig_percentual_testes_positivos_fator_risco = px.bar(
    data_frame = df_percentual_testes_positivos_fator_risco,
    x = 'fator_risco_covid',
    y = 'percentual_testes_positivos',
    color= 'fator_risco_covid',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'percentual_testes_positivos': 'Percentual de testes positivos',
        'fator_risco_covid': 'Fator de risco'
    }
)
fig_percentual_testes_positivos_fator_risco.update_layout(
    title='<b>Percentual dos fatores de risco em casos confirmados de COVID-19 nos grupos de risco</b>',
    showlegend=False,
    yaxis_title='%',
    width=600,
    height=500
)
fig_percentual_testes_positivos_fator_risco.update_xaxes(tickangle=45)
#distribuição dos tipos de sintomas em infectados
df_percentual_testes_positivos_tipo_sintoma = pd.read_csv('dados/dados_streamlit/df_percentual_testes_positivos_tipo_sintoma.csv', sep=',')
fig_percentual_testes_positivos_tipo_sintoma = px.bar(
    data_frame = df_percentual_testes_positivos_tipo_sintoma,
    x = 'sintoma',
    y = 'percentual_testes_positivos',
    color= 'sintoma',
    color_discrete_sequence=['#67000D'],
    labels={
        'percentual_testes_positivos': 'Percentual de testes positivos',
        'sintoma': 'Sintoma'
    }
)
fig_percentual_testes_positivos_tipo_sintoma.update_layout(
    title='<b>Distribuição dos tipos de sintomas nos casos confirmados de COVID-19</b>',
    showlegend=False,
    yaxis_title='%',
    width=600,
    height=500
)
fig_percentual_testes_positivos_tipo_sintoma.update_xaxes(tickangle=45)
#percentual internados e não internados
df_qtd_testes_positivos_internacao = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_internacao.csv', sep=',')
fig_qtd_testes_positivos_internacao = px.pie(
    data_frame=df_qtd_testes_positivos_internacao.sort_values('qtd_testes_positivos', ascending=False),
    values='qtd_testes_positivos',
    names='questao_internacao',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos':'Quantidade',
        'questao_internacao':'Condição'
    }
)
fig_qtd_testes_positivos_internacao.update_traces(
    pull=[0.3, 0],
    texttemplate='%{percent:.2%}'
)
fig_qtd_testes_positivos_internacao.update_layout(
    title='<b>Perfil das internações por COVID-19: percentual de pacientes internados e não internados</b>',
    legend_title='Legenda',
    width=600,
    height=400
)
#percentual internados e internados com respiração artificial
df_testes_positivos_respiracao_artificial = pd.read_csv('dados/dados_streamlit/df_testes_positivos_respiracao_artificial.csv', sep=',')
fig_qtd_testes_positivos_respiracao_artificial = px.pie(
    data_frame=df_testes_positivos_respiracao_artificial.sort_values('qtd_testes_positivos', ascending=False),
    values='qtd_testes_positivos',
    names='questao_internacao_ajuda_respirar',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos':'Quantidade',
        'questao_internacao_ajuda_respirar':'Condição'
    }
)
fig_qtd_testes_positivos_respiracao_artificial.update_traces(
    texttemplate='%{percent:.2%}'
)
fig_qtd_testes_positivos_respiracao_artificial.update_layout(
    title='<b>Pacientes internados por COVID-19: percentual com e sem respiração artificial</b>',
    legend_title='Legenda',
    width=600,
    height=400
)
#taxa de infectados por faixa etária do esquema vacinal
df_taxa_incidencia_faixa_etaria_esquema_vacinal = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_faixa_etaria_esquema_vacinal.csv', sep=',')
fig_taxa_incidencia_faixa_etaria_esquema_vacinal = px.bar(
    data_frame=df_taxa_incidencia_faixa_etaria_esquema_vacinal.sort_values('taxa_de_contagio_mil_habitantes', ascending=False),
    x='faixa_etaria',
    y='taxa_de_contagio_mil_habitantes',
    color='faixa_etaria',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_de_contagio_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'faixa_etaria': 'Faixa etária'
    }
)
fig_taxa_incidencia_faixa_etaria_esquema_vacinal.update_layout(
    title='<b>Taxa de incidência de COVID-19 por faixa etária do esquema vacinal</b>',
    showlegend=False,
    width=600, 
    height=500
)
fig_taxa_incidencia_faixa_etaria_esquema_vacinal.update_xaxes(tickangle=45)

#aba características comportamentais

#qtd de sintomáticos que buscaram atendimento médico
df_sintomaticos_estabelecimento_saude = pd.read_csv('dados/dados_streamlit/df_sintomaticos_estabelecimento_saude.csv', sep=',')
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
    title='<b>Casos suspeitos de COVID-19 que buscaram atendimento médico</b>',
    showlegend=False,
    width=600,
    height=400
)
#percentual de sintomáticos que buscaram atendimento médico
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
    title='<b>Percentual de casos suspeitos de COVID-19 que buscaram atendimento médico</b>',
    width=600,
    height=400
)
#qtd de infectados que adotaram medida de isolamento social
df_qtd_infectados_permaneceu_casa = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_permaneceu_casa.csv', sep=',')
fig_qtd_sintomaticos_permaneceu_casa = px.bar(
    data_frame=df_qtd_infectados_permaneceu_casa.sort_values('qtd_testes_validos', ascending=False), 
    x='questao_permaneceu_casa', 
    y='qtd_testes_validos',
    color='questao_permaneceu_casa',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_validos': 'Quantidade',
        'questao_permaneceu_casa': 'Isolamento'
    }
)
fig_qtd_sintomaticos_permaneceu_casa.update_layout(
    title='<b>Adesão ao isolamento social de casos confirmados de COVID-19</b>',
    showlegend=False,
    width=600, 
    height=400
)
#percentual de infectados que adotaram medida de isolamento social
fig_percentual_sintomaticos_permaneceu_casa = px.pie(
    data_frame=df_qtd_infectados_permaneceu_casa, 
    values = 'qtd_testes_validos', 
    names = 'questao_permaneceu_casa',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_validos': 'Quantidade',
        'questao_permaneceu_casa': 'Isolamento'
    }
)
fig_percentual_sintomaticos_permaneceu_casa.update_layout(
    title='<b>Percentual de isolamento social entre casos confirmados de COVID-19</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual de infectados que adotaram medida de isolamento social por região
df_qtd_infectados_permaneceu_casa_regiao = pd.read_csv('dados/dados_streamlit/df_qtd_infectados_permaneceu_casa_regiao.csv', sep=',')
fig_sintomaticos_permaneceu_casa_regiao = px.pie(
    data_frame=df_qtd_infectados_permaneceu_casa_regiao, 
    values = 'qtd_testes_positivos', 
    names = 'regiao',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'regiao': 'Região'
    }
)
fig_sintomaticos_permaneceu_casa_regiao.update_layout(
    title='<b>Percentual de isolamento social entre casos confirmados de COVID-19 por região</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#percentual sintomáticos que adotaram medida de isolamento social por região por estado
df_qtd_infectados__permaneceu_casa_estado = pd.read_csv('dados/dados_streamlit/df_qtd_infectados__permaneceu_casa_estado.csv', sep=',')
fig_sintomaticos_permaneceu_casa_estado = px.bar(
    data_frame=df_qtd_infectados__permaneceu_casa_estado.sort_values('qtd_testes_validos', ascending=False), 
    x='uf',
    y='qtd_testes_validos',
    color='uf',
    color_discrete_sequence=['#67000D'],
    labels={
        'qtd_testes_validos': 'Quantidade',
        'uf': 'Estado'
    }
)
fig_sintomaticos_permaneceu_casa_estado.update_layout(
    title='<b>Casos confirmados de COVID-19 que adotaram isolamento por estado</b>',
    showlegend=False,
    width=600, 
    height=500
)
fig_sintomaticos_permaneceu_casa_estado.update_xaxes(tickangle=45)
#qtd de infectados automedicados e medicados com orientacao médica
df_testes_positivos_medicacao = pd.read_csv('dados/dados_streamlit/df_testes_positivos_medicacao.csv', sep=',')
fig_testes_positivos_medicacao = go.Figure(data=[
    go.Bar(name='Automedicados', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.qtd_automedicacao),
    go.Bar(name='Medicados com orientação médica', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.qtd_medicacao_orientada),
    go.Bar(name='Ambos', x=df_testes_positivos_medicacao.resposta, y=df_testes_positivos_medicacao.questao_remedio_ambos)   
    ]
)
fig_testes_positivos_medicacao.update_layout(
    title='<b>Uso de medicamentos por pacientes com COVID-19: automedicação vs prescrição médica</b>',
    legend_title='Legenda',
    yaxis_title='Quantidade',
    xaxis_visible=False,
    width=600,
    height=500
)
fig_testes_positivos_medicacao.data[0].marker.color = ['#67000d',] * 2
fig_testes_positivos_medicacao.data[1].marker.color = ['#A50F15',] * 2 
fig_testes_positivos_medicacao.data[2].marker.color = ['#FB6A4A',] * 2 

#aba características econômicas

#qtd de infectados por faixa de rendimento
df_qtd_testes_positivos_faixa_rendimento = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_faixa_rendimento.csv', sep=',')
fig_qtd_testes_positivos_faixa_rendimento = px.bar(
    data_frame=df_qtd_testes_positivos_faixa_rendimento.sort_values('qtd_testes_positivos', ascending=False),
    x='faixa_rendimento', #qtd_testes_positivos
    y='qtd_testes_positivos',  #faixa_rendimento
    color='faixa_rendimento',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'faixa_rendimento': 'Faixa de rendimento (R$)'
    }
)
fig_qtd_testes_positivos_faixa_rendimento.update_layout(
    title='<b>Casos confirmados de COVID-19 por faixa de rendimento</b>',
    showlegend=False,
    width=600, 
    height=500
)
fig_qtd_testes_positivos_faixa_rendimento.update_xaxes(tickangle=45)
#qtd de de infectados por faixa de rendimento nas regiões e estados
df_qtd_testes_positivos_regiao_estado_faixa_rendimento = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_regiao_estado_faixa_rendimento.csv', sep=',')
fig_qtd_testes_positivos_regiao_estado_faixa_rendimento = px.treemap(
    data_frame=df_qtd_testes_positivos_regiao_estado_faixa_rendimento, 
    path = ['regiao', 'uf', 'faixa_rendimento'], 
    values = 'qtd_testes_positivos', 
    color='qtd_testes_positivos',
    color_continuous_scale=px.colors.sequential.Reds,
    labels={
        'qtd_testes_positivos': 'Quantidade',
        'faixa_rendimento': 'Faixa de rendimento (R$)'
    }
)
fig_qtd_testes_positivos_regiao_estado_faixa_rendimento.update_layout(
    title='Casos confirmados de COVID-19 por faixa de rendimento em regiões e estados',
    showlegend=False,
    width=600,  
    height=500
)
#taxa de incidência por faixa de rendimento
df_taxa_incidencia_faixa_rendimento = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_faixa_rendimento.csv', sep=',')
fig_taxa_incidencia_faixa_rendimento = px.bar(
    data_frame=df_taxa_incidencia_faixa_rendimento.sort_values('taxa_incidencia_mil_habitantes', ascending=False),
    x='faixa_rendimento',
    y='taxa_incidencia_mil_habitantes', 
    color='faixa_rendimento',
    hover_data='qtd_testes_positivos',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'faixa_rendimento': 'Faixa de rendimento (R$)',
        'qtd_testes_positivos': 'Quantidade'
    }
)
fig_taxa_incidencia_faixa_rendimento.update_layout(
    title='<b>Taxa de incidência de COVID-19 por faixa de rendimento</b>',
    showlegend=False,
    width=600,  
    height=500
)
fig_taxa_incidencia_faixa_rendimento.update_xaxes(tickangle=45)
#valor médio auxílio entre infectados
df_testes_positivos_valor_medio_auxilio_emergencial = pd.read_csv('dados/dados_streamlit/df_testes_positivos_valor_medio_auxilio_emergencial.csv', sep=',')
fig_testes_positivos_valor_medio_auxilio_emergencial = px.bar(
    data_frame=df_testes_positivos_valor_medio_auxilio_emergencial.sort_values('media_auxlio_covid_faixa_rendimento', ascending=False),
    x='faixa_rendimento',
    y='media_auxlio_covid_faixa_rendimento', 
    color='faixa_rendimento',
    hover_data='qtd_testes_positivos',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'media_auxlio_covid_faixa_rendimento': 'Valor (R$)',
        'faixa_rendimento': 'Faixa de rendimento (R$)',
        'qtd_testes_positivos': 'Quantidade'
    }
)
fig_testes_positivos_valor_medio_auxilio_emergencial.update_layout(
    title='<b>Valor médio do auxílio emergencial recebido entre infectados por faixa de rendimento</b>',
    showlegend=False,
    width=600, 
    height=500
)
fig_testes_positivos_valor_medio_auxilio_emergencial.update_xaxes(tickangle=45)
#qtd de infectados por tipo de trabalho realizado
df_qtd_testes_positivos_tipo_trabalho = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_tipo_trabalho.csv', sep=',')
fig_qtd_testes_positivos_tipo_trabalho = px.bar(
    data_frame=df_qtd_testes_positivos_tipo_trabalho.sort_values('qtd_testes_positivos', ascending=False),
    x='qtd_testes_positivos',
    y='questao_tipo_trabalho_realizado', 
    color='questao_tipo_trabalho_realizado',
    color_discrete_sequence=['#67000d'],
    labels={
        'qtd_testes_positivos':'Quantidade',
        'questao_tipo_trabalho_realizado':'Tipo de trabalho realizado'
    }
)
fig_qtd_testes_positivos_tipo_trabalho.update_layout(
    title='<b>Casos confirmados de COVID-19 por profissão</b>',
    showlegend=False,
    width=1200, 
    height=800
)
#taxa de incidência por tipo de trabalho
df_taxa_incidencia_tipo_trabalho = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_tipo_trabalho.csv', sep=',')
fig_taxa_incidencia_tipo_trabalho = px.bar(
    data_frame=df_taxa_incidencia_tipo_trabalho.sort_values('taxa_incidencia_mil_habitantes', ascending=False),
    x='taxa_incidencia_mil_habitantes',
    y='questao_tipo_trabalho_realizado', 
    color='questao_tipo_trabalho_realizado',
    hover_data='qtd_testes_positivos',
    color_discrete_sequence=['#67000d'],
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'questao_tipo_trabalho_realizado': 'Tipo de trabalho realizado',
        'qtd_testes_positivos':'Quantidade',
    }
)
fig_taxa_incidencia_tipo_trabalho.update_layout(
    title='<b>Taxa de incidência de COVID-19 por profissão</b>',
    showlegend=False,
    width=1200, 
    height=800
)
#percentual entre infectados por motivo do afastamento do trabalho
df_percentual_motivo_afastamento = pd.read_csv('dados/dados_streamlit/df_percentual_motivo_afastamento.csv', sep=',')
fig_percentual_motivo_afastamento = px.bar(
    data_frame=df_percentual_motivo_afastamento.sort_values('percentual_motivo_afastamento', ascending=False), 
    x = 'questao_motivo_afastamento', 
    y = 'percentual_motivo_afastamento',
    color='questao_motivo_afastamento',
    hover_data='qtd_testes_positivos',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'percentual_motivo_afastamento': 'Percentual',
        'questao_motivo_afastamento': 'Motivo do afastamento',
        'qtd_testes_positivos':'Quantidade',
    }
)
fig_percentual_motivo_afastamento.update_layout(
    title='<b>Percentual dos casos de COVID-19 por motivo de afastamento do trabalho</b>',
    yaxis_title='%',
    legend_title='Legenda',
    xaxis_visible=False,
    xaxis_showticklabels=False,
    width=1200, 
    height=500
)
#qtd de testes aplicados
df_qtd_tipo_teste = pd.read_csv('dados/dados_streamlit/df_qtd_tipo_teste.csv', sep=',')
fig_qtd_tipo_teste = px.bar(
    data_frame=df_qtd_tipo_teste.sort_values('qtd_tipo_teste', ascending=False), 
    x='tipo_teste',
    y='qtd_tipo_teste',
    color='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_tipo_teste': 'Quantidade',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_qtd_tipo_teste.update_layout(
    title='<b>Quantidade de testes para COVID-19 por tipo de teste</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
fig_qtd_tipo_teste.update_xaxes(tickangle=45)
#percentual de testes aplicados por tipo de teste
fig_percentual_tipo_teste = px.pie(
    data_frame=df_qtd_tipo_teste.sort_values('qtd_tipo_teste', ascending=False), 
    values='qtd_tipo_teste',
    names='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_tipo_teste': 'Quantidade',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_percentual_tipo_teste.update_layout(
    title='<b>Percentual de testes aplicados por tipo de teste</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
fig_percentual_tipo_teste.update_xaxes(tickangle=45)
#qtd de testes positivos por tipo de teste
df_qtd_testes_positivos_tipo_teste = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_tipo_teste.csv', sep=',')
fig_qtd_testes_positivos_tipo_teste = px.bar(
    data_frame=df_qtd_testes_positivos_tipo_teste.sort_values('qtd_testes_positivos', ascending=False), 
    x='tipo_teste',
    y='qtd_testes_positivos',
    color='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_validos': 'Quantidade',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_qtd_testes_positivos_tipo_teste.update_layout(
    title='<b>Casos confirmados de COVID-19 por tipo de teste</b>',
    legend_title='Legenda',
    yaxis_title='%',
    width=600, 
    height=400
)
fig_qtd_testes_positivos_tipo_teste.update_xaxes(tickangle=45)
#diferença percentual da taxa de incidência por tipo de teste
df_taxa_incidencia_tipo_teste = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_tipo_teste.csv', sep=',')
fig_taxa_incidencia_tipo_teste= px.pie(
    data_frame=df_taxa_incidencia_tipo_teste.sort_values('taxa_incidencia_mil_habitantes', ascending=False), 
    values='taxa_incidencia_mil_habitantes',
    names='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_taxa_incidencia_tipo_teste.update_layout(
    title='<b>Diferença percentual da taxa de incidência por tipo de teste</b>',
    legend_title='Legenda',
    yaxis_title='%',
    width=600, 
    height=400
)
#qtd de testes inconclusivos
df_qtd_testes_inconclusivos_tipo_teste = pd.read_csv('dados/dados_streamlit/df_qtd_testes_inconclusivos_tipo_teste.csv', sep=',')
fig_qtd_testes_inconclusivos_tipo_teste = px.bar(
    data_frame=df_qtd_testes_inconclusivos_tipo_teste.sort_values('qtd_testes_inconclusivos', ascending=False), 
    x='tipo_teste',
    y='qtd_testes_inconclusivos',
    color='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'qtd_testes_inconclusivos': 'Quantidade',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_qtd_testes_inconclusivos_tipo_teste.update_layout(
    title='<b>Casos inconclusivos de COVID-19 por tipo de teste</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#diferença percentual da taxa de incidênciade testes com resultado inconclusivo por tipo de teste
df_taxa_incidencia_tipo_teste_inconclusivo = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_tipo_teste_inconclusivo.csv', sep=',')
fig_taxa_incidencia_tipo_teste_inconclusivo = px.pie(
    data_frame=df_taxa_incidencia_tipo_teste_inconclusivo.sort_values('taxa_incidencia_mil_habitantes', ascending=False), 
    values='taxa_incidencia_mil_habitantes',
    names='tipo_teste',
    color_discrete_sequence=px.colors.sequential.Reds_r,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'tipo_teste': 'Tipo de teste'
    }
)
fig_taxa_incidencia_tipo_teste_inconclusivo.update_layout(
    title='<b>Diferença percentual da taxa de incidência de testes inconclusivos por tipo de teste</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)

#características geoespaciais

#taxa de incidência nacional
df_taxa_incidencia = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia.csv', sep=',')
#qtd de infectados por zona de domicílio
df_qtd_testes_positivos_zona = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_zona.csv', sep=',')
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
    title='<b>Casos confirmados de COVID-19 por zona de domicílio</b>',
    legend_title='Legenda',
    width=600, 
    height=400
)
#diferença percentual da taxa de incidência por zona de domicílio
df_taxa_incidencia_zona = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_zona.csv', sep=',')
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
#qtd de infectados por região
df_qtd_testes_positivos_regiao = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_regiao.csv', sep=',')
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
    title='<b>Casos confirmados de COVID-19 por região</b>',
    showlegend=False,
    width=600, 
    height=400
)
fig_qtd_testes_positivos_regiao.update_xaxes(tickangle=45)
#diferença percentual da taxa de incidência por região
df_taxa_incidencia_regiao = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_regiao.csv', sep=',')
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
#qtd de infectados por estado
df_qtd_testes_positivos_estado = pd.read_csv('dados/dados_streamlit/df_qtd_testes_positivos_estado.csv', sep=',')
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
    title='<b>Casos confirmados de COVID-19 por estado</b>',
    yaxis_title='Quantidade de infectados',
    showlegend=False,
    width=600, 
    height=500
)
fig_qtd_testes_positivos_estado.update_xaxes(tickangle=45)
#mapa de risco por taxa de incidência
df_taxa_incidencia_estado = pd.read_csv('dados/dados_streamlit/df_taxa_incidencia_estado.csv', sep=',')
geojson = json.load(open('dados/dados_streamlit/brasil_estados.json'))
fig_mapa_risco_taxa_incidencia_estado = px.choropleth(
    data_frame=df_taxa_incidencia_estado,
    geojson=geojson,
    locations='sigla',
    color='taxa_incidencia_mil_habitantes',
    hover_name='uf',
    scope='south america',
    color_continuous_scale=px.colors.sequential.Reds,
    labels={
        'taxa_incidencia_mil_habitantes': 'Taxa de incidência (por mil habitantes)',
        'sigla': 'Sigla'
    }
)
fig_mapa_risco_taxa_incidencia_estado.add_scattergeo(
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
fig_mapa_risco_taxa_incidencia_estado.update_geos(fitbounds='locations', visible=False)
fig_mapa_risco_taxa_incidencia_estado.update_layout(
    title='<b>Mapa de risco de acordo com a taxa de incidência de COVID-19 nos estados</b>',
    width=1000, 
    height=800
)

#visualização no streamlit

#logo fiap
st.image('img/fiap.png')

#título
st.title('DASHBOARD PNAD-COVID-19 IBGE :mask:')

#layout do aplicativo
aba1, aba2, aba3, aba4, aba5 = st.tabs(['Características gerais', 'Características clínicas', 'Características comportamentais', 'Características econômicas', 'Caracteríticas geoespaciais'])

with aba1:
    st.metric('**Total de infectados**', df_qtd_testes_positivos['qtd_testes_positivos'])
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('**Total de infectados internados**', df_qtd_infectados_internados['qtd_testes_positivos'])
    with coluna2:
        st.metric('**Total de infectados internados com respiração artificial**', df_qtd_infectados_internados_respiracao_artificial['qtd_testes_positivos'])
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        st.plotly_chart(fig_qtd_testes_positivos_sexo, use_container_width=True)
    with coluna4:
        st.plotly_chart(fig_taxa_incidencia_sexo, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que o número total de casos confirmados é maior entre mulheres do que entre homens e que a taxa de incidência foi 3% superior em mulheres. Entre os fatores que podem explicar essa diferença, estão:
                        <ul>
                            <li>A maior parte dos profissionais de saúde são mulheres: isso pode aumentar a exposição ao vírus por trabalharem na linha de frente no combate à pandemia.</li>
                            <li>Busca por teste: as mulheres tendem a ser mais proativas do que os homens em procurar testagem ao desenvolverem sintomas.</li>
                            <li>Responsabilidades domésticas: ao cuidarem da casa e da família, as mulheres podem se expor mais ao contágio por membros infectados.</li>
                            <li>Distribuição etária: como as mulheres têm expectativa de vida maior, elas correspondem à maioria dos idosos, grupo de risco mais afetado pela COVID-19.</li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    coluna5, coluna6 = st.columns(2)
    with coluna5:
        st.plotly_chart(fig_qtd_testes_positivos_cor_raca, use_container_width=True)
    with coluna6:
        st.plotly_chart(fig_taxa_incidencia_cor_raca, use_container_width=True)
    st.markdown(
        ''' 
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que os casos confirmados de COVID-19 apresentou o maior número na população parda, onde houve uma taxa de 21.5%. Contudo, o grupo proporcionalmente mais impactado é o de indígenas, 28%. Isso pode ocorrer devido as condições socioeconômicas singulares, como moradia e saneamento básico precários, o que facilita a disseminação de doenças infecciosas. Essas condições também estão bastante evidenciadas entre pardos e pretos, o que reforça sua correlação com a taxa de incidência. 
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_qtd_testes_positivos_escolaridade, use_container_width=True)
    st.plotly_chart(fig_taxa_incidencia_escolaridade, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Observa-se que o número de casos confirmados é relativamente maior nos grupos com ensino médio completo e incompleto. Entre os fatores que podem explicar esse resultado, estão:
                        <ul>
                            <li>Pessoas com ensino médio completo estão em idade para o trabalho regular e, muito provavelmente, não puderam ficar em casa durante a pandemia.</li>
                            <li>Os indivíduos entrevistados nesse grupo executam trabalhos com maior contato ao público. Exemplo: comerciante, vendedor, cabeleireiro.</li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )

#aba características clínicas
with aba2:
    st.markdown(
        '''
            ## Indicadores clínicos :stethoscope:
        '''
    )
    coluna1, coluna2 = st.columns(2)    
    with coluna1:
        st.metric('**Total de infectados sintomáticos**', df_qtd_infectados_sintomaticos['qtd_testes_positivos'])
    with coluna2:
        st.metric('**Total de infectados assintomáticos**', df_qtd_infectados_assintomaticos['qtd_testes_positivos'])
    st.plotly_chart(fig_percentual_testes_positivos_sintomaticos, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Nota-se que os casos assintomáticos de COVID-19 são a ampla maioria. Nesse cenário, esse fato pode ter contribuído para o aumento da taxa de contaminação, pois, sem a consciência de estar contaminado, o indivíduo tende a negligenciar medidas de isolamento. 
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_percentual_testes_positivos_fator_risco, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    O grupo de risco é constituído por um conjunto de doenças que podem agravar os efeitos da COVID-19. 
                </p>
                <p>
                    Pessoas classificadas no grupos de risco não raramente estão em tratamento, caso em que sua imunidade tende a estar mais baixa. É importante pontuar que a hipertensão atinge mais de 26% dos brasileiros, já a diabetes, 6,9%. Ademais, idosos, pertecentes ao grupo de risco, constituem 14% da população.
                </p>
                <p>
                    Dentre os indivíduos classificados no grupo de risco e que tiveram caso confirmado de COVID-19, lideram aqueles que possuem hipertensão, idosos, e que sofrem de diabetes. Esse indicador é importante para a triagem de casos face a COVID-19, pois indivíduos no grupo de risco devem receber atendimento prioritário e com cuidados compatíveis à sua condição.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_percentual_testes_positivos_tipo_sintoma, use_container_width=True)
    st.metric('**Total de infectados internados**', df_qtd_infectados_internados.values)
    st.plotly_chart(fig_qtd_testes_positivos_internacao, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Apenas 0.69% dos contaminados precisaram ser internados e, dentro os indivíduos internados, verifica-se que a maioria são do grupo de risco.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.metric('**Total de internados com respiração artificial**', df_qtd_infectados_internados_respiracao_artificial.values)
    st.plotly_chart(fig_qtd_testes_positivos_respiracao_artificial, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    A maioria dos internados não precisaram de respiração artificial. Dentre aqueles que receberam respiração artificial, 72% pertencem ao grupo de risco. 
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_taxa_incidencia_faixa_etaria_esquema_vacinal, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Indicadores relativos a faixa etária do esquema vacinal são importantes, pois podem auxiliar na otimização de alocação de recursos.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )

#aba características comportamentais
with aba3:
    st.markdown(
        '''
            ## Indicadores comportamentais :grimacing:
        '''
    )
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(fig_qtd_sintomaticos_estabelecimento_saude, use_container_width=True)
    with coluna2:
        st.plotly_chart(fig_percentual_sintomaticos_estabelecimento_saude, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Analisando os dados, observa-se uma baixa busca por atendimento médico entre aqueles que tiveram sintomas de COVID-19. O levantamento apontou que 33.141 sintomáticos não buscaram atendimento, enquanto apenas 11.796 buscaram algum tipo de assistência de saúde. Em termos percentuais, isso significa que 73,7% das pessoas com sinais da doença não procuraram atendimento médico.
                </p>
                <p>
                    A baixa procura por serviços de saúde, mesmo diante de sintomas, pode ser devido a fatores como: 
                        <ul>
                            <li>Barreiras no acesso ao sistema de saúde durante a pandemia.</li>
                            <li>Restrições financeiras para buscar atendimento.</li>
                            <li>Pouco concientização em relação aos riscos da doença. </li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        st.plotly_chart(fig_qtd_sintomaticos_permaneceu_casa, use_container_width=True)
    with coluna4:
        st.plotly_chart(fig_percentual_sintomaticos_permaneceu_casa, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que um pouco mais de 1039 infectados adotaram algum isolamento, enquanto 333 não adotaram. Isso mostra que 75,7% das pessoas infectadas adotaram alguma medida de isolamento, enquanto, 24,3% não.
                </p>
                <p>
                    Apesar da maioria dos infectados ter adotado alguma medida de isolamento social, ainda há uma parcela importante de negligentes potencialmente transmitindo o vírus.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_sintomaticos_permaneceu_casa_regiao, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    O gráfico demonstra variações regionais significativas quanto à adoção de isolamento social. Podemos observar que o Nordeste de destaca com maior adesão ao isolamento, enquanto o Sul aparece com a menor taxa proporcional. 
                </p>
                <p>
                    Essas diferenças podem refletir: 
                        <ul>
                            <li>Diferenças socioeconômicas.</li>
                            <li>Eficiência de políticas públicas de combate a pandemia.</li>
                            <li>Pouco concientização em relação aos riscos da doença. </li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_sintomaticos_permaneceu_casa_estado, use_container_width=True)
    st.plotly_chart(fig_testes_positivos_medicacao, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que a maioria das pessoas se automedicaram, ou seja, fizeram uso de medicamentos por conta própria, sem prescrição. Isso pode ser reflexo da circulação de informações falsas a respeito da doença e ineficiência de políticas públicas de concientização.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )

#aba características econômicas
with aba4:
    st.markdown(
        '''
            ## Indicadores econômicos :moneybag:
        '''
    )
    st.plotly_chart(fig_qtd_testes_positivos_faixa_rendimento, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que, em números absolutos, o grupo mais atingido pela COVID no período é aquele cuja faixa de rendimento é ligeiramente superior a um salário-mínimo. Entre as razões, estão:
                        <ul>
                            <li>O tipo de trabalho realizado exige estar em contato com o público.</li>
                            <li>Pessoas que não tiveram a oportunidade de ficar em isolamento.</li>
                            <li>Pouca concientização em relação aos riscos da doença. </li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_qtd_testes_positivos_regiao_estado_faixa_rendimento, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Na maioria dos estados brasileiros, os indivíduos mais afetados são aqueles que vivem com rendimento menor ou pouco superior ao salário-mínimo, com exceção aos que vivem São Paulo e Santa Catarina, onde a faixa de rendimento tem um piso superior ao salário-mínimo.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_taxa_incidencia_faixa_rendimento, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Por fim, observa-se que a taxa de incidência é tanto maior quanto mais vunerável financeiramente é o grupo.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_testes_positivos_valor_medio_auxilio_emergencial, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Vê-se que a distribuição do valor médio do auxílio emergencial concedido segue uma ordem quase inversamente proporcional à faixa de rendimento do grupo.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_qtd_testes_positivos_tipo_trabalho, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Em relação aos infectados por tipo de trabalho, observa-se resultados relevantes em duas categorias:
                        <ul>
                            <li>Profissões de nível superior (Onde se englobou diversas funções na hora de responder a pesquisa).</li>
                            <li>Área da saúde (Técnicos, médicos e enfermeiros), que a análise inteira diz por si só, foram pessoas que estavam na linha de frente ao combate da doença.</li>
                        <ul>
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_taxa_incidencia_tipo_trabalho, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    A taxa de incidência mostra que, apesar de expostos à doença, profissionais de saúde não lideram os grupos proporcionalmente mais afetados.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.plotly_chart(fig_percentual_motivo_afastamento, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Podemos observar que o principal motivo de afastamento decorre de medidas em prol do isolamento social. 
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(fig_qtd_tipo_teste, use_container_width=True)
    with coluna2:
        st.plotly_chart(fig_percentual_tipo_teste, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    No início da pandemia, um dos testes mais aplicados era o teste de sorologia IgM e IgG (Sangue - Furo dedo), que detecta os anticorpos produzidos pelo sistema imunológico para combater a infecção, portanto em relação a quantidade ele aparece em primeiro lugar. Em seguida temos o teste SWAB, que basicamente é uma coleta por meio das vias nasais e faríngea, para detectar proteínas produzidas na base de replicação viral.
                </p>
                <p>
                    E por último o exame de sangue, que também faz a testagem dos anticorpos produzidos pelo sistema imunológico. 
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        st.plotly_chart(fig_qtd_testes_positivos_tipo_teste, use_container_width=True)
    with coluna4:
        st.plotly_chart(fig_taxa_incidencia_tipo_teste, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    O teste que mais apresentou casos positivos foi o SWAB, o que pode ser pelo fato de o teste detectar no momento da realização a infecção, fazendo com que seja mais procurado por sintomáticos e mais eficaz segundo as pesquisas. Como os testes de sangue apresentam os anticorpos produzidos, o resultado pode ser interpretado tanto como "Já teve a doença" ou "Está com a doença", de acordo com os sintomas sentidos no momento.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    coluna5, coluna6 = st.columns(2)
    with coluna5:
        st.plotly_chart(fig_qtd_testes_inconclusivos_tipo_teste, use_container_width=True)
    with coluna6:
        st.plotly_chart(fig_taxa_incidencia_tipo_teste_inconclusivo, use_container_width=True)

#aba características geoespaciais
with aba5:
    st.markdown(
        '''
            ## Indicadores geoespaciais :world_map:
        '''
    )
    st.metric('**Média da taxa de incidência nacional**', df_taxa_incidencia['taxa_incidencia_mil_habitantes'].mean().astype(int))
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(fig_qtd_testes_positivos_zona, use_container_width=True)
    with coluna2:
        st.plotly_chart(fig_taxa_incidencia_zona, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    Apesar da incidência maior em áreas urbanas dado a densidade populacional, a taxa de incidência entre os entrevistados se mostrou ligeiramente maior.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    #região
    st.metric('**Média da taxa de incidência nas regiões**', df_taxa_incidencia_regiao['taxa_incidencia_mil_habitantes'].mean().astype(int))
    coluna3, coluna4 = st.columns(2)
    with coluna3:
        st.plotly_chart(fig_qtd_testes_positivos_regiao, use_container_width=True)
    with coluna4:
        st.plotly_chart(fig_taxa_incidencia_regiao, use_container_width=True)
    st.markdown(
        '''
            <div style='text-align: justify;'>
                <p>
                    As regiões Nordeste, Sudeste e Norte lideram, respectivamente, em números absolutos. Contudo, a região Norte passa a liderar em taxa de incidência, enquanto o Sudeste fica em quarto lugar, com uma diferença percentual 15,3% menor que a região Norte, ainda que possua uma população consideravelmente maior. Esse comportamento dos dados podem ser explicados pelo emprego de estratégias de saúde pública mais adequadas e pela diferença econômica entre as regiões.
                </p>
            </div>
        ''',
            unsafe_allow_html=True
    )
    st.metric('**Média da taxa de incidência nos estados**', df_taxa_incidencia_estado['taxa_incidencia_mil_habitantes'].mean().astype(int))
    st.plotly_chart(fig_qtd_testes_positivos_estado, use_container_width=True)
    st.plotly_chart(fig_mapa_risco_taxa_incidencia_estado, use_container_width=True)


