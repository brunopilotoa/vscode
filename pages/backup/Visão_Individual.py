import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    # sheet_name="NCs_H23",
    header=1,
)


def data_manipulation():
    df["Data Recebimento"] = df["Data Recebimento"].dt.strftime("%d/%m/%Y")
    df["Data AEV"] = df["Data AEV"].dt.strftime("%d/%m/%Y")
    # if (df["Data VTI"] != "AGUARDANDO").any():
    #     df["Data VTI"] = pd.to_datetime(df["Data VTI"])
    df["Data VTI"] = df["Data VTI"].dt.strftime("%d/%m/%Y")
    df["Data de Entrega Cliente"] = df["Data de Entrega Cliente"].dt.strftime(
        "%d/%m/%Y"
    )
    ## Data AEV , Data VTI , Data de Entrega Cliente
    return df


data_manipulation()

st.dataframe(df)

prefixo = st.selectbox(
    "", df["Prefixo"].unique(), index=None, placeholder="Selecione a Aeronave"
)
datas = df[
    [
        "Data Recebimento",
        "Data VTI",
        "Motorização",
        "Data de Entrega Cliente",
        "Prefixo",
        "Modelo",
        "VFR/IFR",
    ]
]

filtered_df = datas[datas["Prefixo"] == prefixo]
st.dataframe(
    filtered_df,
    hide_index=True,
    column_order=(
        "Data Recebimento",
        "Data VTI",
        "Data de Entrega Cliente",
        "Motorização",
        "Modelo",
        "VFR/IFR",
    ),
)
