import subprocess
import os
import streamlit as st
os.system("apt install -y hwinfo")
c=subprocess.run("hwinfo",shell=True,capture_output=True)
st.write(c.stdout.decode())
st.write("----end----")
