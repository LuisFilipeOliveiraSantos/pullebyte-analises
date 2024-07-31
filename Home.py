# import streamlit as st
# import pandas as pd

# st.set_page_config(
#     page_title = "PISI3 - BSI - UFRPE por Gabriel Alves",
#     layout = "wide",
#     menu_items = {
#         'About': '''Este sistema foi desenvolvido pelo prof Gabriel Alves para fins didáticos, para a disciplina de 
#         Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período do curso de Bacharelado em Sistemas de Informação
#         (BSI) da Universidade Federal Rural de Pernambuco (UFRPE).
#         Dúvidas? gabriel.alves@ufrpe.br
#         Acesse: bsi.ufrpe.br
#         '''
#     }
# )

# st.markdown(f'''
#     <h1>Sistema Didático para PISI3</h1>
#     <br>
#     Este projeto tem o objetivo de prover vários exemplos úteis para os projetos que serão desenvolvidos na disicplina de 
#     Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período do curso de Bacharelado em Sistemas de Informação
#     (BSI) da Sede da Universidade Federal Rural de Pernambuco (UFRPE).
#     <br>
#     Alguns dos exemplos são:
#     <ul>
#             <li>Páginas e componentes do Streamlit.</li>
#             <li>Uso do Pandas.</li>
#             <li>Uso do YData Profiling.</li>
#             <li>Utilização de arquivos parquet.</li>
#             <li>Visualização de dados.</li>
#             <li>Aprendizado de Máquina: Agrupamento e Classificação.</li>
#     </ul>
#     Classroom: <a href="https://classroom.google.com/c/NjExNTAzOTU4MDQy?cjc=7qgaz7u">https://classroom.google.com/c/NjExNTAzOTU4MDQy?cjc=7qgaz7u</a><br>
#     Contato: gabriel.alves@ufrpe.br<br>
#     Acesse: <a href="bsi.ufrpe.br">bsi.ufrpe.br</a>
# ''', unsafe_allow_html=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.float_format = '{:.2f}'.format
df_original = pd.read_parquet(r"DataSet Project/merge_by_clubs/merge_by_clubs.parquet")
df_original.head()
df_original.shape
df_original.info()
df_original.describe()
df_original.isnull().sum()                              
