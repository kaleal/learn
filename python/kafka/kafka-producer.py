import json
import yaml

from confluent_kafka import Producer

with open('config.yml', 'r') as file:
  config = yaml.safe_load(file.read())

conf = {'client.id': 'kafka-python-console-sample-consumer',
        'group.id': 'kafka-python-console-sample-group',
        'bootstrap.servers': ','.join(config['kafka']['brokers']),
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': '/etc/pki/tls/certs/ca-bundle.crt',
        'sasl.mechanisms': 'PLAIN',
        'sasl.username': config['kafka']['credentials']['username'],
        'sasl.password': config['kafka']['credentials']['password'],
        'api.version.request': True,
        'broker.version.fallback': '0.10.2.1',
        'log.connection.close': False}

print(conf)
data = {"nome": "Kleber", "beauty_index": 100}

producer = Producer(conf)
producer.produce(config['kafka']['topics'][0], json.dumps(data))
producer.flush(30)

