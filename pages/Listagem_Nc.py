from app import st, df

st.subheader("Selecione Prefixo")
# seleciona PV ou Prefixo
# pv_prefixo = st.radio("", ("PV", "Prefixo"))
# if pv_prefixo == "Prefixo":
#    prefixo = st.selectbox(
#        "",
#       df[pv_prefixo].unique(),
#        index=None,
#        placeholder="Selecione a Aeronave",
#    )
# Cria o selectbox
prefixo = st.selectbox(
    "",
    df["Prefixo"].unique(),
    index=None,
    placeholder="Selecione a Aeronave",
)
col1, col2 = st.columns(2)
with col1:
    st.subheader("NC em Aberto")
    # Filtra o dataset pelo selectbox
    # if pv_prefixo == "Prefixo":
    panes_filtered = df[df["Prefixo"] == prefixo]
    # elif pv_prefixo == "PV":
    #    panes_filtered = df[df["PV"] == pv]

    # opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
    if panes_filtered is None:
        print("Nada")
    else:
        st.dataframe(
            panes_filtered["Descrição da Não Conformidade"],
            hide_index=True,
            height=280,
            width=600,
        )
with col2:
    st.subheader("NC Concluidas")
    closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
    st.dataframe(
        closed_pane["Descrição da Não Conformidade"],
        hide_index=True,
        height=280,
        width=600,
    )
