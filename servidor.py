import grpc
from concurrent import futures
import vendas_pb2
import vendas_pb2_grpc

class PassagensService(vendas_pb2_grpc.PassagensServiceServicer):
    def VerificarDisponibilidade(self, request, context):
        disponibilidade = True
        categoria = 'econômica'
        # TODO: Verificar a disponibilidade e a categoria da passagem
        response = vendas_pb2.PassagemResponse(disponibilidade=disponibilidade, categoria=categoria)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
vendas_pb2_grpc.add_PassagensServiceServicer_to_server(PassagensService(), server)

#adicionando servidor a porta 3000
server.add_insecure_port('[::]:3000')
server.start()

server.wait_for_termination()
