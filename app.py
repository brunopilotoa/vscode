import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    header=1,
    sheet_name="NCs_H23",
)


st.header("Visualização de Dados Hangar 23")
st.divider()


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
    # df["Data NC"] = df["Data NC"].dt.strftime("%d-%m-%y")
    df["Ação de Correção"] = df["Ação de Correção"].str.capitalize()
    df["Falha Reincidente"] = df["Falha Reincidente"].str.capitalize()

    return df


def main():
    streamlit_settings()
    data_manipulation()
    file_loader_nc("W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx")
    ncs = df["Class NC"].value_counts().sum()
    quantidade_nc = df["Class NC"].value_counts()
    # quantidade_nc_prefixo = df[""]
    nc = df["Descrição da Não Conformidade"].value_counts()
    # quantidade_nc["count"] = quantidade_nc["count"]
    (col1, col2) = st.columns(2, gap="large")
    with col1:
        # Figura que Mostra a Quantidade de Items por Setor AVI,GMP,CEL
        fig = (
            px.bar(
                quantidade_nc,
                y="count",
                title="Quantidade de NC por Setor",
                color="count",
            )
            .update_xaxes(categoryorder="total descending", title="Setor")
            .update_yaxes(title="Quantia")
        )
        # average_value = quantidade_nc.mean()
        fig.update_traces(width=0.7)
        fig.update_layout(hovermode="x", title_x=0.3)
        # fig.add_hline(
        #    y=average_value,
        #    line_dash="dash",
        #    line_color="white",
        #    annotation_text=f"Media: {average_value:.0f}",
        #    annotation_position="bottom right",
        # )
        st.plotly_chart(
            fig,
        )
        # Mais ocorridas
        nc = nc[:10]
        fig2 = (
            px.bar(nc, x="count", title="Mais Frequentes", color="count")
            .update_xaxes(
                title="Quantidade",
            )
            .update_yaxes(
                categoryorder="total ascending",
                # title="Titulo Nc"
            )
        )
        fig2.update_layout(title_x=0.5)
        st.plotly_chart(
            fig2,
        )
        # Filtrando por Tipo de NC
        tipo_nc = df["Tipo NC"].value_counts().reset_index()
        tipo_nc.columns = ["Tipo NC", "Quantia"]
        most5 = tipo_nc[:5]
        fig3 = px.pie(
            most5,
            title="As 5 Maiores Falhas",
            values="Quantia",
            names="Tipo NC",
        )
        fig3.update_layout(title_x=0.2)
        fig3.update_traces(textposition="inside", textinfo="label+percent")
        st.plotly_chart(fig3)
    with col2:
        ## ocorrencia por cada aeronave
        fig4 = (
            px.bar(df, x="Prefixo", title="Ocorrencia por Aeronaves", color="Prefixo")
            .update_yaxes(
                title="Quantidade Por Aeronave", categoryorder="total ascending"
            )
            .update_xaxes(title="Prefixo", tickangle=-50)
        )
        fig4.update_layout(title_x=0.3)
        st.plotly_chart(
            fig4,
        )
        ## ocorrencia por mes
        fig_mes = (
            px.bar(
                df,
                x="Data NC",
                title="Ocorrência por Data",
                # height=500
                color="Prefixo",
            )
            .update_yaxes(title="Quantidade Por Data", categoryorder="total ascending")
            .update_xaxes(title="count", tickangle=-50)
        )
        fig_mes.update_layout(title_x=0.4)
        st.plotly_chart(
            fig_mes,
        )
        fig10 = px.bar(
            most5,
            title="As 5 Maiores Falhas",
            x="Tipo NC",
            y="Quantia",
            color="Tipo NC",
            # names="Tipo NC",
        )
        # fig10.update_layout(title_x=0.2)
        # fig10.update_traces(textposition="inside", textinfo="label+percent")
        st.plotly_chart(fig10)


main()
