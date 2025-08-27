from app import st, df
import numpy as np
import pandas as pd
# st.title("Pagina 1")


df.dropna()
# print(df["Modelo"])

st.write("Formulário de Cadastro de Aeronaves")
print(df.columns)


# return form_data
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["PV"])

with st.form(key="form_nc"):
    # for column in df.columns:
    #    column
    col1, col2 = st.columns(2)
    with col1:
        numero = st.text_input(
            "Numero ", max_chars=3, placeholder="Numero De Fabricação da Aeronave "
        )
        prefixo = st.text_input(
            " Prefixo", placeholder="PT-AAA", max_chars=6, value=None
        )
        pv = st.number_input(
            "Numero do PV", format="%1f", placeholder="01234", value=None
        )
    with col2:
        ns = st.number_input(
            "Numero de Série FVS", format="%1f", value=None, placeholder=""
        )
        modelo = st.selectbox("Modelo", options=["RV10-LSA", "RV12-LSA"])
        motorizacao = st.selectbox(
            "Motorizacao",
            options=["Lycoming", "Sma", "Rotax"],
        )

    vfr = st.radio(
        "Selecione VFR Ou IFR",
        ["VFR", "IFR"],
    )
    submited = st.form_submit_button("Cadastrar")
    send_to_excel = st.form_submit_button("Enviar ao Excel")
    if submited:
        st.write(
            f"Numero : {numero} Prefixo :{prefixo} PV : {pv} Numero de Serie :{ns} Modelo : {modelo} Motor : {motorizacao} VFR/IFR : {vfr} "
        )
    # if send_to_excel
