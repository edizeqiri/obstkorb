# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies required for building TLSH, radare2, and ssdeep
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    automake \
    libtool \
    && rm -rf /var/lib/apt/lists/*

# Install ssdeep from source
RUN git clone --depth 1 https://github.com/ssdeep-project/ssdeep.git \
    && cd ssdeep \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install \
    && ldconfig

# Install radare2 from source
RUN git clone https://github.com/radareorg/radare2.git \
    && cd radare2 \
    && sys/install.sh

# Install TLSH from source
RUN git clone https://github.com/trendmicro/tlsh.git \
    && cd tlsh \
    && git checkout master \
    && ./make.sh

# Install Python dependencies
# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter
RUN pip install jupyter

# Copy the rest of your application's code
COPY . .

# Copy the start-up script and give execution permissions
COPY start.sh .
RUN chmod +x ./start.sh

# Expose the port Jupyter will run on
EXPOSE 8888

# Set the default command to run the start-up script
#CMD ["./start.sh"]
