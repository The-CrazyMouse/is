import grpc  # Import gRPC library
from concurrent import futures  # For handling concurrent connections
import time  # Time handling (not used here but can be useful)
import unary_pb2_grpc as pb2_grpc  # Import generated gRPC client/server code
import unary_pb2 as pb2  # Import generated gRPC message definitions


class UnaryService(pb2_grpc.UnaryServicer):
    """
    gRPC service implementation for UnaryService.
    This class implements the methods defined in the service.
    """

    def __init__(self, *args, **kwargs):
        pass  # Constructor doesn't need additional logic for now

    def GetServerResponse(self, request, context):
        """
        Handles the incoming gRPC request and sends back a response.
        - `request`: The message sent by the client.
        - `context`: Context for the RPC call (used for metadata, cancellation, etc.)
        """
        # Extract the message sent by the client
        message = request.message

        # Prepare the response
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        # Return the response in the expected MessageResponse format
        return pb2.MessageResponse(**result)


def serve():
    """
    Starts the gRPC server and listens for incoming connections.
    - Creates a thread pool with a maximum of 10 workers to handle requests.
    - Registers the UnaryService to the server.
    - Starts the server to listen on port 50051.
    """
    # Create a gRPC server with a thread pool
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register the UnaryService to the server
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)

    # Bind the server to port 50051
    server.add_insecure_port('[::]:50051')

    # Start the server and wait for termination
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    # Start the server when the script is executed
    serve()

