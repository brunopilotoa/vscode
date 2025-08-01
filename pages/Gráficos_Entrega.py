from app import pd, st, px, df

df_panes = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    # sheet_name="NCs_H23",
    header=1,
)
col1, col2 = st.columns(2, gap="small")
with col1:
    vti_aprovado = df_panes[
        (df_panes["Status VTI"] == "APROVADO") & (df_panes["Data VTI"] != "AGUARDANDO")
    ]
    vti_aprovado["Data VTI"] = pd.to_datetime(vti_aprovado["Data VTI"])
    # data_vti = vti_aprovado[vti_aprovado["Data VTI"]].value_counts()
    # vti_aprovado = vti_aprovado["Data VTI"].dt.strftime("%d/%m/%Y")
    st.subheader("Aeronaves Aprovadas em VTI")
    st.markdown(vti_aprovado["Prefixo"].value_counts().sum())
    st.divider()

    # st.metric(vti_aprovado.value_counts().sum())
    fig5 = (
        px.scatter(
            vti_aprovado,
            y="Prefixo",
            # "Data Recebimento",
            x=[
                "Data VTI",
                "Data Recebimento",
            ],
            title="Progresso entre a Data de Recebimento até a Data da VTI",
            # trendline="expanding",
            # trendline_scope="overall",
        )
        .update_xaxes(title="")
        .update_yaxes(title="")
    )
    # fig5.add_hline(
    # y=data_vti,
    #    line_dash="dash",
    #    line_color="white",
    # annotation_text=f"Media: {average_value:.0f}",
    # annotation_position="bottom right",
    # )
    st.plotly_chart(fig5)
with col2:
    anv_entregue = df_panes[df_panes["STATUS FINAL"] == "ENTREGUE"]
    # entrega = anv_entregue["Data de Entrega Cliente"].dropna()
    # entrega = pd.to_datetime(entrega)
    # anv_entregue
    st.subheader("Aeronaves Entregues")
    st.markdown(anv_entregue["Prefixo"].value_counts().sum())
    st.divider()

    fig6 = (
        px.scatter(
            anv_entregue,
            x=["Data VTI", "Data de Entrega Cliente"],
            y="Prefixo",
            title="Progresso entre a VTI e a Entrega",
        )
        .update_yaxes(title="")
        .update_xaxes(title="")
    )
    fig6.add_vline(
        x="Data de Entrega Cliente",
        line_dash="dash",
        line_color="white",
        #    annotation_text=f"Media: {average_value:.0f}",
        #    annotation_position="bottom right",
    )
    st.plotly_chart(fig6)


## aeronaves entregues por mes
anv_entregue_filtered = anv_entregue[["Data de Entrega Cliente", "Prefixo"]]
anv_entregue_filtered["Data de Entrega Cliente"] = pd.to_datetime(
    anv_entregue_filtered["Data de Entrega Cliente"]
)
# anv_entregue_filtered["Mes_Ano"] = (
#    anv_entregue_filtered["Data de Entrega Cliente"]
#    .dt.to_period("M")
#    .value_counts()
#    .sum()
# )
# anv_entregue_filtered["Mes_Ano"]

# figa = px.bar(anv_entregue_filtered, x="Mes_Ano")
# st.plotly_chart(figa)
# st.dataframe(anv_entregue, hide_index=True)
# sum_anv_month = anv_entregue_filtered.groupby("Data de Entrega Cliente").sum()
# sum_anv_month
