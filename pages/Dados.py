import streamlit as st
import pandas as pd
import time


@st.cache_data
def converte_csv(df):
    return df.to_csv(index = False).encode('utf-8')

def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso', icon = "✅") 
    time.sleep(3)
    sucesso.empty()

#lendo a base de dados
df = pd.read_csv('dados/dados_exportados/dados_uteis/2023-10-31_pnad_covid_view.zip', compression='zip', sep=',')
df['data'] = pd.to_datetime(df['data'])

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(df.columns), list(df.columns))
st.sidebar.title('Filtros')
with st.sidebar.expander('UF'):
    uf = st.multiselect('Selecione o UF', df['uf'].unique(), df['uf'].unique())
with st.sidebar.expander('Período de referência'):
    df['data'] = pd.to_datetime(df['data'])
    data = st.date_input('Selecione o período', (df['data'].min(), df['data'].max()))

query = '''
`uf` in @uf and \
@data[0] <= `data` <= @data[1]
'''

dados_filtrados = df.query(query)
dados_filtrados = dados_filtrados[colunas]

st.dataframe(dados_filtrados)

st.markdown(f'A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas')

st.markdown('Escreva um nome para o arquivo')
col1, col2 = st.columns(2)
with col1:
    nome_arquivo = st.text_input('', label_visibility = 'collapsed', value = 'dados')
    nome_arquivo += '.csv'
with col2:
    st.download_button('Fazer o download da tabela em csv', data = converte_csv(dados_filtrados), file_name = nome_arquivo, mime = 'text/csv', on_click = mensagem_sucesso)
