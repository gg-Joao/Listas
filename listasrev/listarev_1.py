a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
if a > b: 
 print(a)
elif  a == b:
 print('Os numeros são iguais')
else:
 print(b)

 # exercio 2

 
valores = []
for i in range(4):
    valor = int(input(f"Digite o {i + 1}º valor inteiro: "))
    valores.append(valor)


media = sum(valores) / len(valores)


menores = [v for v in valores if v < media]
maiores_ou_iguais = [v for v in valores if v >= media]


print(f"Média aritmética: {media:.2f}")
print(f"Números menores que a média: {menores}")
print(f"Números maiores ou iguais à média: {maiores_ou_iguais}")

# exercio 3

