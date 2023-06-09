import grpc
import vendas_aereas_pb2
import vendas_aereas_pb2_grpc

def executar():
    with grpc.insecure_channel('localhost:50051') as canal:
        stub = vendas_aereas_pb2_grpc.VendasStub(canal)
        resposta = stub.VerificarDisponibilidade(
            vendas_aereas_pb2.RequisicaoDisponibilidade(
                data_partida ='2023-05-01',
                data_retorno = '2023-05-10',
                origem = 'SFO',
                destino = 'LAX'
            )
        )

        if resposta.disponivel:
            # print(f'Assentos disponíveis na categoria {resposta.categoria}.')
            if resposta.categoria == vendas_aereas_pb2.Categoria.ECONOMICA:
                print("Assentos disponíveis na categoria econômica.")
            elif resposta.categoria == vendas_aereas_pb2.Categoria.EXECUTIVA:
                print("Assentos disponíveis na categoria executiva.")
            elif resposta.categoria == vendas_aereas_pb2.Categoria.PRIMEIRA_CLASSE:
                print("Assentos disponíveis na categoria primeira classe.")
        else:
            print('Não há assentos disponíveis para o itinerário solicitado.')

if __name__ == '__main__':
    executar()