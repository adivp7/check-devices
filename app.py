import subprocess
import os
import streamlit as st
# os.system("apt install -y hwinfo")
os.system("wget https://cdn.geekbench.com/Geekbench-5.4.5-Linux.tar.gz")
os.system("tar -xf Geekbench-5.4.5-Linux.tar.gz")
c=subprocess("./Geekbench-5.4.5-Linux/geekbench5",capture_output=True)
st.write(c.stdout.decode())
st.write("----end----")
