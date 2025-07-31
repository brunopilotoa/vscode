from app import df, pd, st, px

df_panes = pd.read_excel(
    "W:\H23 - Montagem Final\Base de Dados_Montagem Final_H23_2025.xlsx",
    engine="openpyxl",
    # sheet_name="NCs_H23",
    header=1,
)
anv_entregue = df_panes[df_panes["STATUS FINAL"] == "ENTREGUE"]

# cria o radio entre Pv ou Prefixo
# prefixo_pv = st.radio(
#    "Selecione PV ou Matricula",
#    ("PV", "Prefixo"),
# )
an_filtered = anv_entregue[
    anv_entregue["Data Recebimento ", "Data AEV", "Data VTI", "Data de Entrega Cliente"]
]
st.write("Selecione o Prefixo Abaixo")
# Cria o selectbox
prefixo = st.selectbox(
    "",
    anv_entregue["Prefixo"].unique(),
    index=None,
    placeholder="Selecione a Aeronave",
    key="",
)
anv_entregue
fig = px.line(
    anv_entregue,
    x=prefixo,
    y=an_filtered,
)

# percentagem de entregues vs programados
# meta = st.slider("Insira a Meta Desejada", 0, 50)
# contagem_ifr_entregue = anv_entregue["VFR/IFR"].value_counts()
# fig8 = px.pie(
#    contagem_ifr_entregue,
#    values=contagem_ifr_entregue,
#    names="count",
# )
# st.dataframe()
st.plotly_chart(fig)
