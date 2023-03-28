# Import the libraries
import streamlit as st

# Set up the page
st.set_page_config(page_title="Documentation")

# Page content
st.title("Geodata clipping application")

st.markdown("""
# Description
The `Geodata clipping application` is a web-based application that allow you to import and clip your
geographical data.

# Functionalities

### Data importation
The first functionality of the web app is to import the geodata files.
The mask used to clip the data should be a polygon geofile.
The allowed extensions are: kml/kmz, csv, shp, geojson.

The layer to be clipped can be a vector or raster data.

### Plot the imported files
After the importation, the layers are plotted to guarantee the user the success of the import.

### Plot the clipped file
The result of the clipped file is displayed.

### Download the result
The file resulting from the clipping operation can be downloaded as vector or raster data.
""")

_, poweredCol = st.columns([7,6])

poweredCol.markdown("*Powered by* [Sidoine DAKO](https://wa.me/22967602727) | Data analyst")