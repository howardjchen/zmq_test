import zmq
import pandas as pd
import random
import time


def publish_column_values(filename, column_name):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5555")  # Bind the publisher socket to a specific address and port

    df = pd.read_csv(filename)
    column_values = df[column_name]

    try:
        while True:
            for value in column_values:
                delay = random.uniform(0.1, 1)  # Random delay between 0.1 and 0.5 seconds
                message = f"{column_name}: {value}"
                socket.send_string(message)  # Publish the message
                time.sleep(delay)

    except KeyboardInterrupt:
        socket.send_string("quit")  # Publish the message
        print("Stopping publisher...")
        socket.close()
        context.term()


# Usage example
filename = "Daily_2023_06_15_tx_raw.csv"  # Replace with your CSV file path
column_name = "Price"  # Replace with the name of the desired column

publish_column_values(filename, column_name)
