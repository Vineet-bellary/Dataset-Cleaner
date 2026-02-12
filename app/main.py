import streamlit as st

from ui.show_upload import show_uploader
from ui.show_profiler import show_profile

st.set_page_config(page_title="Dataset Cleaner", page_icon=":broom:", layout="wide")

if "is_data_uploaded" not in st.session_state:
    st.session_state["is_data_uploaded"] = False

st.title("Dataset Cleaner")

show_uploader()

if st.session_state["is_data_uploaded"]:
    st.subheader("Data Preview", divider="red")

    data = st.session_state["uploaded_data"]
    # Showing Data Preview
    st.dataframe(data)

    # Showing Data Profile
    show_profile(data)
