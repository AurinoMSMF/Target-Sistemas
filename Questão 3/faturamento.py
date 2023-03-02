import json
with open("dados.json") as dados:
    faturamentos = json.load(dados)

diasZerados =[]
diasNormais =[]
acimaDaMedia =[]
for i in faturamentos:
    indice=i['valor']
    if indice == 0.0:
        diasZerados.append(indice)
    elif indice>0.0:
        diasNormais.append(indice)

media = sum(diasNormais)/len(diasNormais)

for j in diasNormais:
    if j > media:
        acimaDaMedia.append(j)

menorValor = min(diasNormais)
maiorValor = max(diasNormais)
qtdDiasAcimaDaMedia = len(acimaDaMedia)

print("Este é o menor valor de faturamento ocorrido em um dia do mês: ", menorValor)
print("Este é o maior valor de faturamento ocorrido em um dia do mês: ", maiorValor)
print("Este é o número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", qtdDiasAcimaDaMedia)