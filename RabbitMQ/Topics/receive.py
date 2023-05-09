import pika
import sys

def callback(ch, method, prop, body):
    print(ch, body)


credent = pika.PlainCredentials(username ="san" , password ="123" , erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.185", virtual_host ="topic", port = 5672 )
connect = pika.BlockingConnection(parameters = param)
channel = connect.channel()

channel.exchange_declare(exchange = "log_topic", exchange_type = "topic")
res = channel.queue_declare(queue = '')
name = res.method.queue

rout = sys.argv[1]

channel.queue_bind(queue = name,
                   exchange = "log_topic",
                   routing_key = rout)

channel.basic_consume(queue = name, on_message_callback = callback, auto_ack = True)

channel.start_consuming()
