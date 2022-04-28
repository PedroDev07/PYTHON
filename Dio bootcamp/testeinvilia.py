Tamanho_Pista = int(input("Digite o comprimento da pista em metros: "))
Total_Voltas = int(input("Digite a quantidade de voltas: "))
Reabastecimento = int(input("Digite a quantidade de vezes que deseja reabastecer: "))
Consumo = int(input("Digite o consumo do carro em KM/L: "))

calc1 = Total_Voltas/Reabastecimento
reabastecimento1 = calc1*Tamanho_Pista

print(f"o número total de combustível até o 1° 1reabastecimento será de {reabastecimento1} litros")
