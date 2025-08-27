from app import df, st, px


def streamlit_settings():
    st.set_page_config(page_title="Gráficos H23", layout="wide")


def data_manipulation():
    df["Descrição da Não Conformidade"] = df[
        "Descrição da Não Conformidade"
    ].str.capitalize()
    # df["Data NC"] = df["Data NC"].dt.strftime("%d-%m-%y")
    # df["Data"] = df["Data"].dt.strftime("%d-%m-%y")
    # df["Data NC"] = df["Data NC"].dt.strftime("%d-%m-%y")
    df["Ação de Correção"] = df["Ação de Correção"].str.capitalize()
    df["Falha Reincidente"] = df["Falha Reincidente"].str.capitalize()
    ncs = df["Class NC"].value_counts().sum()
    tipo_nc = df["Tipo NC"].value_counts().reset_index()
    tipo_nc.columns = ["Tipo NC", "Quantia"]
    most5 = tipo_nc[:5]
    return df


quantidade_nc = df["Class NC"].value_counts()


def ocorrencia():
    quantidade_prefixo = df["Prefixo"].value_counts()
    ## ocorrencia por cada aeronave
    fig = (
        px.bar(
            quantidade_prefixo,
            x="count",
            title="Ocorrencia por Aeronaves",
            color="count",
            text="count",
        )
        .update_xaxes(
            title="Quantidade Por Aeronave",
        )
        .update_yaxes(title="Prefixo", categoryorder="total ascending")
    )
    fig.update_traces(textposition="outside", textfont_size=14)
    # fig.update_layout(title_x=0.3)
    st.plotly_chart(
        fig,
    )


def ocorrencia2():
    ## ocorrencia por mes
    fig_mes = (
        px.histogram(
            df,
            x="Data NC",
            title="Ocorrência por Data",
            color="Prefixo",
        )
        .update_yaxes(title="Quantidade Por Data", categoryorder="total ascending")
        .update_xaxes(title="count", tickangle=-50)
    )
    fig_mes.update_layout(title_x=0.4)
    st.plotly_chart(
        fig_mes,
    )


def main():
    streamlit_settings()
    data_manipulation()
    (
        col1,
        col2,
    ) = st.columns(2, gap="medium")
    with col1:
        # Figura que Mostra a Quantidade de Items por Setor AVI,GMP,CEL
        fig = (
            px.bar(
                quantidade_nc,
                y="count",
                title="Quantidade de NC por Setor",
                # color="count",
                # text="count",
            )
            .update_xaxes(categoryorder="total descending", title="Setor")
            .update_yaxes(title="Quantia")
        )
        average_value = quantidade_nc.mean()
        fig.update_traces(
            width=0.5,
            textposition="outside",
        )
        fig.update_layout(hovermode="x", title_x=0.3)
        fig.add_hline(
            y=average_value,
            line_dash="dash",
            line_color="blue",
            annotation_text=f"Media: {average_value:.0f}",
            # annotation_position="top center ",
        )
        st.plotly_chart(
            fig,
        )
        # Mais ocorridas
        nc = df["Descrição da Não Conformidade"].value_counts()
        nc = nc[:5]
        fig2 = (
            px.bar(
                nc,
                x="count",
                title="Mais Frequentes",
                color="count",
            )
            .update_xaxes(
                title="",
            )
            .update_yaxes(categoryorder="total ascending", title="")
        )
        fig2.update_traces(width=0.4)
        fig2.update_layout(title_x=0.5)
        st.plotly_chart(
            fig2,
        )
        tipo_nc = df["Tipo NC"].value_counts().reset_index()
        tipo_nc.columns = ["Tipo NC", "Quantia"]
        most5 = tipo_nc[:5]
        fig10 = px.bar(
            most5,
            title="As 5 Maiores Falhas",
            x="Tipo NC",
            y="Quantia",
            color="Tipo NC",
            text="Quantia",
        )
        # fig10.update_traces(textposition="auto")
        # fig10.update_layout(
        #    title_x=0.2,
        # )
        st.plotly_chart(fig10)

    with col2:
        ocorrencia()
        ocorrencia2()


main()
