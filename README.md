# Seid Cubro – Garage Environmental Monitoring System

This repository contains the complete software stack for an Internet of Things (IoT) garage environmental monitoring system developed for **CS260 – Introduction to Cloud Computing and IoT**.

The system continuously measures temperature and humidity in a garage environment using a physical sensor, transmits the data through a cloud-based MQTT broker, stores it in a cloud database, and visualizes it using data analytics tools.

---

## System Overview

### End-to-End Data Flow

    DHT11 Sensor
        ↓
    Arduino Uno
        ↓ (USB Serial)
    Python Publisher
        ↓ (MQTT over TLS)
    HiveMQ Cloud
        ↓
    MongoDB Atlas
        ↓
    CSV Export
        ↓
    Tableau Visualization

This architecture separates sensing, networking, storage, and visualization into modular components.

---

## Hardware Components

- Arduino Uno  
- DHT11 Temperature & Humidity Sensor  
- Jumper wires  
- Laptop/PC acting as the network gateway  

---

## Software Components

### Arduino
- Reads temperature and humidity from the DHT11 sensor
- Outputs formatted readings over USB serial

### Python (Edge / Gateway)
- Reads serial data from the Arduino
- Publishes data to HiveMQ using MQTT over TLS
- Subscribes to MQTT data and stores it in MongoDB Atlas
- Exports stored data to CSV for analysis

### Cloud Services
- HiveMQ Cloud – MQTT broker
- MongoDB Atlas – Cloud-hosted database

### Analytics & Visualization
- CSV file as an intermediate dataset
- Tableau dashboards for visualization and analysis

---

## Repository Contents

- dht11dataReadFormatfinal.ino  
  Arduino sketch that reads DHT11 sensor data and prints formatted output to serial

- arduino_to_hivemq.py  
  Reads serial data from Arduino and publishes JSON messages to HiveMQ

- mqtt_to_mongo.py  
  Subscribes to MQTT messages and inserts data into MongoDB Atlas

- mongo_to_csv.py  
  Exports MongoDB data into a CSV file

- iot_data.csv  
  Generated CSV containing timestamped temperature and humidity readings

- README.md  
  Project documentation

---

## Data Format

MQTT JSON Payload Example:

    {
      "timestamp": "2025-12-10T21:03:24Z",
      "temperature": 25,
      "humidity": 18
    }

MongoDB Document Structure:

    {
      "_id": ObjectId(...),
      "timestamp": "2025-12-10T21:03:24Z",
      "temperature": 25,
      "humidity": 18
    }

---

## How the System Runs

- The Arduino continuously reads temperature and humidity from the DHT11 sensor.
- Readings are sent via USB serial to a Python script running on a laptop.
- The Python publisher formats the data as JSON and publishes it to HiveMQ using MQTT over TLS.
- HiveMQ routes the data to subscribed clients.
- A Python subscriber stores incoming messages in MongoDB Atlas.
- Data is exported from MongoDB to a CSV file.
- Tableau connects to the CSV file to visualize trends and perform analysis.

Only the garage laptop must remain powered on for continuous data collection. Cloud services operate independently.

---

## Analysis Capabilities

- Temperature and humidity trends over time
- Hourly averages
- Identification of:
  - Top 5 warmest hours
  - Top 5 coldest hours
  - Most humid periods
  - Least humid periods

---

## Future Improvements

- Move the MQTT-to-database bridge to a cloud VM instead of a local machine
- Replace the DHT11 sensor with a higher-precision sensor (e.g., DHT22)
- Implement real-time dashboards without CSV intermediates
- Add alerting for temperature or humidity threshold violations

---

## Author

Seid Cubro  
CS260 – Introduction to Cloud Computing and IoT  
Wilkes University
