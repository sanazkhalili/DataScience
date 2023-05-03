from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic

### connect to kafka
admin_kafka = KafkaAdminClient(bootstrap_servers = ['192.168.241.128:9092'])
list_topics = admin_kafka.list_topics()
print(list_topics)
print(admin_kafka.list_consumer_groups())
print(admin_kafka.DEFAULT_CONFIG.keys())

### kafka producer
kafka_pro = KafkaProducer(bootstrap_servers=['192.168.241.128:9092'])
kafka_pro.send(topic = 'topic1', value = 'fffff'.encode())
kafka_pro.flush()

### kafka consumer
kafka_cons = KafkaConsumer("topic1",
                           bootstrap_servers=['192.168.241.128:9092'],
                           auto_offset_reset='earliest')

for i in kafka_cons:
    print(i.value)

### Create new topic
new_topic_name = NewTopic ( name = "yasna", num_partitions = 1, replication_factor = 1 )
admin_kafka.create_topics(new_topics = [new_topic_name]   , validate_only = False)