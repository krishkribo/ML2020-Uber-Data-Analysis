# ML2020-Uber-Data-Analysis  
ML2020-Uber-Data-Analysis  

### Requirements  

1 - Anaconda  
2 - Python 3.7+  
3 - Jupyter notebook  


### Setting up the environment  
1 - Run the command **conda env create -f environment.yml** to setup your conda environment.  
2 - If everything is successful run **activate conda ML_UBER_ENV**  
3 - If you encounter any error and wish to rerun the setup execute **conda env update --file environment.yml** after fixing the issue. (optional)  
4 - Execute **conda install -c anaconda ipykernel**  
5 - Run **python -m ipykernel install --user --name=ML_UBER_ENV*  
6 - Install the Geopands library as per the instructions below.  


### Installing Geopandas  

If you encounter some issue while installing Geopandas follow this guide.  

Navigate to the **lib** folder and install the following.  

Python 3.7 (Recommended if you installed our env)  

1 - **pip install Fiona-1.8.18-cp37-cp37m-win_amd64.whl**  
2 - **pip install GDAL-3.2.1-cp37-cp37m-win_amd64.whl**   
3 - **pip install geopandas-0.6.2-py2.py3-none-any.whl**   

Python 3.9

1 - **pip install Fiona-1.8.18-cp39-cp39-win_amd64.whl**  
2 - **pip install GDAL-3.2.1-cp39-cp39-win_amd64.whl**  
3 - **pip install geopandas-0.6.2-py2.py3-none-any.whl**  

Python 3.8

1 - **pip install Fiona-1.8.18-cp38-cp38-win_amd64.whl**  
2 - **pip install GDAL-3.1.4-cp38-cp38-win_amd64.whl**  
3 - **pip install geopandas-0.6.2-py2.py3-none-any.whl**  

### NOTE: Do not forget to select the appropriate kernel in your jupyter notebook  

**Tested on Python 3.7**

The **WHL** files are obtained from https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal  

**rtree** is required to support the Spatial join in Geopandas  

**pip install Rtree** and restart your jupyter kernel or Python interpreter.

### Data Analysis ipy notebook  
Google drive link: https://drive.google.com/file/d/1tjLbnm7ZJUHnD6nlVoy8Rv4ZayYJasfV/view?usp=sharing
Due to the size of the notebook it cannot be uploaded on the Git repository.  

### NOTE: If you run into any issues, feel free to request us for assistance either by creating issues or contacting us directly.  

