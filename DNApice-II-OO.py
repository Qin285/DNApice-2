from EspecieSeiLa import *
from random import *

limiteMaximoGene = 1000
tamanhoPopulacao = 10
tamanhoCaracteristica1 = 5
valorTaxaMutacao = 5
valorTaxaSelecao = 80

def geracaoIndividuo():
    individuo = Especie("Sein Lásus", choice(["M","F"]))
    caracteristica = []
    for i in range(0, tamanhoCaracteristica1):
        caracteristica += [randint(1, limiteMaximoGene)]
    individuo.caracteristica1 = caracteristica
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = Especie("Su Lú", choice(["M","F"]))
    caracteristica = []
    for (i, j) in zip(par1.caracteristica1, par2.caracteristica1):
        caracteristica += [max(i, j)]
    individuo.caracteristica1 = caracteristica
    return individuo

def mutacaoGenetica(individuo):
    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica1 - 1)
        individuo.caracteristica1[i] = randint(1, limiteMaximoGene)
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo.caracteristica1)
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
    if sum(ind3.caracteristica1) >= avaliacaoPopulacao(populacao):
        popnewage += [ind3]

for individuo in populacao:
    print(f"{individuo.nome} - {individuo.sexo}")
    print(f"Característica 1: {individuo.caracteristica1}")
print()
for individuo in popnewage:
    print(f"{individuo.nome} - {individuo.sexo}")
    print(f"Característica 1: {individuo.caracteristica1}")
