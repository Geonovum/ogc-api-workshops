# docker file voor ogc wps (pygeopapi) 
# 

# FROM geopython/pygeoapi:latest
FROM geopython/pygeoapi:0.19.0

WORKDIR /pygeoapi

LABEL author='Niels Hoffmann'
LABEL name='ogc api processes workshop'

ADD requirements.txt /pygeoapi/
RUN python3 -m pip install --no-cache-dir -r requirements.txt
