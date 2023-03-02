n = int(input("Digite o número para verificar sua presença na sequência de fibonacci: "))
ultimo=1
penultimo=1

seq=[0]

if (n==1) or (n==2):
    seq.append(1)
else:
    contador=3
    while contador <= n:
        indice = ultimo + penultimo
        penultimo = ultimo
        ultimo = indice
        contador += 1
        seq.append(indice)
    print(seq)
    if n in seq:
        print('O numero faz parte da sequencia de fibonacci.')
    else:
        print('O numero não faz parte da sequencia de fibonacci.')