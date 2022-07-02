import subprocess
import os
import streamlit as st
c=subprocess.run("lspci",shell=True,capture_output=True)
st.write(c.stdout.decode())
st.write("done")
os.system("lspci")
