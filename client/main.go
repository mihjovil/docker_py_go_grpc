package main

import (
	"context"
	"log"

	"pkg/pkg"

	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

func main() {
	var conn *grpc.ClientConn
	conn, err := grpc.Dial("grpc_py:30300", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %s", err)
	}
	defer conn.Close()

	c := nlp.NewActionClient(conn)
	// Creating the metadata for authentication
	user, pass := "user", "pass"
	meta := metadata.Pairs("user", user, "pass", pass)
	ctx := metadata.NewOutgoingContext(context.Background(), meta)
	response, err := c.Action(ctx, &nlp.Request{Name: "Miguel"})
	if err != nil {
		log.Fatalf("failed to get response from Action. %s", err)
	} else {
		log.Printf("Got the following response from Action. %s", response)
	}
}
