from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <=30:
        print('O piloto {} percorreu {} km:'.format(piloto,trajeto))
        trajeto += velocidade
        time.sleep(0.5)

carro1 = Thread(target=carro,args=[5,'Pedro'])
carro2 = Thread(target=carro,args=[1,'Samuel'])

carro1.start()
carro2.start()