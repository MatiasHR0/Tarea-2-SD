import grpc
from grpc_server.proto import servicio_pb2
from grpc_server.proto import servicio_pb2_grpc

def run():
    # Crear el canal de conexión al servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = servicio_pb2_grpc.PedidoServiceStub(channel)
        # Enviar una solicitud al servidor gRPC
        response = stub.CrearPedido(servicio_pb2.PedidoRequest(nombreProducto="Laptop", precio=999.99))
        print("Estado del pedido: " + response.estado)

if __name__ == '__main__':
    run()

