FROM --platform=linux/x86_64 python:2.7.18-stretch

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin

# Utopia

WORKDIR /utopia


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN sed -i 's/geos_version().decode()/geos_version().decode().strip()/' /usr/local/lib/python2.7/site-packages/django/contrib/gis/geos/libgeos.py

COPY . .

