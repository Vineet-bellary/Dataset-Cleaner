import streamlit as st
from core.dataUploader import dataset_upload


def show_upload():
    data = dataset_upload()

    if data is not None:
        st.session_state["uploaded_data"] = data
        st.session_state["is_data_uploaded"] = True
        st.success(
            icon=":material/thumb_up:",
            body="Dataset Uploaded Successfully",
        )
