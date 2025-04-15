A = int(input())
B = int(input())
PROD = A * B
print(f"PROD = {PROD}")


# --------- 1005 ----------

a = float(input())
b = float(input())
media = (a * 3.5 + b * 7.5) / 11
print("MEDIA = {:.5f}".format(media))


# --------- 1011 ----------

R = int(input())
pi = 3.14159
volume = (4/3) * pi * R**3
print(f"VOLUME = {volume:.3f}")


# --------- 2416 ----------


L, D = map(int, input().split())
print(D % L)


# --------- 1015 ----------

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{distancia:.4f}")


# --------- 1930 ----------

a, b, c, d = map(int, input().split())
total = a + b + c + d - 3
print(total)



