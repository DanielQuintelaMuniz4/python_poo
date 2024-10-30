from FPS import Jogador
from armas import *

if __name__ == '__main__':
    j1 = Jogador()
    j2 = Jogador()
    print(f'Jogador 1: {j1}')
    print(f'Jogador 2: {j2}')

    j1.add_arma(Revolver())
    j1.add_arma(Lanca_Chamas())

    for x in range(1,8):
        j1.atirar(j1.armas[0], j2)
        print(f'Jogador 1: {j1}')
        print(f'Jogador 2: {j2}')
    j1.municiar(j1.armas[0])

    for x in range(1,5):
        j1.atirar(j1.armas[1], j2)
        print(f'Jogador 1: {j1}')
        print(f'Jogador 2: {j2}')
    j1.municiar(j1.armas[1])
