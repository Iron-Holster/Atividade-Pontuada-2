import os
os.system("cls || clear") 

# Variáveis para armazenar as estatísticas
QUANTIDADE_NUMEROS = 5
numeros_geral = []
pares = []
impares = []
positivos = []
negativos = []

# Variáveis para armazenar os números
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))

    numeros_geral.append(numero)

    # Processando cada número
    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)
        

    if numero < 0:
        negativos.append(numero) 
    elif numero > 0:
        positivos.append(numero) 


# Armazenando quantidades
quantidade_pares = len(pares)
quantidade_impares = len(impares)

media_pares =


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {len(pares)}")
print(f"Quantidade de ímpares: {len(impares)}")
print(f"Quantidade de positivos: {len(positivos)}")
print(f"Quantidade de negativos: {len(negativos)}")
print(f"Maior número: {max(numeros_geral)}")
print(f"Menor número: {min(numeros_geral)}")
print(f"Média dos números pares: {media_pares}")
print(f"Média dos números ímpares: {media_impares}")
print(f"Média de todos os números: {numeros_geral}")
print(f"Números na ordem inversa: {reversed(numeros_geral(numero))}")