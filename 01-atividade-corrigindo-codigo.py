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

    # Filtrando cada número
    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)
        

    if numero < 0:
        negativos.append(numero) 
    elif numero > 0:
        positivos.append(numero) 


# Armazenando quantidades & Evitando erro caso quantidade de pares ou impares = 0
quantidade_pares = len(pares)
quantidade_impares = len(impares)

if quantidade_pares == 0:
    media_pares = "Vazio"
else:
    media_pares = sum(pares) / quantidade_pares

if quantidade_impares == 0:
    media_pares = "Vazio"
else:
    media_impares = sum(impares) / quantidade_impares




# Imprimindo as estatísticas
print("\n=== Estatísticas dos números ===")
print(f"Quantidade de pares: {len(pares)}")
print(f"Quantidade de ímpares: {len(impares)}")
print(f"Quantidade de positivos: {len(positivos)}")
print(f"Quantidade de negativos: {len(negativos)}")
print(f"Maior número: {max(numeros_geral)}")
print(f"Menor número: {min(numeros_geral)}")
print(f"Média dos números pares: {media_pares:.2}")
print(f"Média dos números ímpares: {media_impares:.2}")
print(f"Média de todos os números: {sum(numeros_geral)/len(numeros_geral):.2}")
numeros_geral.reverse()
print(f"Números na ordem inversa: {numeros_geral}")