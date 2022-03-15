class Calculadora:
    
    def __init__ (self, num1, num2):
        self.a=num1
        self.b=num2
    
    def soma(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def divisao(self):
        return self.a / self.b
    




if __name__ == '__main__':
    print('O que deseja fazer?')
    print('a -> somar')
    print('b -> subtrair')
    print('c -> dividir')
    print('d -> multiplicar')
    x = input('digite a opcao: ')
    
    print("xxx")
if (x == "a"):
    z= int(input('digite o primeiro numero'))
    b= int(input('digite o segundo numero'))
    calc= Calculadora(z,b)
    print(calc.soma())    

if (x == "b"):
    z= int(input('digite o primeiro numero'))
    b= int(input('digite o segundo numero'))
    calc= Calculadora(z,b)
    print(calc.subtracao())

if (x == "c"):
    z= int(input('digite o primeiro numero'))
    b= int(input('digite o segundo numero'))
    calc= Calculadora(z,b)
    print(calc.divisao())

if (x == "d"):
    z= int(input('digite o primeiro numero'))
    b= int(input('digite o segundo numero'))
    calc= Calculadora(z,b)
    print(calc.multiplicacao())