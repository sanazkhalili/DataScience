import pika
import sys

severity = "info"
message = "Hello I am elasticsearch"

credent = pika.PlainCredentials(username ="san" , password ="123" , erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.111", virtual_host ="topic", port = 5672 )
connect = pika.BlockingConnection(parameters = param)


channel = connect.channel()
channel.exchange_declare(exchange = "log_topic", exchange_type = "topic")

channel.basic_publish(exchange = "log_topic", routing_key = severity, body = message)

connect.close()
