import pika, json

params = pika.URLParameters('YOUR-URL-HERE')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='app1', body=json.dumps(body), properties=properties)
    channel.basic_publish(exchange='', routing_key='app2', body=json.dumps(body), properties=properties)


