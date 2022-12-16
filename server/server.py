from concurrent import futures
from signal import signal, SIGTERM, SIGINT
import grpc
import os
from nlp_pb2 import Response, Request, Durations
import nlp_pb2_grpc
from datetime import datetime, timezone
import json
import time

# region Global variables
username = "user"
password = "pass"
# endregion

# region Auth interceptor
class AuthInterceptor(grpc.ServerInterceptor):
    """This class is the intercepotor that will handle the authentication of the requests"""
    def __init__(self):
        """This init function sets up the abortion for requests that do not pass the authentication
        """
        def abort(ignored_request, context):
            """This function handles the abortion of handling a request

            Args:
                context: the context for the received request
            """
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")

        self._abortion = grpc.unary_unary_rpc_method_handler(abort)
        print("Added abortion to interceptor!!!!!")
        print(self._abortion)

    def intercept_service(self, continuation, handler_call_details):
        """ This function handles the interception of all requests received by the server.
        It checks for the authentication and in case it fails aborts the request. Otherwise lets it pass
        to perform the regular behavior of the request.

        Args:
            continuation: the function that will be call the next step in case the interceptor gives a green light
            handler_call_details: the data that comes with the request. It is where the authentication values will travel

        Returns:
            _type_: a function for the server to take. It can be abortion of the request or continuation with the request's details
        """
        meta = dict(handler_call_details.invocation_metadata)       
        if "user" not in meta or "pass" not in meta:
            log.error("there is no user or pass in the request. Failed authentication")
            return self._abortion
        request_user, request_password = meta["user"], meta["pass"]
        if request_user == user and request_password == password:
            return continuation(handler_call_details)
        return self._abortion
            

# endregion

class ActionService(nlp_pb2_grpc.ClassificationsServicer):      

    def Action(self, request: Request, context) -> Response:
        """ TODO

        Args:
            request (Request): the gRPC request for Action
            context (_type_): the context in which the request lives

        Returns:
            Response: the gRPC response for Action
        """
        
        return Response()

def serve():
    """ This function is the one that starts the server and defines the handlers for the functions."""
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(AuthInterceptor(),),
        
    )
    nlp_pb2_grpc.add_ActionServicer_to_server(
        ActionService(), server
    )

    server.add_insecure_port(f"[::]:{config['port']}")
    server.start()

    def handle_sigterm(*_):
        """Function to handle a termination command (Ctrl -C) and shutdown gracefully the server
        """
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shutdown gracefully")

    print("Server started....")
    signal(SIGINT, handle_sigterm)    
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
