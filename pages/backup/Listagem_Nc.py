from app import st, df

st.subheader("Selecione Prefixo")
prefixo = st.selectbox(
    "",
    df["Prefixo"].dropna().unique(),
    index=None,
    placeholder="Selecione a Aeronave",
)
if prefixo is not None:
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.subheader("NC em Aberto")
        # Filtra o dataset pelo selectbox
        # if pv_prefixo == "Prefixo":
        panes_filtered = df[df["Prefixo"] == prefixo]
        # elif pv_prefixo == "PV":
        #    panes_filtered = df[df["PV"] == pv]
        opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
        if panes_filtered is not None:
            st.dataframe(
                opened_pane["Descrição da Não Conformidade"],
                hide_index=True,
                height=280,
                width=500,
            )
        else:
            {}
    with col2:
        st.subheader("NC Concluidas")
        closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
        st.dataframe(
            closed_pane["Descrição da Não Conformidade"],
            hide_index=True,
            height=280,
            width=600,
        )
else:
    ""
