FROM golang:1.19
# Copying the codebase
RUN mkdir codebase
WORKDIR /codebase
RUN mkdir logs

COPY protobufs protobufs

RUN apt update
RUN apt install -y protobuf-compiler
RUN go install github.com/golang/protobuf/protoc-gen-go@latest
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
# Creating the proto classes
RUN protoc --go_out=pkg --go-grpc_out=pkg protobufs/example.proto
RUN go mod init pkg
RUN go get google.golang.org/grpc
RUN go mod tidy

CMD [ "echo", "Hello Matey!"]
