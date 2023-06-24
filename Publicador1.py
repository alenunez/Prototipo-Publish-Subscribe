import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola1')


message = 'Mensaje del publicador 1'
channel.basic_publish(exchange='', routing_key='cola1', body=message)
print("Mensaje enviado por el publicador 1: %r" % message)

connection.close()
