# Docker for Mezzanine CMS + API

Mezzanine API Docker is an instance of [Mezzanine CMS](http://mezzanine.jupo.org/) with the [REST API](http://gcushen.github.io/mezzanine-api/) which runs within Docker containers.

Three microservices are created, for *Mezzanine itself*, the *PostgreSQL database*, and the *Nginx web server*.

## Prerequisites

The following Docker products should be installed:

- [Docker Engine](https://docs.docker.com/engine/installation/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Machine](https://docs.docker.com/machine/install-machine/)

## Installation

To setup Mezzanine CMS with the REST API as Docker microservices:

1. Download this Mezzanine Docker project with `git`:

        git clone https://github.com/gcushen/mezzanine-api-docker.git
        cd mezzanine-api-docker

1. Create a new docker machine:

        docker-machine create -d virtualbox mezzanine

1. Build the images:

        docker-compose build

1. Start the microservices:

        docker-compose up -d

1. Open the URL given by the following command in your web browser:

        echo "http://$(docker-machine ip mezzanine)/"

    Login to the admin panel with username `admin` and password `default`.

## Getting Started

View the [documentation website](http://gcushen.github.io/mezzanine-api/#getting-started) or explore the [remote command line tool](http://gcushen.github.io/mezzanine-api/cli/) and [remote SDK](http://gcushen.github.io/mezzanine-api/client/).

## Community

Feel free to [star](https://github.com/gcushen/mezzanine-api-docker) Mezzanine API Docker on Github to show your support and monitor updates.

Join us in the [Mezzanine API chat room](https://gitter.im/gcushen/mezzanine-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) or leave a message and we will try to get back to you.

Please file a [ticket](https://github.com/gcushen/mezzanine-api-docker/issues) or contribute a pull request on GitHub for bugs or feature requests.

## License

Created by [George Cushen](http://cushen.me).

Released under the [MIT](https://github.com/gcushen/mezzanine-api-docker/blob/master/LICENSE) license.
