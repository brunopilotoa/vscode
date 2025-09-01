from app import st, df
import numpy as np
import pandas as pd
import plotly.express as px

# manipulação dos dados
df = df.dropna(subset=["PV", "Status"])
df["PV"] = df["PV"].astype("int64")
df["Data NC"] = pd.to_datetime(df["Data NC"], dayfirst=True)
df["Data NC"] = df["Data NC"].dt.strftime("%d/%m/%Y")
df = df.sort_values(by="Nº", ascending=True)
# st.title("Ocorrencias ")
# tab1, tab2, tab3 = st.tabs(["Dataframe", "Gráficos Nc", "Previsão"])
# total_ocorrencias = len(df)
em_aberto = df[df["Status"] == "Solucionado"]
# print(df.columns)
# print(df["Status"].unique())
# st.subheader(f"Total de Ocorrencias {total_ocorrencias}")
st.markdown(f"Em Aberto {len(em_aberto)} Ocorrencias")
# with tab1:
options = [
    "Prefixo",
    "PV",
    # "Class NC", "Tipo NC", "6Ms", "Status"
]
# st.dataframe(df, hide_index=True, selection_mode="multi-column")
# with st.sidebar:
# st.subheader("Visualização Tabelas")
selection = st.segmented_control("Por", options, selection_mode="single")
class_nc = st.segmented_control(
    label="Classificação", options=df["Class NC"].dropna().unique()
)
# print(df.columns)
# tipo_nc = st.selectbox("Tipo NC", options=df["Tipo NC"].dropna().unique())
# ct = st.segmented_control("Selecione o CT", options=df["C.T"].unique())

# ct = st.pills(label="C.T", options=df["C.T"].dropna().unique())
# print(ct)
# data_filter = st.slider(
#     "Data",
#     min_value=df["Data NC"].min(),
#     max_value=df["Data NC"].max(),
#     value=(df["Data NC"].min(), df["Data NC"].max()),
# )
# selection = st.select_slider("Selecione o Filtro", options)
# delivered_not = st.radio(
#     "Entregue - Não Entregue", options=["Entregue", "N Entregue"]
# )
if selection == "Prefixo":
    prefixo = st.selectbox("Selecione o Prefixo", df["Prefixo"].dropna().unique())
    filtered_df = df[df["Prefixo"] == prefixo]
    st.markdown(f"Total de Ocorrencias {len(filtered_df)}")
    # fig = px.scatter(filtered_df, x="Data NC", y="C.T")
    # print(filtered_df.columns)
    # st.plotly_chart(fig)
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
        # if ct == 9.1:
        #     filtered_dfa = filtered_df[filtered_df["C.T"] == 9.1]
        #     st.dataframe(filtered_dfa, hide_index=True)
        # if ct == "9.2":
        #     filtered_dfa = filtered_df[filtered_df["C.T"] == "9.2"]
        #     st.dataframe(filtered_dfa, hide_index=True)

    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
    elif class_nc is None:
        st.dataframe(filtered_df, hide_index=True)

if selection == "PV":
    pv = st.selectbox("Selecione o PV", df["PV"].dropna().unique())
    filtered_df = df[df["PV"] == pv]
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
        if filtered_df is None:
            ""
    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        st.dataframe(filtered_df, hide_index=True)
    elif class_nc is None:
        "Selecione CEL , GMP , AVI no Menu Lateral"
# if selection == "Class NC":

# filtered_df = df[df["Class NC"] == class_nc]
# st.dataframe(filtered_df, hide_index=True)
elif selection is None:
    # st.write(
    #     "Selecione Prefixo ou PV na Barra Lateral"
    # )  # st.subheader("Use A Barra Lateral Para Filtrar ")''
    # st.divider()

    ""
# with tab2:
#     st.subheader("Gráficos Relacionados a Ncs ")
#     (
#         col1,
#         col2,
#     ) = st.columns(2, gap="small")
#     with col1:
#         # histograma das ocorrencias por prefixo
#         fig = px.histogram(
#             df,
#             y="Prefixo",
#             # color="Prefixo",
#             title="Contagem de Ocorrencias Por Aeronave",
#             text_auto=True,
#         )
#         fig.update_layout(bargap=0.2)
#         st.plotly_chart(fig)
#     #     # segunda figura
#     #     figbar = px.bar(
#     #         df,
#     #         x="Class NC",
#     #         title="Quantidades por Setor",
#     #     )
#     #     # st.plotly_chart(figbar)
#     #     # terceira
#     #     fig_pie_resolvido = px.pie(
#     #         df,
#     #         names=df["Status"],
#     #         title="Comparação Entre NC Aberta e Solucionada",
#     #     )
#     #     st.plotly_chart(fig_pie_resolvido)
#     with col2:
#         fig2 = px.histogram(
#             df,
#             x="Data NC",
#             title="Distribuição das Ocorrencias Por Data",
#         )
#         #     fig2.update_layout(
#         #         bargap=0.1,
#         #         # xaxis=dict(tickmode="array"),
#         #         xaxis_tickformat="%m - %Y",
#         #     )
#         st.plotly_chart(fig2)
#         #     fig_pie = px.pie(
#         #         df,
#         #         names="Class NC",
#         #         title="Porcentagem entre Setor",
#         #     )
#         #     st.plotly_chart(fig_pie)
#         # with col3:
#         fig3 = px.scatter(
#             df,
#             x="Data NC",
#             title="Espaçamento das Ocorrencias",
#         )
#         # fig3.update_layout(xaxis_tickformat="%m - %Y")
#         st.plotly_chart(fig3)
#     #     fig_pie_ct = px.pie(df, names="C.T", title="Porcentagem por CT", color="C.T")
#     #     st.plotly_chart(fig_pie_ct)
# with tab3:
#     st.write("Previsão de entregas")
#     df_entrega = pd.read_excel(
#         "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
#         sheet_name=0,
#         header=1,
#     )
#     df_entrega["Data de Entrega Cliente"] = pd.to_datetime(
#         df_entrega["Data de Entrega Cliente"], errors="coerce"
#     )
#     df_entrega["Data Recebimento"] = pd.to_datetime(
#         df_entrega["Data Recebimento"], errors="coerce"
#     )
#     # print(df_entrega.columns)
#     # print(df_entrega["Data Recebimento"].dtype)
#     fig_scatter_recebimento = px.scatter(
#         df_entrega, x="Data Recebimento", y="Prefixo", title="Data de Recebimento H23"
#     )
#     st.plotly_chart(fig_scatter_recebimento)
#     # print(df_entrega["Data de Entrega Cliente"].dtype)
#     # print(df_entrega["Data Recebimento"].dtype)

#     df_entrega["dif_date"] = (
#         df_entrega["Data de Entrega Cliente"] - df_entrega["Data Recebimento"]
#     ).dt.days
#     print(df_entrega["dif_date"])
#     st.dataframe(df_entrega)
#     fig_sc_entrega = px.scatter(
#         df_entrega,
#         y="dif_date",
#         x="Data de Entrega Cliente",
#         # color="Prefixo",
#         trendline="ols",
#     )
#     st.plotly_chart(fig_sc_entrega)
