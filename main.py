import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

# Streamlit page configuration
st.set_page_config(page_title="RACKANALYSIS", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: Rack Store EDA")
st.markdown('<style> div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# File uploader
fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

if fl is not None:
    # Determine file type and read accordingly
    filename = fl.name
    st.write(f"Uploaded file: {filename}")
    
    if filename.endswith('.csv'):
        df = pd.read_csv(fl, encoding="ISO-8859-1")
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        df = pd.read_excel(fl, engine='openpyxl')
    elif filename.endswith('.txt'):
        df = pd.read_csv(fl, delimiter='\t', encoding="ISO-8859-1")  # Assuming tab-delimited for txt
    else:
        st.error("Unsupported file format.")
else:
    # Load default CSV if no file uploaded
    os.chdir(r"C:\Users\shedr\Desktop\dashboard\dashboard")
    df = pd.read_csv("dd.csv", encoding="ISO-8859-1")

# Display DataFrame
col1, col2 = st.columns((2))
with col1:
    st.subheader("Data Preview:")
    st.dataframe(df)

# You can add more EDA visualizations and analysis here
st.subheader("Visualizations")
if 'Category' in df.columns and 'Sales' in df.columns:
    fig_bar=px.bar(df, x='Category', y= 'Sales', title='Sales by Category')
    st.plotly_chart(fig_bar)