from app import st, df
import pandas as pd

# import plotly.express as px
from st_aggrid import AgGrid

st.set_page_config(layout="wide")
print(df.columns)
columns = [
    "Prefixo",
    "Data NC",
    "C.T",
    "Descrição da Não Conformidade",
    "Ação de Correção",
    "Resp. Correção",
    "Data",
    "Status",
]
AgGrid(df)
filtered_df = df[columns]
AgGrid(filtered_df)
