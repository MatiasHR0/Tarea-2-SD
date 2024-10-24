import grpc
from concurrent import futures
import kafka
from kafka import KafkaProducer
from proto import servicio_pb2
from proto import servicio_pb2_grpc
import json

# Clase que implementa los métodos definidos en el .proto
class PedidoServiceServicer(servicio_pb2_grpc.PedidoServiceServicer):
    def __init__(self, kafka_producer):
        self.kafka_producer = kafka_producer

    def CrearPedido(self, request, context):
        # Procesar el pedido y publicarlo en Kafka
        pedido = {
            "nombreProducto": request.nombreProducto,
            "precio": request.precio
        }
        self.kafka_producer.send('pedidos', value=pedido)
        self.kafka_producer.flush()
        return servicio_pb2.PedidoResponse(estado="Pedido recibido y enviado a Kafka")


def serve():
    # Crear el productor Kafka
    producer = KafkaProducer(
        bootstrap_servers=['kafka1:9092'],
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

    # Configurar el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicio_pb2_grpc.add_PedidoServiceServicer_to_server(PedidoServiceServicer(producer), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server corriendo en puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
