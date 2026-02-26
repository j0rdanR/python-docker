# Python/Docker Example

This repository contains a simple example of using Docker to containerise and
distribute a python application.

It doesn't do much, but you get the idea...

> Disclaimer: This repository is mainly for me to test GitHub Actions and the
> container registry. There are probably better examples out there.

## Dependencies

- Python 3.12
- Cowsay 6.1

## Building the Docker Image

```sh
docker build . -t python-docker:latest
```

## Running with Docker

```sh
docker run --rm -it python-docker:latest
```

## Running locally

```sh
python main.py
```
