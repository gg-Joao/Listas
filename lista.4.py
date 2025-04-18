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


