from EspecieSeiLa import *
from random import *

limiteMaximoGene = 1000
tamanhoPopulacao = int(input("Insira o tamanho da população inicial: "))
tamanhoNovaPopulação = int(input("Insira o tamanho da nova população: "))
tamanhoCaracteristica1 = 5
valorTaxaMutacao = 5
valorTaxaSelecao = 5

def geracaoIndividuo():
    # Os valores aleatórios (100 a 1000) já tão sendo definidos dentro da classe Especie
    individuo = Especie("Pinguim-Real")
    individuo.geracao = 1  
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = Especie("Pinguim-Real", choice(["M","F"]))
    individuo.geracao = max(par1.geracao, par2.geracao) + 1
    individuo.resistencia_frio = max(par1.resistencia_frio, par2.resistencia_frio)
    individuo.velocidade_nado = max(par1.velocidade_nado, par2.velocidade_nado)
    individuo.mergulho_eficiente = max(par1.mergulho_eficiente, par2.mergulho_eficiente)
    return individuo

def mutacaoGenetica(individuo):
    if randint(1, 100) <= valorTaxaMutacao:
        atributo_mutado = choice(["resistencia_frio", "velocidade_nado", "mergulho_eficiente"])
        novo_valor = randint(1, limiteMaximoGene)
        if atributo_mutado == "resistencia_frio":
            individuo.resistencia_frio = novo_valor
        elif atributo_mutado == "velocidade_nado":
            individuo.velocidade_nado = novo_valor
        else: 
            individuo.mergulho_eficiente = novo_valor
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = individuo.resistencia_frio + individuo.velocidade_nado + individuo.mergulho_eficiente
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
    fitness_do_ind3 = ind3.resistencia_frio + ind3.velocidade_nado + ind3.mergulho_eficiente
    if fitness_do_ind3 >= avaliacaoPopulacao(populacao):
        popnewage.append(ind3)
    if len(popnewage) >= tamanhoNovaPopulação:
        break

for individuo in populacao:
    print(f"{individuo.nome} - {individuo.sexo} - Geração: {individuo.geracao}")
    print(f"Resistência ao frio: {individuo.resistencia_frio}")
    print(f"Velocidade de nado: {individuo.velocidade_nado}")
    print(f"Eficiência de mergulho: {individuo.mergulho_eficiente}")
print()
for individuo in popnewage:
    print(f"{individuo.nome} - {individuo.sexo} - Geração: {individuo.geracao}")
    print(f"Resistência ao frio: {individuo.resistencia_frio}")
    print(f"Velocidade de nado: {individuo.velocidade_nado}")
    print(f"Eficiência de mergulho: {individuo.mergulho_eficiente}")
print()

mais_apto = None
max_fitness = 0

for ind in popnewage:
    fitness_atual = ind.resistencia_frio + ind.velocidade_nado + ind.mergulho_eficiente
    if fitness_atual > max_fitness:
        max_fitness = fitness_atual
        mais_apto = ind

print(f"\n--- Indivíduo Mais Apto (Fitness: {max_fitness}) ---")
print(f"Resistência: {mais_apto.resistencia_frio}, Nado: {mais_apto.velocidade_nado}, Mergulho: {mais_apto.mergulho_eficiente}\n")

print("--- Comparação da População ---")
for individuo in popnewage:
    print(f"Indivíduo (Geração {individuo.geracao}):")
    #pra gnt comparar a resistência:
    if individuo.resistencia_frio >= mais_apto.resistencia_frio:
        print(f"  ❄ Resistência: {individuo.resistencia_frio} (Ganha/Empata)")
    else:
        print(f"  ❄ Resistência: {individuo.resistencia_frio} (Perde)")
    #pra comparar nado:
    if individuo.velocidade_nado >= mais_apto.velocidade_nado:
        print(f"  🌊 Nado: {individuo.velocidade_nado} (Ganha/Empata)")
    else:
        print(f"  🌊 Nado: {individuo.velocidade_nado} (Perde)")
    #pra comparar mergulho:
    if individuo.mergulho_eficiente >= mais_apto.mergulho_eficiente:
        print(f"  🤿 Mergulho: {individuo.mergulho_eficiente} (Ganha/Empata)")
    else:
        print(f"  🤿 Mergulho: {individuo.mergulho_eficiente} (Perde)")
    print()
