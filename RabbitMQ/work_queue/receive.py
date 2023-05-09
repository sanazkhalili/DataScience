import pika
import time


def callback(ch, method, prop, body):
    time.sleep(3)
    print("receive: ", body)
    ch.basic_ack(delivery_tag = method.delivery_tag)


credent = pika.PlainCredentials(username = "san", password = "123", erase_on_connect = True)
parameter = pika.ConnectionParameters(host = "192.168.120.185", virtual_host = "myworkqueue", credentials =credent , port = 5672)
conn = pika.BlockingConnection(parameters = parameter)


channel = conn.channel()
channel.queue_declare("workqueue")
channel.basic_consume(queue = "workqueue" ,on_message_callback = callback)
channel.start_consuming()