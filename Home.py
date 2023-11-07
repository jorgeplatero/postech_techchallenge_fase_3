import streamlit as st


st.image('img/fiap.png')
st.title('Home')
st.markdown(
    '''
        <div style="text-align: justify;">
            <p>
                A pandemia da COVID-19 representou um teste de estresse sem precedentes para os sistemas de saúde em todo o mundo. No Brasil, mostrou diversas fragilidades na infraestrutura dos hospitais particulares e do SUS, 
                mostrando que não estávamos preparados para um surto dessa magnitude. Diante disso, é fundamental extrairmos as lições aprendidas e nos prepararmos melhor para possíveis novas ondas que possam vir a aparecer.
                Nesse contexto, dados confiáveis são fundamentais para entender os principais gargalos e necessidades da população durante a pandemia. 
            </p>
            <p>
                A PNAD COVID-19, realizada pelo IBGE, é uma das principais fontes de informação sobre os brasileiros que dispomos para análise. Neste projeto, você irá conferir alguns insights e ações que os hospitais podem tomar para o caso de um novo surto.
            </p>
            <p>    
                O projeto conta com as seguintes características:
                <ul>
                    <li>Utilização de no máximo 20 questionamentos realizados na pesquisa.</li>
                    <li>Utilização de 3 meses para construção da solução.</li>
                    <li>Caracterização dos sintomas clínicos da população.</li>
                    <li>Caracterização do comportamento da população diante da doença.</li>
                    <li>Caracterização de aspectos socioeconômicos.</li>
                    <li>Características geoespaciais.</li>
                </ul>
            </p>
        </div>
    ''',
    unsafe_allow_html=True
)