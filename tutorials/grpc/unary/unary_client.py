import grpc  # Import gRPC library
import unary_pb2_grpc as pb2_grpc  # Import generated gRPC client code
import unary_pb2 as pb2  # Import generated gRPC message definitions


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        # Initialize the client with server details
        self.host = 'localhost'  # Server address
        self.server_port = 50051  # Server port

        # Instantiate a channel to communicate with the server
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port)
        )

        # Bind the generated client stub to the channel
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse.
        It sends a message to the server and waits for a response.
        """
        # Create a Message object with the provided message string
        message = pb2.Message(message=message)

        # Log the message being sent
        print(f'Sending message: {message}')

        # Call the RPC method on the server and return the response
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    # Instantiate the client
    client = UnaryClient()

    # Call the RPC method with a test message
    result = client.get_url(message="Hello Server, you there?")

    # Print the server's response
    print(f'Server response: {result}')

