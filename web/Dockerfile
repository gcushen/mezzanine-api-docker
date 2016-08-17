FROM python:3.5-onbuild
MAINTAINER George Cushen

# Install Mezzanine dependencies.
RUN sed "s/^deb\ /deb-src /g" /etc/apt/sources.list >> /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && apt-get update && \
    apt-get install -y \
        libjpeg-dev &&\
    apt-get build-dep -y \
        python-imaging

ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Add start script
ADD ./start.sh /
