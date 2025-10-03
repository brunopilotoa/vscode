from app import st, df
import pandas as pd

# import plotly.express as px
from st_aggrid import AgGrid
from st_material_table import st_material_table

# config
st.set_page_config(
    page_title="Ocorrencias",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)
# st.get_option('theme.primaryColor')
# manipulação dos dados
df = df.dropna(subset=["PV", "Status"])
df["PV"] = df["PV"].astype("int64")
# df["Data NC"] = pd.to_datetime(df["Data NC"], dayfirst=True)
# df["Data NC"] = df["Data NC"].dt.strftime("%d/%m/%Y")
df = df.sort_values(by="Nº", ascending=True)
st.header("Ocorrências ")
em_aberto = df[df["Status"] != "Solucionado"]
encerrado = df[df["Status"] == "Solucionado"]
columns = [
    "Prefixo",
    "Modelo",
    "Data NC",
    "C.T",
    "Descrição da Não Conformidade",
    "Class NC",
    "Ação de Correção",
    "Resp. Correção",
    "Data",
    # "Falha Reincidente",
    "Validação QA",
    "Status",
]
df = df[columns]
# for i in df.columns i
options = [
    "Prefixo",
    "PV",
    # "Class NC", "Tipo NC", "6Ms", "Status"
]
with st.sidebar:
    st.subheader("Visualização Tabelas")
    selection = st.segmented_control(
        "Por", options, selection_mode="single", default=None, width="content"
    )
    if selection == "Prefixo":
        prefixo = st.selectbox("Selecione o Prefixo", df["Prefixo"].dropna().unique())
    if selection == "PV":
        pv = st.selectbox("Selecione o PV", df["PV"].dropna().unique())
    class_nc = st.segmented_control(
        label="Classificação", options=df["Class NC"].dropna().unique()
    )
    ct = (st.segmented_control("Selecione o CT", options=df["C.T"].unique()),)
print(df.columns)

if selection == "Prefixo":
    filtered_df = df[df["Prefixo"] == prefixo]
    st.markdown(f"Total de Ocorrencias {len(filtered_df)}")
    # fig = px.scatter(filtered_df, x="Data NC", y="C.T")
    # print(filtered_df.columns)
    # st.plotly_chart(fig)
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        filtered_df_columns = filtered_df[columns]
        AgGrid(filtered_df_columns, hide_index=True)
    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        AgGrid(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        AgGrid(filtered_df, hide_index=True)
    elif class_nc is None:
        AgGrid(filtered_df, hide_index=True)

if selection == "PV":
    filtered_df = df[df["PV"] == pv]
    if class_nc == "AVI":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        AgGrid(filtered_df, hide_index=True)
        if filtered_df is None:
            ""
    if class_nc == "CÉL":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        AgGrid(filtered_df, hide_index=True)
    if class_nc == "GMP":
        filtered_df = filtered_df[filtered_df["Class NC"] == class_nc].sort_values(
            by="Data NC", ascending=True
        )
        AgGrid(filtered_df, hide_index=True)
    elif class_nc is None:
        "Selecione CEL , GMP , AVI no Menu Lateral"
# if selection == "Class NC":

# filtered_df = df[df["Class NC"] == class_nc]
# AgGrid(filtered_df, hide_index=True)
elif selection is None:
    st.write(
        "Selecione Prefixo ou PV na Barra Lateral"
    )  # st.subheader("Use A Barra Lateral Para Filtrar ")''
st.divider()
