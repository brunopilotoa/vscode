import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    header=1,
    sheet_name="NCs_H23",
)


def data_manipulation_ncs():
    # df["Data NC"] = df["Data NC"].dt.strftime("%d/%m/%Y")
    # df["Data"] = df["Data"].dt.strftime("%d/%m/%Y")
    df["Ação de Correção"] = df["Ação de Correção"].str.capitalize()
    df["Falha Reincidente"] = df["Falha Reincidente"].str.capitalize()

    # df["Data AEV"] = df["Data AEV"].dt.strftime("%d/%m/%Y")
    # if (df["Data VTI"] != "AGUARDANDO").any():
    #    df["Data VTI"] = pd.to_datetime(df["Data VTI"])
    # df["Data VTI"] = df["Data VTI"].dt.strftime("%d/%m/%Y")
    # df["Data de Entrega Cliente"] = df["Data de Entrega Cliente"].dt.strftime(
    #    "%d/%m/%Y"
    # )
    ## Data AEV , Data VTI , Data de Entrega Cliente
    return df


print(df.columns)
data_manipulation_ncs()
respostas = df[
    [
        "PV",
        "Prefixo",
        "Class NC",
        "Descrição da Não Conformidade",
        # "Data NC",
        "Ação de Correção",
        # "Data",
        "Falha Reincidente",
        "Status",
    ]
].dropna()
respostas_sorted = sorted(respostas["Descrição da Não Conformidade"].unique())


def main():
    st.title("Panes")
    st.markdown("Filtra e Responde as NC")
    pane = st.selectbox(
        "",
        respostas_sorted,
    )
    filtered_pane = respostas[respostas["Descrição da Não Conformidade"] == pane]
    st.dataframe(filtered_pane, hide_index=True)
    return main


main()
