# RabbitMQ Simple Alert System

## Description
**RabbitMQ Simple Alert System** is a lightweight Python-based application that demonstrates the use of RabbitMQ for sending and receiving alerts in real-time. It leverages RabbitMQ's robust messaging capabilities to efficiently process and deliver alert messages between producers and consumers in a distributed system.

## Features
- **Producer-Consumer Architecture:** Implements a producer to send alert messages and a consumer to process them.
- **Real-Time Alerts:** Ensures quick delivery of messages for time-sensitive notifications.
- **Scalable Design:** Supports multiple consumers for distributed environments.

## Future Features
- **More Scalable Design:** Supports multiple producers for distributed environments.
- **Customizable Message Queues:** Allows configuration of RabbitMQ queues and routing keys for flexible alert delivery.
- **Error Handling:** Includes basic error-handling mechanisms for message acknowledgment and retries.

## Use Cases
- Monitoring system alerts.
- Real-time notifications for applications.
- Event-driven architectures.

## Technologies
- **RabbitMQ:** Message broker for handling queues and message delivery.
- **Python:** Core programming language for producer and consumer scripts.
- **pika:** Python library for interacting with RabbitMQ.

## Getting Started

### Prerequisites
- Install RabbitMQ on your system or use a cloud-hosted RabbitMQ service.
- Install Python (version 3.6 or higher recommended).
- Install the required Python dependencies using the following command:
  ```bash
  pip install pika
