import pika


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib ( n - 1 ) + fib ( n - 2 )


def on_request(ch, method, prop, body):
    n = int ( body )
    res = fib ( n )

    ch.basic_publish ( exchange = "",
                       routing_key = prop.reply_to,
                       body = str ( res ),
                       properties = pika.BasicProperties ( correlation_id = prop.correlation_id ) )

    ch.basic_ack ( delivery_tag = method.delivery_tag )


credent = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
param = pika.ConnectionParameters(port = 5672, credentials = credent, host = "192.168.120.185", virtual_host = "rpc")

connect = pika.BlockingConnection(parameters = param)


channel = connect.channel()
channel.queue_declare(queue = "rpc_queue")

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue = "rpc_queue",on_message_callback =on_request)
channel.start_consuming()