import pika, json

# with RabbitMQ cloud
#params = pika.URLParameters('YOUR-URL-HERE')

# with RabbitMQ localhost
credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='app2', body=json.dumps(body), properties=properties)


