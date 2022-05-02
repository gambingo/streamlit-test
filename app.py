import platform

import streamlit as st


st.header("Python and Streamlit Sharing")
msg = f"This repo specifies python version ^3.9 but is using {platform.python_version()}."
st.write(msg)