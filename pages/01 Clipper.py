# Import the libraries
import streamlit as st
import geopandas as gpd
from io import StringIO

# Set up the page
st.set_page_config(page_title="Documentation")

# Page content
st.title("Geodata clipping application")
st.markdown("If you want to know how this app works please check the [description](..#geodata-clipping-application).")

# Files importations
with st.expander(":page_facing_up: Files importation:"):
    maskLayer = st.file_uploader("Import your mask",accept_multiple_files=True)
    #maskLayer = maskLayer.getvalue()
    maskLayer = gpd.read_file(maskLayer)
    st.write(maskLayer)
    #maskLayer = gpd.read_file(maskLayer.read())
    #st.pyplot(maskLayer.plot())