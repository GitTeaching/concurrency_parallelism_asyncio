import pika, json

# with RabbitMQ cloud
#params = pika.URLParameters('YOUR-URL-HERE')

# with RabbitMQ localhost
credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='app1')


def callback(ch, method, properties, body):
    print('Received in app1')
    data = json.loads(body)
    print(data)


channel.basic_consume(queue='app1', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()