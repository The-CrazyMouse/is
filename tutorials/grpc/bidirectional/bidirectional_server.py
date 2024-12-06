from concurrent import futures  # Importing concurrent futures for handling threads
import grpc  # Importing gRPC library
import bidirectional_pb2_grpc as bidirectional_pb2_grpc  # Import generated bidirectional gRPC code


class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):
    """
    Service class that implements the Bidirectional gRPC service.
    """

    def GetServerResponse(self, request_iterator, context):
        """
        A Bidirectional streaming RPC method that receives a stream of messages
        from the client and sends back a stream of messages to the client.
        """
        # Iterating over the stream of requests from the client and yielding responses
        for message in request_iterator:
            yield message


def serve():
    """
    Starts the gRPC server and listens for incoming connections.
    - Creates a thread pool with a maximum of 10 workers to handle requests.
    - Registers the BidirectionalService to the server.
    - Starts the server to listen on port 50051.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Create the server with a thread pool
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)  # Add service to server
    server.add_insecure_port('[::]:50051')  # Bind the server to port 50051
    server.start()  # Start the server
    server.wait_for_termination()  # Wait for the server to stop


if __name__ == '__main__':
    # Start the server when the script is executed
    serve()

