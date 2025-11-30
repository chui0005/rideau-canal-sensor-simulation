import time
import random
import json
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Load environment variables
load_dotenv()

SEND_INTERVAL = int(os.getenv("SEND_INTERVAL_SECONDS", "10"))

DEVICE_CONFIG = {
    "Dows Lake": os.getenv("CONNECTION_STRING_DOWSLAKE"),
    "Fifth Avenue": os.getenv("CONNECTION_STRING_FIFTHAVE"),
    "NAC": os.getenv("CONNECTION_STRING_NAC"),
}

# Validate configuration
for location, conn in DEVICE_CONFIG.items():
    if not conn:
        raise ValueError(f"Missing connection string for {location}")


def generate_sensor_data() -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ice_thickness_cm": round(random.uniform(15.0, 45.0), 1),
        "surface_temperature_c": round(random.uniform(-15.0, 0.0), 1),
        "snow_accumulation_cm": round(random.uniform(0.0, 30.0), 1),
        "external_temperature_c": round(random.uniform(-25.0, 5.0), 1),
    }


def main():
    print("Starting IoT device simulators...")

    # Create one IoT client per location/device
    clients = {
        location: IoTHubDeviceClient.create_from_connection_string(conn)
        for location, conn in DEVICE_CONFIG.items()
    }

    try:
        while True:
            for location, client in clients.items():
                payload = generate_sensor_data()
                payload["location"] = location

                message = Message(json.dumps(payload))
                message.content_type = "application/json"
                message.content_encoding = "utf-8"

                client.send_message(message)
                print(f"[{location}] Sent telemetry: {payload}")

            time.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("Stopping telemetry transmission...")

    finally:
        for client in clients.values():
            client.disconnect()

if __name__ == "__main__":
    main()
