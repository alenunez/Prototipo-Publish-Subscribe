import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola2')

message = 'Mensaje del publicador 2'
channel.basic_publish(exchange='', routing_key='cola2', body=message)
print("Mensaje enviado por el publicador 2: %r" % message)

connection.close()
