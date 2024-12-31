import pika
import os
import sys
import time

def main():
    def tackle_alert(ch, method, properties, body):
        print("Your message received, we will assign a team to it")
        print(f" message : {body}")

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.basic_consume(queue='alert.log', auto_ack=True, on_message_callback=tackle_alert)
    channel.start_consuming()

if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Alert Receiver Closed")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)