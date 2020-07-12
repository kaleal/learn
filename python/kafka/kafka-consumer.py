import json
import time
import yaml

from confluent_kafka import Consumer, KafkaError

with open('config.yml', 'r') as file:
  config = yaml.safe_load(file.read())

settings = {'client.id': 'kafka-python-console-sample-consumer',
        'group.id': 'kafka-python-console-sample-group',
        'bootstrap.servers': ','.join(config['kafka']['brokers']),
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': '/etc/pki/tls/certs/ca-bundle.crt',
        'sasl.mechanisms': 'PLAIN',
        'sasl.username': config['kafka']['credentials']['username'],
        'sasl.password': config['kafka']['credentials']['password'],
        'api.version.request': True,
        'enable.auto.commit': True,
        'broker.version.fallback': '0.10.2.1',
        'log.connection.close': False}

print(settings)

consumer = Consumer(settings)
consumer.subscribe(config['kafka']['topics'])
while True:
  msg = consumer.poll(timeout=10.0)
  if msg == None:
    time.sleep(0.1)
  elif type(msg.error()) == KafkaError:
    time.sleep(0.1)
  else:
    print(msg.value())
consumer.unsubscribe()

