# ML2020-Uber-Data-Analysis
ML2020-Uber-Data-Analysis

### Installing Geopandas

If you encounter some issue while installing Geopandas follow this guide.

Navigate to the **lib** folder and install the following.

Python 3.9

1 - **pip install Fiona-1.8.18-cp39-cp39-win_amd64.whl**  
2 - **pip install GDAL-3.2.1-cp39-cp39-win_amd64.whl**  
3 - **pip install geopandas-0.6.2-py2.py3-none-any.whl**  

Python 3.8

1 - **pip install Fiona-1.8.18-cp38-cp38-win_amd64.whl**  
2 - **pip install GDAL-3.1.4-cp38-cp38-win_amd64.whl**  
3 - **pip install geopandas-0.6.2-py2.py3-none-any.whl**  


**Tested on Python 3.9.1**

The **WHL** files are obtained from https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal  

**rtree** is required to support the Spatial join in Geopandas  

**pip install Rtree** and restart your jupyter kernel or Python interpreter.

