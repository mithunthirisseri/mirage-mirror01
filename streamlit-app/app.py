import streamlit as st
import time

# Create a spinner with some text
with st.spinner('In progress...'):
    # Simulate a long-running task
    time.sleep(5)
    st.success('Loading completed!')