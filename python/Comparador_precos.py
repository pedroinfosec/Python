import time

print("--------------------------------------------------------------")
print("                    seja bem - vindo                           ")
print("------------- --------------------------------------------------")

p1 = float(input("Digite preço:".upper()))
p2 = float(input("Digite preço:".upper()))
p3 = float(input("Digite preço222:".upper()))


def menor():
    if p1 < p2 and p1 < p3:
        return p1
    elif p2 < p1 and p2 < p3:
        return p2
    else:
        return p3

time.sleep(0.8)

print("Menor preço é:", menor())
