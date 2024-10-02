import time
from pymavlink import mavutil

# Change port to 50002
connection = mavutil.mavlink_connection('udp:127.0.0.1:50002')

# Wait for a heartbeat from the drone
def listen_for_heartbeat():
    while True:
        # Wait for the heartbeat message
        message = connection.recv_match(type='HEARTBEAT', blocking=True)
        if message:
            print(f"Received heartbeat from Drone: {message}")
        time.sleep(1)

# Start listening for heartbeat messages
listen_for_heartbeat()
