import pika
import uuid

class fibonachiRpcClient():
    def __init__(self):
            self.credent = pika.PlainCredentials(username = "san", password ="123", erase_on_connect = True )
            self.param = pika.ConnectionParameters(port = 5672, credentials = self.credent, host = "192.168.120.185", virtual_host = "rpc")
            self.connect = pika.BlockingConnection(parameters = self.param)
            self.channel = self.connect.channel()

            result = self.channel.queue_declare(queue = '', exclusive = True)
            self.name_queue = result.method.queue

            self.channel.basic_consume(
                queue = self.name_queue,
                on_message_callback = self.on_response,
                auto_ack = True
            )
            self.response = None
            self.corr_id = None

    def on_response(self, ch, method, prop, body):

        if self.corr_id == prop.correlation_id:
            self.response = body

    def call(self, n):
           self.response = None
           self.corr_id = str(uuid.uuid4())
           self.channel.basic_publish(exchange = "",
                                      routing_key = "rpc_queue",
                                      body = str(n),
                                      properties = pika.BasicProperties(reply_to = self.name_queue,
                                                                        correlation_id = self.corr_id))
           self.connect.process_data_events(time_limit = None)

           return int(self.response)

fib = fibonachiRpcClient()
print(" [x] requesting fib(30)")

res = fib.call(30)

print(res)