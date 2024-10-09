import streamlit as st
import plotly.express as px 
import pandas as pd 
import os
import warnings 
warnings.filterwarnings('ignore')

st.set_page_config( page_title="RACKANALYSIS", page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Rack Store EDA")
st.markdown('<style> div.block-container{padding-top:1 rem;}</style>',unsafe_allow_html=True)
fl= st.file_uploader(":file_folder: Upload a file", type= (["csv","txt","xlsx","xls"]))
if fl is not None:
    filename =fl.name
    st.write(filename)
    df =pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    os.chdir(r"C:\Users\shedr\Desktop\projects\datasets\healthcare-dataset-stroke-data.csv")   
    df =pd.read_csv("healthcare-dataset-stroke-data.csv", encoding ="ISO-8859-1")