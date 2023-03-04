import pika

credent = pika.PlainCredentials(username = "san", password = "123", erase_on_connect = True)
param = pika.ConnectionParameters(credentials = credent, host = "192.168.120.185", virtual_host = "pub_sub")
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()

channel.exchange_declare(exchange = 'ex_log', exchange_type = 'fanout')
result = channel.queue_declare(queue = '', exclusive = True)

queue_name = result.method.queue
print(queue_name)


channel.queue_bind(exchange = 'ex_log', queue = queue_name)

def callback(ch, method, prop, body):
    print(body)

channel.basic_consume(queue = queue_name,
                      on_message_callback = callback,
                      auto_ack = True)

channel.start_consuming()