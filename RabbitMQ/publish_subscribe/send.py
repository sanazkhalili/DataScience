<<<<<<< HEAD
import sys

import pika


credent = pika.PlainCredentials(username = "san", password = "123", erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.185", virtual_host = "pub_sub")
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.exchange_declare(exchange = "ex_log", exchange_type = "fanout")

message = sys.argv[1]
channel.basic_publish(exchange = "ex_log",
                      routing_key = '',
                      body = message)

print(message)
conn.close()
=======
import sys

import pika


credent = pika.PlainCredentials(username = "san", password = "123", erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.185", virtual_host = "pub_sub")
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.exchange_declare(exchange = "ex_log", exchange_type = "fanout")

message = sys.argv[1]
channel.basic_publish(exchange = "ex_log",
                      routing_key = '',
                      body = message)

print(message)
conn.close()
>>>>>>> a756265572a35c9219f8292dee8ce0c36c6ef430
