from app import pd, st, px

df_panes = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    # sheet_name="NCs_H23",
    header=1,
)
# col1, col2 = st.columns(2, gap="small")
# with col1:
vti_aprovado = df_panes[
    (df_panes["Status VTI"] == "APROVADO") & (df_panes["Data VTI"] != "AGUARDANDO")
]
vti_aprovado["Data VTI"] = pd.to_datetime(vti_aprovado["Data VTI"])
# data_vti = vti_aprovado[vti_aprovado["Data VTI"]].value_counts()
# vti_aprovado = vti_aprovado["Data VTI"].dt.strftime("%d/%m/%Y")
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
# with col2:
anv_entregue = df_panes[df_panes["STATUS FINAL"] == "ENTREGUE"]
# entrega = anv_entregue["Data de Entrega Cliente"].dropna()
# entrega = pd.to_datetime(entrega)
# anv_entregue
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
st.plotly_chart(fig6)
