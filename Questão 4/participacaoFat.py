sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

representacoes=[]
representacoes.append(sp)
representacoes.append(rj)
representacoes.append(mg)
representacoes.append(es)
representacoes.append(outros)

totalRepresentacao= sum(representacoes)

def representacao (estado):
    representacaoIndividual = (estado * 100)/totalRepresentacao
    return representacaoIndividual

representacaoSp=representacao(sp)
representacaoRj=representacao(rj)
representacaoMg=representacao(mg)
representacaoEs= representacao(es)
representacaoOutros =representacao(outros)

print(f"A representação do estado de São Paulo no faturamento é de {representacaoSp:.2f}%")
print(f"A representação do estado do Rio de Janeiro no faturamento é de {representacaoRj:.2f}%")
print(f"A representação do estado de Minas Gerais no faturamento é de {representacaoMg:.2f}%")
print(f"A representação do estado do Espírito Santo no faturamento é de {representacaoEs:.2f}%")
print(f"A representação de outros estados no faturamento é de {representacaoOutros:.2f}%")
