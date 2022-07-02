import subprocess
import os
import streamlit as st
# os.system("apt install -y hwinfo")
os.system("uname")
c=subprocess.run("lscpu",shell=True,capture_output=True)
st.write(c.stdout.decode())
st.write("----end----")
