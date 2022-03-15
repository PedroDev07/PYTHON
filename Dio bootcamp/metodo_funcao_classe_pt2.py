class Calculadora:
    
    def __init__ (self):
        pass
    
    def soma(self,a,b):
        return a + b
    
    def subtracao(self,a,b):
        return a - b
    
    def multiplicacao(self,a,b):
        return a * b
    
    def divisao(self,a,b):
        return a / b
    

print('O que deseja fazer?')
print('a -> somar')
print('b -> subtrair')
print('c -> dividir')
print('d -> multiplicar')
x = input('digite a opcao: ')
calc= Calculadora()


if (x == "a"):
    z= int(input('digite o primeiro numero: '))
    b= int(input('digite o segundo numero: '))
    
    print(calc.soma(z,b))    

if (x == "b"):
    z= int(input('digite o primeiro numero: '))
    b= int(input('digite o segundo numero: '))
    print(calc.subtracao(z,b))

if (x == "c"):
    z= int(input('digite o primeiro numero: '))
    b= int(input('digite o segundo numero: '))
    print(calc.divisao(z,b))

if (x == "d"):
    z= int(input('digite o primeiro numero: '))
    b= int(input('digite o segundo numero:'))
    print(calc.multiplicacao(z,b))