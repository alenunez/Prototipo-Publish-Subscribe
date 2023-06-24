import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola3')

def callback(ch, method, properties, body):
    print("Mensaje recibido por el suscriptor 3: %r" % body)

channel.basic_consume(queue='cola3', on_message_callback=callback, auto_ack=True)

print('Esperando mensajes...')
channel.start_consuming()
