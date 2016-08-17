FROM python:3.5-onbuild
MAINTAINER George Cushen

# Install Mezzanine dependencies.
RUN sed "s/^deb\ /deb-src /g" /etc/apt/sources.list >> /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && apt-get update && \
    apt-get install -y \
        libjpeg-dev &&\
    apt-get build-dep -y \
        python-imaging

# Add start script
ADD ./start.sh /
