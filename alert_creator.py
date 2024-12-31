import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

alert_message = input("alert message: ")
queue_create = channel.queue_declare("alert.log")

channel.basic_publish(exchange='', routing_key='alert.log', body=alert_message)
print(f"Alert message sent [' {alert_message} '] ")

connection.close()