import subprocess
import os
import streamlit as st
os.system("sudo apt-get install -y hwinfo")
c=subprocess.run("hwinfo",shell=True,capture_output=True)
st.write(c.stdout.decode())
st.write("----end----")
