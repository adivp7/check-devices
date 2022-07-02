import subprocess
import streamlit as st
c=subprocess.run("lspci",shell=True,capture_output=True)
st.write(c.output.decode())
