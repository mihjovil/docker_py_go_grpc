# docker_py_go_grpc
This repository is to create a gRPC server and client using Python and Go respectively. However, one would not be too far from doing both on Python or both on Go.
1. [Requirements](#requirements)
2. [Tasks](#tasks)
3. [Usage](#usage)


## Requirements
This repository has the code to create a server container and a client container using [Docker](https://www.docker.com). Therefore, Docker must be installed in one's machine before continuying with the project. However, if one wishes to use it locally on one's own machine, one can also use the code in the repository to do so. This will require however, that one has [gRPC](https://grpc.io/docs/) in one's own machine (this process is very different depending on one's OS and which language one is going to use with the Protobufs (Python or Go).

## Tasks
The tasks one needs to implement before actually using the code in this repository are the following:
1. Implement the action on the server. This is basically the logic the server will execute when receiving a request from a gRPC client. The name of the task should match the one displayed on the `protobufs/example.proto`file.
2. Implement the request function in the client. As previously mentioned, the idea of the client in this repo is to be in Go, however, one can implement it in any of the languages supported by gRPC.

## Usage
In order to use this repository, the easiest way to get something out of it is to run the `docker-compose.yml` file. If you are not familiar with Docker, I recommend checking their documentation at least for a brief introduction to what it does and how it does it. The commands one needs to execute in the terminal in the root directory of the project are the following:

```
docker compose build

docker compose up

```

The first one will use both the `Dockerfile` in `client` and the `Dockerfile` in `server` to build both environments, while the second command will run the containers and put them in a Docker network, which will allow the continers to communicate with each other. 
