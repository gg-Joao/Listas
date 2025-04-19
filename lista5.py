# 1

def maior(x, y):
    return x if x > y else y

a = int(input())
b = int(input())
print(maior(a, b))

# 2

def maior(x, y, z):
    return max(x, y, z)

a = int(input())
b = int(input())
c = int(input())
print(maior(a, b, c))

# 3

def iniciais(nome):
    return ''.join([parte[0].upper() for parte in nome.split()])

nome = input()
print(iniciais(nome))

# 4

def aprovado(n1, n2):
    media = (n1 * 2 + n2 * 3) / 5
    return media >= 60

n1 = int(input())
n2 = int(input())
print("Aprovado" if aprovado(n1, n2) else "Prova final")

# 5

def formatar_nome(nome):
    return nome.title()

nome = input()
print(formatar_nome(nome))
