from __future__ import print_function  # Ensures compatibility with Python 2 and 3

import grpc  # Import gRPC library
import bidirectional_pb2_grpc as bidirectional_pb2_grpc  # Import generated gRPC server/client code
import bidirectional_pb2 as bidirectional_pb2  # Import generated message classes


# Helper function to create a message object
def make_message(message):
    return bidirectional_pb2.Message(
        message=message
    )


# Generator function that produces multiple messages to be sent to the server
def generate_messages():
    messages = [
        make_message("First message"),
        make_message("Second message"),
        make_message("Third message"),
        make_message("Fourth message"),
        make_message("Fifth message"),
    ]
    # Iterates over the list and yields each message to the server
    for msg in messages:
        print("Hello Server Sending you the %s" % msg.message)
        yield msg


# Function to send the generated messages to the server and print responses
def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())  # Calling the bidirectional RPC
    for response in responses:
        print("Hello from the server received your %s" % response.message)  # Print the response


# Main function to create a channel and send messages to the server
def run():
    # Establishing an insecure gRPC channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)  # Creating a client stub
        send_message(stub)  # Sending messages to the server


if __name__ == '__main__':
    run()  # Running the client code when the script is executed

