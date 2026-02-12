import streamlit as st

from ui.UploadDataset import show_upload

st.set_page_config(page_title="Dataset Cleaner", page_icon=":broom:", layout="wide")

if "is_data_uploaded" not in st.session_state:
    st.session_state["is_data_uploaded"] = False

st.title("Dataset Cleaner")

show_upload()

if st.session_state["is_data_uploaded"]:
    st.subheader("Data Preview", divider="red")

    data = st.session_state["uploaded_data"]
    st.dataframe(data)
