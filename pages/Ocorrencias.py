from app import st, df
import numpy as np
import pandas as pd

df["PV"] = df["PV"].dropna()
# df["PV"] = df["PV"].astype(int)
print(df["PV"])
df["Data NC"] = pd.to_datetime(df["Data NC"], dayfirst=True)
df["Data NC"] = df["Data NC"].dt.strftime("%d/%m/%Y")
st.title("Ocorrencias ")
options = [
    "Prefixo",
    "PV",
    # "Class NC", "Tipo NC", "6Ms", "Status"
]
# st.dataframe(df, hide_index=True, selection_mode="multi-column")
with st.sidebar:
    st.subheader("Visualização")
    selection = st.segmented_control("Filtros", options, selection_mode="single")
    class_nc = st.pills(label="Classificação", options=df["Class NC"].dropna().unique())
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
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
        if ct == 9.1:
            filtered_dfa = filtered_df[filtered_df["C.T"] == 9.1]
            st.dataframe(filtered_dfa, hide_index=True)
        if ct == "9.2":
            filtered_dfa = filtered_df[filtered_df["C.T"] == "9.2"]
            st.dataframe(filtered_dfa, hide_index=True)

    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
    elif class_nc is None:
        st.dataframe(filtered_df, hide_index=True)

if selection == "PV":
    pv = st.selectbox("Selecione o PV", df["PV"].dropna().unique())
    filtered_df = df[df["PV"] == pv]
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc]
        st.dataframe(filtered_df, hide_index=True)
    elif class_nc is None:
        st.dataframe(filtered_df, hide_index=True)
# if selection == "Class NC":

# filtered_df = df[df["Class NC"] == class_nc]
# st.dataframe(filtered_df, hide_index=True)
else:
    ""  # st.subheader("Use A Barra Lateral Para Filtrar ")''
