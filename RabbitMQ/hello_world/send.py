<<<<<<< HEAD
import pika


credential = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
parameter = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host ="mybroker" ,credentials = credential)

conn = pika.BlockingConnection(parameter)
channel = conn.channel()
channel.queue_declare("queue2")# queue=myqueue

channel.basic_publish(exchange = '',
                      routing_key = "queue2",
                      body = "It is queue2")

print("my message send")
=======
import pika


credential = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
parameter = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host ="mybroker" ,credentials = credential)

conn = pika.BlockingConnection(parameter)
channel = conn.channel()
channel.queue_declare("queue2")# queue=myqueue

channel.basic_publish(exchange = '',
                      routing_key = "queue2",
                      body = "It is queue2")

print("my message send")
>>>>>>> a756265572a35c9219f8292dee8ce0c36c6ef430
conn.close()