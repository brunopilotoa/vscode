import streamlit as st
from app import df, px, pd
from io import BytesIO

buffer = BytesIO()
edited_df = st.data_editor(df)
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    edited_df.to_excel(writer, index=False)

st.download_button(
    label="Download Excel",
    data=buffer.getvalue(),
    file_name="teste.xlsx",
    mime="application/vnd.ms-excel",
)
