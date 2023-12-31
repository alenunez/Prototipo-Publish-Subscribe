import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola2')

def callback(ch, method, properties, body):
    print("Mensaje recibido por el suscriptor 2: %r" % body)

channel.basic_consume(queue='cola2', on_message_callback=callback, auto_ack=True)

print('Esperando mensajes...')
channel.start_consuming()
