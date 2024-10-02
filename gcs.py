import time
from pymavlink import mavutil


def start_gcs():
    # Listen for messages from the drone's IP (e.g., 192.168.4.2)
    master = mavutil.mavlink_connection('udp:0.0.0.0:14550')

    print("Waiting for drone heartbeat...")
    master.wait_heartbeat()
    print("Drone heartbeat received.")

    while True:
        msg = master.recv_match(blocking=True)
        if msg:
            print(f"Received message: {msg}")
        time.sleep(1)


if __name__ == "__main__":
    start_gcs()
