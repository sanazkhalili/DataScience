import pika
import sys


credent = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
param = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host = "routing", credentials = credent)
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.exchange_declare(exchange = "log_dir", exchange_type = "direct")
message = ' '.join(sys.argv[2:])
severity_routing = sys.argv[1]
print( message)
print(severity_routing)
channel.basic_publish(exchange = "log_dir",
                      routing_key = severity_routing,
                      body = message)
conn.close()