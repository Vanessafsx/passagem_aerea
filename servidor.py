import grpc
from concurrent import futures
import vendas_aereas_pb2
import vendas_aereas_pb2_grpc

class ServicoDeVendas(vendas_aereas_pb2_grpc.VendasServicer):
    def VerificarDisponibilidade(self, requisicao, contexto):
        # Aqui você pode inserir a lógica para verificar a disponibilidade de voos com base nos dados fornecidos pelo cliente.
        # No exemplo abaixo, estamos apenas retornando uma resposta fixa.
        disponivel = True
        categoria = vendas_aereas_pb2.ECONOMICA
        resposta = vendas_aereas_pb2.RespostaDisponibilidade(disponivel=disponivel, categoria=categoria)
        return resposta

def servir():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vendas_aereas_pb2_grpc.add_VendasServicer_to_server(ServicoDeVendas(), servidor)
    porta = servidor.add_insecure_port('[::]:50051')
    print(f'Servidor gRPC rodando na porta {porta}')
    servidor.start()
    servidor.wait_for_termination()

if __name__ == '__main__':
    servir()
