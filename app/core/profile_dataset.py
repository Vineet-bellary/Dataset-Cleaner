import streamlit as st
import pandas as pd


"""
This module returns basic Details of the uploaded Dataset.
"""


def get_readable_size(size_in_bytes: int) -> str:
    """Converts bytes to a human-readable string (KB, MB, GB)."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PB"


def dataProfiling(df: pd.DataFrame) -> dict:
    profile = {}

    profile["rows"] = df.shape[0]
    profile["cols"] = df.shape[1]

    # For number of duplicate rows
    profile["duplicate_rows"] = len(df[df.duplicated()])
    column_names = df.columns.to_list()
    profile["column_names"] = column_names

    raw_size = df.memory_usage(deep=True).sum()
    profile["readable_size"] = get_readable_size(raw_size)

    return profile
