import zmq
import time

def subscribe_messages():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")  # Connect the subscriber socket to the publisher's address

    # Subscribe to all messages
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    try:
        while True:
            start_time = time.time()  # Start time for measuring elapsed time
            message = socket.recv_string()  # Wait for a message from the publisher
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            print("Received message:", message, "Elapsed time:", elapsed_time, "seconds")
            if(message == "quit"):
                print("Publisher close topic, Stopping subscriber...")
                socket.close()
                context.term()
                quit()

    except KeyboardInterrupt:
        print("Stopping subscriber...")
        socket.close()
        context.term()

# Usage example
subscribe_messages()
