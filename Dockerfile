# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libexpat1 \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    branca==0.8.1 \
    folium==0.20.0 \
    geopandas==1.1.1 \
    leafmap==0.52.2 \
    mapclassify==2.10.0 \
    streamlit \
    streamlit-folium==0.25.2 \
    rasterio==1.4.3\
    localtileserver==0.10.6

# Copy app files into container
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "sequestree.py", "--server.port=8501", "--server.address=0.0.0.0"]

