# base image
FROM python:3.9

# working directory
WORKDIR /app

# install system-dependencies
RUN apt-get update && apt-get install -y \
    graphviz \
    graphviz-dev \
    pkg-config \
    ffmpeg \
    libpq-dev \
    postgresql-client \
    sagemath \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip  # Upgrade pip to avoid old issues
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy the files into container
COPY src /app/src

WORKDIR /app/src
# expose the local port
EXPOSE 8888

# default command to run the application
CMD ["python", "main.py"]