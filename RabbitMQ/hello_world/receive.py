<<<<<<< HEAD
import pika


def callback(ch, method, properties, body):
    print("context", body)

credential = pika.PlainCredentials(username = "san", password = "123",erase_on_connect = True)
parametr = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host = "mybroker", credentials = credential )

conn = pika.BlockingConnection(parametr)
channel = conn.channel()

channel.queue_declare("myqueue")


channel.basic_consume(queue = "myqueue", on_message_callback = callback, auto_ack = True)
print("start consuming")
=======
import pika


def callback(ch, method, properties, body):
    print("context", body)

credential = pika.PlainCredentials(username = "san", password = "123",erase_on_connect = True)
parametr = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host = "mybroker", credentials = credential )

conn = pika.BlockingConnection(parametr)
channel = conn.channel()

channel.queue_declare("myqueue")


channel.basic_consume(queue = "myqueue", on_message_callback = callback, auto_ack = True)
print("start consuming")
>>>>>>> a756265572a35c9219f8292dee8ce0c36c6ef430
channel.start_consuming()