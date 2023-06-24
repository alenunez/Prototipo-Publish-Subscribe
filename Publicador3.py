import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola3')

message = 'Mensaje del publicador 3'
channel.basic_publish(exchange='', routing_key='cola3', body=message)
print("Mensaje enviado por el publicador 3: %r" % message)

connection.close()
