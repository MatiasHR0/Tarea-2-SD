from confluent_kafka import Consumer

# Configura el Consumer para conectarse a los brokers
consumer_conf = {
    'bootstrap.servers': 'localhost:9093',
    'group.id': 'grupo-consumidor1',
    'auto.offset.reset': 'earliest'  # Empieza desde el principio si no hay un offset guardado
}
consumer = Consumer(consumer_conf)

consumer.subscribe(['el-topico1'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Espera 1 segundo por mensajes
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            
        print(f"Mensaje recibido: key={msg.key().decode('utf-8')}, value={msg.value().decode('utf-8')}, partition={msg.partition()}")

finally:
    consumer.close()