import subprocess
import streamlit as st
c1=subprocess.run("lspci",shell=True,capture_output=True)
st.write(cl.output.decode())
