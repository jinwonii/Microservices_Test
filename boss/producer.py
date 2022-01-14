import pika
import json

params = pika.URLParameters('amqps://qqygxrme:2Ob8DTf3pIxUkC6fShXpXeFQuH9gr-8d@dingo.rmq.cloudamqp.com/qqygxrme')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='order', body=json.dumps(body), properties=properties)