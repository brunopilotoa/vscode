import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    header=1,
    sheet_name="NCs_H23",
)
df = df.sort_values(by="Nº")


def data_manipulation_ncs():
    # df["Data NC"] = df["Data NC"].dt.strftime("%d/%m/%Y")
    # df["Data"] = df["Data"].dt.strftime("%d/%m/%Y")

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
nc_aberto = df[df["Status"] != "Solucionado"]


def main():
    st.set_page_config(page_title="Dashboard", layout="wide")
    st.header("Visualização de Dados Hangar 23")
    st.divider()
    st.markdown(
        "Este Aplicativo Foi Criado com Objetivo da Visualização de Dados das Aeronaves no Hangar 23"
    )
    st.write("Utilize o Menu Lateral Para Navegação")


# if st.button("Gráficos de Não Conformidade"):
# st.switch_page("pages/graphs_nc.py")
main()
