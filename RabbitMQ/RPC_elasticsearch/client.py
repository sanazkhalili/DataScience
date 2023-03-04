import pika
import uuid

class readAllIndex():
    def __init__(self):
        credent = pika.PlainCredentials(username ="san" , password = "123", erase_on_connect = True)
        parameter = pika.ConnectionParameters(virtual_host = "my_elk_host", host = "192.168.120.185", credentials = credent,port = 5672)
        self.connect = pika.BlockingConnection(parameters = parameter)

        self.channel = self.connect.channel()

        queue = self.channel.queue_declare("", exclusive = True)
        self.name = queue.method.queue

        self.channel.basic_consume(queue=self.name,
                              on_message_callback = self.on_response,
                              auto_ack = True)

        self.corr_id = None
        self.resp = None

    def on_response(self, ch, method, prop, body):
        if prop.correlation_id == self.corr_id:
            self.resp = body

    def call(self, word):
        self.corr_id = str(uuid.uuid4())
        self.resp = None

        self.channel.basic_publish(
            exchange = '',
            body = str(word),
            properties = pika.BasicProperties(reply_to = self.name,
                                              correlation_id = self.corr_id),
            routing_key = 'rpcqueue'
        )

        self.connect.process_data_events(time_limit = None)

        return self.resp


object_read = readAllIndex()

result = object_read.call("books")

print(result)