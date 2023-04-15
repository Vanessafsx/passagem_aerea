import grpc
import vendas_pb2
import vendas_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3000') as channel:
        stub = vendas_pb2_grpc.PassagensServiceStub(channel)
        response = stub.VerificarDisponibilidade(vendas_pb2.PassagemRequest(data_ida='2023-05-01', data_volta='2023-05-10', origem='São Paulo', destino='Rio de Janeiro'))
        print("Disponibilidade: ", response.disponibilidade)
        print("Categoria: ", response.categoria)

if __name__ == '__main__':
    run()
