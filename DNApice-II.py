from random import *

limiteMaximoGene = 1000
tamanhoPopulacao = 10
tamanhoIndividuo = 5
valorTaxaMutacao = 5
valorTaxaSelecao = 80

def geracaoIndividuo():
    individuo = []
    for i in range(0, tamanhoIndividuo):
        individuo += [randint(1, limiteMaximoGene)]
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = []
    for (i, j) in zip(par1, par2):
        individuo += [max(i, j)]
    return individuo

def mutacaoGenetica(individuo):
    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoIndividuo - 1)
        individuo[i] = randint(1, limiteMaximoGene)
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo)
        if somatorio > adaptado:
            adaptado = somatorio
    return adaptado * (valorTaxaSelecao / 100)

populacao = [geracaoIndividuo() for i in range(0, tamanhoPopulacao)]
popnewage = []
for i in range(0, len(populacao) - 1):
    par1 = populacao[i]
    par2 = populacao[i+1]
    ind3 = reproducaoIndividuos(par1, par2)
    ind3 = mutacaoGenetica(ind3)
    if sum(ind3) >= avaliacaoPopulacao(populacao):
        popnewage += [ind3]

for individuo in populacao:
    print(individuo)
print()
for individuo in popnewage:
    print(individuo)
