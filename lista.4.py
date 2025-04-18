import math

a, b, c = map(float, input().split())
delta = b**2 - 4*a*c


if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(delta)) / (2*a)
    r2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")


# 1044


a, b = map(int, input().split())
if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


# 1049


a = input()
b = input()
c = input()


if a == 'vertebrado':
    if b == 'ave':
        print('aguia' if c == 'carnivoro' else 'pomba')
    else:
        print('homem' if c == 'onivoro' else 'vaca')
else:
    if b == 'inseto':
        print('pulga' if c == 'hematofago' else 'lagarta')
    else:
        print('sanguessuga' if c == 'hematofago' else 'minhoca')


# 1050


ddd = int(input())
ddd_dict = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}
print(ddd_dict.get(ddd, 'DDD nao cadastrado'))

# 2424


x, y = map(int, input().split())
if 0 < x < 9 and 0 < y < 9:
    print(1)
else:
    print(0)


# 2670


a1 = int(input())
a2 = int(input())
a3 = int(input())


tempo1 = a2 * 2 + a3 * 4
tempo2 = a1 * 2 + a3 * 2
tempo3 = a1 * 4 + a2 * 2


print(min(tempo1, tempo2, tempo3))

# 1059


for i in range(2, 101, 2):
    print(i)


# 1080

maior = 0
posicao = 0
for i in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posicao = i
print(maior)
print(posicao)


# 1094

n = int(input())
total = coelhos = ratos = sapos = 0




for _ in range(n):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    total += quantidade
    if tipo == 'C':
        coelhos += quantidade
    elif tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade


print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / total * 100:.2f} %")
print(f"Percentual de ratos: {ratos / total * 100:.2f} %")
print(f"Percentual de sapos: {sapos / total * 100:.2f} %")


# 1114


while True:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")


# 1116

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{x / y:.1f}")


# 1151


n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=' ' if i < n - 1 else '\n')
    a, b = b, a + b





