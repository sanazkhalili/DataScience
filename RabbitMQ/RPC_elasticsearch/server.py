import pika
from elasticsearch import Elasticsearch

def elk(body):
    es = Elasticsearch(hosts = 'http://192.168.120.000:9200')
    res = es.search(index = body)['hits']['hits']
    return res

def on_response(ch, method, prop,body):
    result = elk(body.decode('ascii'))
    ch.basic_publish(body =  result[0]['_source']['title'] ,exchange = '', routing_key = prop.reply_to, properties = pika.BasicProperties(correlation_id = prop.correlation_id))
    ch.basic_ack(delivery_tag = method.delivery_tag)




credent = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
param = pika.ConnectionParameters(host = "192.168.120.185", port = 5672, virtual_host = "my_elk_host", credentials = credent)
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.queue_declare(queue = "rpcqueue")
channel.basic_qos(prefetch_count = 1)
channel.basic_consume(on_message_callback = on_response, auto_ack = True, queue = "rpcqueue")
channel.start_consuming()
