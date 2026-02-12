import pandas as pd
import streamlit as st
from core.profile_dataset import dataProfiling


def show_profile(df: pd.DataFrame):
    data_profiling = dataProfiling(df)

    st.subheader("Dataset Overview", divider="red")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rows", data_profiling["rows"], border=True)
    with col2:
        st.metric("columns", data_profiling["cols"], border=True)
    with col3:
        st.metric("Duplicate Rows", data_profiling["duplicate_rows"], border=True)
    with col4:
        st.metric("RAM Usage", data_profiling["readable_size"], border=True)

    with st.expander(label="View Column Names", icon=":material/folder:"):
        cols = st.columns(4)
        for index, name in enumerate(data_profiling["column_names"]):
            with cols[index % 4]:
                st.code(name, language=None)
