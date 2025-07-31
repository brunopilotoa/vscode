import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    header=1,
    sheet_name="NCs_H23",
)

print(df.head())

st.header("Visualização de Dados Hangar 23")


def streamlit_settings():
    st.set_page_config(page_title="Dashboard", layout="wide")


def file_loader_nc(adress):
    df = open(adress)
    return df


def data_manipulation():
    df["Descrição da Não Conformidade"] = df[
        "Descrição da Não Conformidade"
    ].str.capitalize()
    # df["Data NC"] = df["Data NC"].dt.strftime("%d-%m-%y")
    df["Data"] = df["Data"].dt.strftime("%d-%m-%y")
    df["Ação de Correção"] = df["Ação de Correção"].str.capitalize()
    df["Falha Reincidente"] = df["Falha Reincidente"].str.capitalize()
    nc = df["Descrição da Não Conformidade"].value_counts()

    return (df, nc)


def main():
    streamlit_settings()
    data_manipulation()
    file_loader_nc("W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx")
    quantidade_nc = df["Class NC"].value_counts()
    nc = df["Descrição da Não Conformidade"].value_counts()

    # (tab1, tab2, tab3, tab4) = st.tabs(
    #    ["Visão Geral", "NCs", "Progresso ", "Visão Individual"]
    # )
    # with tab1:
    #    st.divider()
    # st.subheader(prefixo)
    #    col1, col2 = st.columns(2, gap="large")

    # with col3:
    # with tab1:
    (col1, col2) = st.columns(2)
    with col1:
        # Figura que Mostra a Quantidade de Items por Setor AVI,GMP,CEL
        fig = (
            px.bar(
                quantidade_nc,
                y="count",
                # y="Prefixo",
                title="Quantidade de NC por Setor",
            )
            .update_xaxes(categoryorder="total descending", title="Setor")
            .update_yaxes(title="Quantidade de NCs")
        )
        average_value = quantidade_nc.mean()
        fig.update_traces(width=0.7)
        fig.update_layout(hovermode="x")
        fig.add_hline(
            y=average_value,
            line_dash="dash",
            line_color="white",
            annotation_text=f"Media: {average_value:.0f}",
            annotation_position="bottom right",
        )
        st.plotly_chart(
            fig,
        )
        # Filtrando por Tipo de NC
        tipo_nc = df["Tipo NC"].value_counts().reset_index()
        tipo_nc.columns = ["Tipo NC", "Quantia"]
        most5 = tipo_nc[:5]
        fig3 = (
            px.pie(
                most5,
                title="As 5 Maiores Falhas",
                values="Quantia",
                names="Tipo NC",
            )
            .update_yaxes(title="Quantias", categoryorder="total ascending")
            .update_xaxes(title="", tickangle=-60)
        )
        fig3.update_traces(textposition="inside", textinfo="label+percent")
        st.plotly_chart(fig3)
        # avg_nc = tipo_nc.median()

    with col2:
        ## ocorrencia por cada aeronave
        fig4 = (
            px.bar(df, x="Prefixo", title="Ocorrencia por Aeronaves")
            .update_yaxes(
                title="Quantidade Por Aeronave", categoryorder="total ascending"
            )
            .update_xaxes(title="Prefixo", tickangle=-50)
        )
        st.plotly_chart(
            fig4,
        )
        ## ocorrencia por mes
        #   st.dataframe(df)
        # df["Data NC"] = pd.to_datetime(df["Data NC"], errors="coerce", format="%d%m%Y")
        # fig_mes = (
        #    px.bar(df, x="Data NC", title="Ocorrencia por Mes")
        #    .update_yaxes(title="Quantidade Mensal", categoryorder="total ascending")
        #    .update_xaxes(title="count", tickangle=-50)
        # )
        # st.plotly_chart(
        #    fig_mes,
        # )
        # with col4:
        # Mais ocorridas
        nc = nc[:10]
        fig2 = (
            px.bar(nc, x="count", title="Mais Frequentes e Suas Quantias")
            .update_xaxes(
                title="",
            )
            .update_yaxes(categoryorder="total ascending", title="")
        )
        st.plotly_chart(
            fig2,
        )


main()
