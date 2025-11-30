# Sensor Simulation Repository 

## Overview

This repository contains a Python-based IoT sensor simulator that sends telemetry data to Azure IoT Hub.
The simulator mimics ice and environmental monitoring sensors deployed at three Ottawa locations:
  - Dow’s Lake
  - Fifth Avenue
  - National Arts Centre (NAC)

Each simulated sensor periodically sends JSON-formatted telemetry including ice thickness, temperature, and snow accumulation, along with a UTC timestamp.


## Prerequisites

- Python 3.9+
- Azure IoT Hub
- A registered IoT Device in your IoT Hub
- The device connection string
- pip package manager

## Installation

### Clone repo 
- git clone https://github.com/chui0005/rideau-canal-sensor-simulation.git
- cd rideau-canal-sensor-simulation

### Create and activate a virtual environment
- python -m venv venv
- source venv/bin/activate    # Linux / macOS

### install dependencies 
- pip install -r requirements.txt


## Configuration

### Create a .env file in the project root:
Get connection string for each device
- CONNECTION_STRING_DOWSLAKE = "Your IoT Hub device connection string here"
- CONNECTION_STRING_FIFTHAVE = "Your IoT Hub device connection string here"
- CONNECTION_STRING_NAC = "Your IoT Hub device connection string here"

## Usage
```
python sensor_simulator.py
```

## Code Structure
```
rideau-canal-sensor-simulation/
├── README.md                  # Setup and usage instructions
├── sensor_simulator.py        # Main simulation script
├── requirements.txt           # Python dependencies
├── .env              # Example environment variables
├── .gitignore
```

### Main Components

#### sensor_simulator.py: 
  - Initializes the IoT Hub client
  - Generates sensor data
  - Sends telemetry at regular intervals

##### Key Functions
  - generate_sensor_data(location: str) -> dict
    - Creates a telemetry payload with:
      - Ice thickness (cm)
      - Surface temperature (°C)
      - Snow accumulation (cm)
      - External temperature (°C)
      - UTC timestamp

  - main()
    - Connects to Azure IoT Hub
    - Iterates over all locations
    - Sends one telemetry message per location
    - Handles graceful shutdown on keyboard interrupt

## Sensor Data Format

- JSON schema
```
{
  "timestamp": "ISO-8601 UTC string",
  "location": "string",
  "ice_thickness_cm": "number",
  "surface_temperature_c": "number",
  "snow_accumulation_cm": "number",
  "external_temperature_c": "number"
}
```


- Example output
```
{
    "timestamp": "2025-11-29T19:28:15.567108+00:00",
    "ice_thickness_cm": 15.3,
    "surface_temperature_c": -1.2,
    "snow_accumulation_cm": 25.8,
    "external_temperature_c": -14.8,
    "location": "Dows Lake",
}
 ```
## AI Tools Used
- **Tool:** ChatGPT
- **Purpose and extent:** 
  - To create generate_sensor_data function


## Troubleshooting


## Common issues and fixes


