FROM golang:1.19
# Copying the codebase
RUN mkdir codebase
WORKDIR /codebase
RUN mkdir logs

COPY protobufs protobufs

RUN apt update
RUN apt install -y protobuf-compiler

ENV PYTHONPATH="$PWD/codebase"
# Installing Python's dependencies
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt --default-timeout=30
RUN python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/nlp.proto
EXPOSE 9000

CMD [ "python3", "grpc_server.py" ]
