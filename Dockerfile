FROM python:3.11-bullseye

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    libproj-dev \
    libgeos-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# GDAL environment
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Python dependencies
RUN pip install --upgrade pip
RUN pip install numpy==1.26.0
RUN pip install \
    branca==0.8.1 \
    folium==0.20.0 \
    geopandas==1.1.1 \
    leafmap==0.52.2 \
    mapclassify==2.10.0 \
    streamlit \
    streamlit-folium==0.25.2 \
    rasterio==1.4.3 \
    localtileserver==0.10.6

# Copy app code and rasters
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "sequestree.py", "--server.port=8501", "--server.address=0.0.0.0"]


