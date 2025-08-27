from app import st, df
import numpy as np
import pandas as pd


st.write("Cadastro de Não Conformidades")
with st.form(key="form"):
    # st.dataframe(df)
    prefixo = st.selectbox("Prefixo", df["Prefixo"].dropna().unique())
    ct = st.selectbox("C.T", df["C.T"].dropna().unique())
    data_nc = st.date_input("Data da Ocorrencia", max_value="today")
    class_nc = st.selectbox("Class NC", df["Class NC"].dropna().unique())
    tipo_nc = st.selectbox("Tipo NC", df["Tipo NC"].dropna().unique())
    descricao_nc = st.text_input("Descrição da Não Conformidade")
    numero_ocorrencia = st.text_input(label="Numero da Ocorrencia", value=len(df))
    sent = st.form_submit_button("Enviar")
