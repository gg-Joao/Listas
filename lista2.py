nome = input()
print("Bem-vindo(a) ao Python,", nome.split()[0])


# --------- Exercicio 2 ----------

n1 = int(input())
n2 = int(input())
print("Média parcial =", (n1*2 + n2*3) // 5)


# --------- Exercicio 3 ----------


b = float(input())
h = float(input())
print("Área =", round(b*h, 2), "- Perímetro =", round(2*(b+h), 2), "- Diagonal =", round((b**2 + h**2)**0.5, 2))


# --------- Exercicio 4 ----------


f = input()
print(f[f.rfind(" ")+1:])
