<<<<<<< HEAD
import pika
import sys
from elasticsearch import Elasticsearch


def callback(ch, method, prop, body):
    es = Elasticsearch(hosts="http://192.168.120.111:9200")
    es.index(index="test", document={"message":body.decode('ascii')})


credent = pika.PlainCredentials(username ="san" , password ="123" , erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.111", virtual_host ="topic", port = 5672 )
connect = pika.BlockingConnection(parameters = param)
channel = connect.channel()

channel.exchange_declare(exchange = "log_topic", exchange_type = "topic")
res = channel.queue_declare(queue = '')
name = res.method.queue

rout = "info"

channel.queue_bind(queue = name,
                   exchange = "log_topic",
                   routing_key = rout)

channel.basic_consume(queue = name, on_message_callback = callback, auto_ack = True)

channel.start_consuming()
=======
import pika
import sys
from elasticsearch import Elasticsearch


def callback(ch, method, prop, body):
    es = Elasticsearch(hosts="http://192.168.120.111:9200")
    es.index(index="test", document={"message":body.decode('ascii')})


credent = pika.PlainCredentials(username ="san" , password ="123" , erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.111", virtual_host ="topic", port = 5672 )
connect = pika.BlockingConnection(parameters = param)
channel = connect.channel()

channel.exchange_declare(exchange = "log_topic", exchange_type = "topic")
res = channel.queue_declare(queue = '')
name = res.method.queue

rout = "info"

channel.queue_bind(queue = name,
                   exchange = "log_topic",
                   routing_key = rout)

channel.basic_consume(queue = name, on_message_callback = callback, auto_ack = True)

channel.start_consuming()
>>>>>>> a756265572a35c9219f8292dee8ce0c36c6ef430
