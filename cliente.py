import grpc
import vendaspassagens_pb2
import vendaspassagens_pb2_grpc

# Define o endereço do servidor
SERVER_ADDRESS = 'localhost:5000'

# Cria o canal de comunicação
channel = grpc.insecure_channel(SERVER_ADDRESS)

# Cria o stub do serviço VendasPassagens
stub = vendaspassagens_pb2_grpc.VendasPassagensStub(channel)

# Solicita as informações ao usuário
origem = input('Digite a cidade de origem: ')
destino = input('Digite a cidade de destino: ')
data = input('Digite a data de ida no formato YYYY-MM-DD: ')

# Cria a requisição
request = vendaspassagens_pb2.Passagem(origem=origem, destino=destino, data=data)

# Faz a chamada ao método VerificarDisponibilidade do servidor
response = stub.VerificarDisponibilidade(request)

# Verifica a disponibilidade das passagens
if response.disponibilidade:
    print('Passagens disponíveis nas categorias:')
    for categoria in response.categoria:
        print(f'- {categoria}')
else:
    print('Não há passagens disponíveis para esta rota na data informada.')
