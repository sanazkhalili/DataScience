import pika
import sys


def callback(cha, method, prop, body):
    print(method.routing_key, body)

credent = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
param = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host = "routing", credentials = credent)
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.exchange_declare(exchange = "log_dir", exchange_type = "direct")


res = channel.queue_declare(queue = '', exclusive = True)
name = res.method.queue

severities = sys.argv[1:]
for i in severities:
    channel.queue_bind(queue = name, exchange = "log_dir", routing_key = i)


channel.basic_consume(queue = name,
                      on_message_callback = callback)


channel.start_consuming()