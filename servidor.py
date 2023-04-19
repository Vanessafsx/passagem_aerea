from concurrent import futures
import grpc
import vendaspassagens_pb2
import vendaspassagens_pb2_grpc

# Configurações do servidor
PORT = 5000

# Dicionário com as informações das passagens disponíveis
passagens = {
    'origem1': {
        'destino1': {'data1': ['1a. classe', 'executivo', 'econômica'],
                     'data2': ['1a. classe', 'executivo', 'econômica']},
        'destino2': {'data1': ['1a. classe', 'executivo', 'econômica'],
                     'data2': ['1a. classe', 'executivo', 'econômica']}},
    'origem2': {
        'destino3': {'data1': ['1a. classe', 'executivo', 'econômica'],
                     'data2': ['1a. classe', 'executivo', 'econômica']},
        'destino4': {'data1': ['1a. classe', 'executivo', 'econômica'],
                     'data2': ['1a. classe', 'executivo', 'econômica']}}
}

class VendasPassagensServicer(vendaspassagens_pb2_grpc.VendasPassagensServicer):

    def VerificarDisponibilidade(self, request, context):
        if request.destino in passagens[request.origem] and request.data in passagens[request.origem][request.destino]:
            disponibilidade = True
            categoria = passagens
            [request.origem][request.destino][request.data]
        else:
            disponibilidade = False
            categoria = []
        return vendaspassagens_pb2.Resposta(disponibilidade=disponibilidade, categoria=categoria)

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vendaspassagens_pb2_grpc.add_VendasPassagensServicer_to_server(VendasPassagensServicer(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    print(f'Servidor iniciado na porta {PORT}')
    server.wait_for_termination()

if __name__ == '__main__':
    start_server()