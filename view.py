from flask import Flask, render_template,request
import os
import json
import pika
app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
     username = request.form.get('valor')
     Nome = request.form.get('Nome')
     print('aqui imprime um valor teste')
     print(username)
     print(Nome)
#tranformando os valores texto para json
     json_username = username
     json_email =  Nome            
     payload = json.dumps({"username": json_username, "email":json_email }, indent=4)
     headers = { 'Content-Type': 'application/json'}
   
    
#Enviando valores para o rabbitMQ


# Conexão com o RabbitMQ
    credentials = pika.PlainCredentials('username','password')
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',credentials=credentials, port=5672)
)
    channel = connection.channel()
    channel.exchange_declare('test', durable=True, exchange_type='topic')
    channel.queue_declare(queue= 'A')
    channel.queue_bind(exchange='test', queue='A', routing_key='A')

    #message= 'hello consumer fila C!!!!!'
    message = payload 
    channel.basic_publish(exchange='test', routing_key='A', body= message)
    channel.close()
    return render_template('index.html')
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8082))
    app.run(debug=True, host='0.0.0.0', port=port)