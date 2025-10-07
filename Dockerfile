FROM python:3

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
RUN pip install -r requirements.txt

# Copy app code and rasters
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "sequestree.py", "--server.port=8501", "--server.address=0.0.0.0"]