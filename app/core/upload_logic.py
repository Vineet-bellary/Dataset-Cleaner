import streamlit as st
import pandas as pd


def dataset_upload() -> pd.DataFrame:
    data = st.file_uploader(
        label="Upload your Dataset", accept_multiple_files=False, type="CSV"
    )

    if data is not None:
        return pd.read_csv(data)

    return None
