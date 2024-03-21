import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='valor')

# Função para enviar o valor para a fila
def enviar_valor(valor):
    channel.basic_publish(exchange='', routing_key='valor', body=valor)

# Obter o valor do formulário
valor = input('Digite um valor: ')

# Enviar o valor para a fila
enviar_valor(valor)

# Fechar a conexão com o RabbitMQ
connection.close()
