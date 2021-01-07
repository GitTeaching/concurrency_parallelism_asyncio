import pika, json

# with RabbitMQ cloud
#params = pika.URLParameters('YOUR-URL-HERE')

# with RabbitMQ local machine
credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='app2')


def callback(ch, method, properties, body):
    print('Received in app2')
    data = json.loads(body)
    print(data)


channel.basic_consume(queue='app2', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()