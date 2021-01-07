import pika, json

params = pika.URLParameters('YOUR-URL-HERE')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='app3')


def callback(ch, method, properties, body):
    print('Received in app3')
    data = json.loads(body)
    print(data)


channel.basic_consume(queue='app3', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()