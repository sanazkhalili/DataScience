import pika
import sys



message = sys.argv[1]

cred = pika.PlainCredentials(username = "san", password = "123", erase_on_connect = True)
param = pika.ConnectionParameters(host = "192.168.120.185",virtual_host = "myworkqueue", credentials = cred, port = 5672)

con = pika.BlockingConnection(parameters = param)
channel = con.channel()
channel.queue_declare("workqueue")
channel.basic_publish(exchange = '', routing_key = "workqueue", body = message)

con.close()