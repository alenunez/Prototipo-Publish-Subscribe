import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola2')

message = 'Mensaje del publicador 2'
channel.basic_consume(queue='cola1', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='cola2', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='cola3', on_message_callback=callback, auto_ack=True)print("Mensaje enviado por el publicador 2: %r" % message)

connection.close()
