turno = input("Digite o período que você estuda (M/V/N): ").upper()

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print("Boa tarde")
elif turno == 'N':
    print("Boa noite")
else:
    print("Tem certeza que digitou certo?")