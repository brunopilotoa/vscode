from app import pd, st, px
import statsmodels.api as sm
import plotly.express as px

df = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    sheet_name="BD_H23",
    header=1,
)
# meta = st.slider(label="Meta de Aeronaves Anual", min_value=1, max_value=50)

with st.sidebar:
    selector = st.radio("Selecione as opções", options=["Aprovado VTI", "Entregue"])
    vti_aprovado = df[df["Status VTI"] == "APROVADO"]
    # vti_aprovado["Data VTI"] = pd.to_datetime(vti_aprovado["Data VTI"])
    # vti_aprovado["Data VTI"] = vti_aprovado["Data VTI"].dt.strftime("%m/%y")
    vti_count = vti_aprovado.groupby("Data VTI")["Prefixo"].size().reset_index()
if selector == "Aprovado VTI":
    st.metric(
        label="Aeronaves Aprovadas em VTI",
        value=vti_aprovado["Prefixo"].value_counts().sum(),
        border=True,
    )
    (
        col1,
        col2,
    ) = st.columns(2, gap="medium")
    with col1:
        fig = px.scatter(
            vti_aprovado,
            y="Prefixo",
            x="Data VTI",
            # color="Prefixo",
            # color="Data VTI",
            title="Progresso Data VTI - Prefixo",
        )
        st.plotly_chart(fig)
    # sum_prefixo = vti_aprovado["Data VTI"].value_counts().sort_values()
    # sum_prefixo = sum_prefixo.sort_values(by="Data VTI")
    # st.dataframe(vti_count)
    # st.dataframe(sum_prefixo)
    # fig2 = px.scatter(
    #     sum_prefixo,
    #     # x="Data VTI",
    #     y="count",
    # )
    # # fig2.update_layout(xaxis=dict(tickmode="linear"))
    # # fig2.update_layout(yaxis=dict(tickformat=".0f"))
    # # fig2.update_xaxes(range=["01-24", "12-25"])
    # st.plotly_chart(fig2)
    ## quantidade de aeronaves entregues
    # st.dataframe(df)
    with col2:
        # st.dataframe(vti_aprovado)
        fig2 = px.scatter(
            vti_aprovado,
            x="Data Recebimento",
            y="Data VTI",
            text="Prefixo",
            title="Prazo entre Data de Recebimento - Data VTI",
        )
        fig2.update_traces(
            textposition="bottom center",
        )
        st.plotly_chart(fig2)
    st.divider()
    # sum_vti = vti_aprovado.groupby("Data VTI")["PV"].sum()
    # st.dataframe(vti_count)
    # st.dataframe(sum_vti)

if selector == "Entregue":
    anv_entregue = df[df["STATUS FINAL"] == "ENTREGUE"]
    #     entregue_count = (
    #         anv_entregue.groupby("Data de Entrega Cliente")["Prefixo"].size().reset_index()
    #     )
    st.metric(
        label="Aeronaves Entregues",
        value=anv_entregue["Prefixo"].value_counts().sum(),
        border=True,
    )
    (
        col1,
        col2,
    ) = st.columns(2, gap="medium")
    with col1:
        fig = px.scatter(
            anv_entregue,
            y="Prefixo",
            x="Data de Entrega Cliente",
            # color="Prefixo",
            # color="Data VTI",
            title="Progresso Data Entrega - Prefixo",
        )
        st.plotly_chart(fig)
    sum_prefixo = vti_aprovado["Data VTI"].value_counts().sort_values()
    # sum_prefixo = sum_prefixo.sort_values(by="Data VTI")
    # st.dataframe(vti_count)
    # st.dataframe(sum_prefixo)
    # fig2 = px.scatter(
    #     sum_prefixo,
    #     # x="Data VTI",
    #     y="count",
    # )
    # # fig2.update_layout(xaxis=dict(tickmode="linear"))
    # # fig2.update_layout(yaxis=dict(tickformat=".0f"))
    # # fig2.update_xaxes(range=["01-24", "12-25"])
    # st.plotly_chart(fig2)
    ## quantidade de aeronaves entregues
    # st.dataframe(df)
    with col2:
        # st.dataframe(vti_aprovado)
        fig2 = px.scatter(
            anv_entregue,
            x="Data Recebimento",
            y="Data de Entrega Cliente",
            color="Prefixo",
            title="Prazo entre Data de Recebimento - Data Entrega Cliente",
        )
        st.plotly_chart(fig2)
    st.divider()
    #     fig = px.scatter(anv_entregue, x="Data de Entrega Cliente", y="Prefixo")
    #     st.plotly_chart(fig)
    #     st.divider()
    #     fig2 = px.histogram(entregue_count, x="Data de Entrega Cliente", nbins=10)
    #     # st.plotly_chart(fig2)
    #     fig3 = px.scatter(entregue_count, x="Data de Entrega Cliente", y="Prefixo")
    # st.plotly_chart(fig3)
    st.dataframe(vti_aprovado, hide_index=True)
    # st.dataframe(anv_entregue, hide_index=True)
