from EspecieSeiLa import *
from random import *
import time,sys

limiteMaximoGene = 1000
tamanhoPopulacao = int(input("Insira o tamanho da população inicial: "))
tamanhoNovaPopulação = int(input("Insira o tamanho da nova população: "))
tamanhoCaracteristica = 5
valorTaxaMutacao = 5
valorTaxaSelecao = 5
cont_num = 0


def esc_maquina(texto, atraso=0.01):
    for letra in texto:
        sys.stdout.write(letra)  
        sys.stdout.flush()       
        time.sleep(atraso)       
    print() 

def gerarID():
    global cont_num
    cont_num += 1
    return cont_num

def geracaoIndividuo():
    individuo = Especie("Pinguim-Real")
    individuo.cont_num = gerarID() 
    individuo.geracao = 1  
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = Especie("Pinguim-Real")
    individuo.cont_num = gerarID() 
    individuo.geracao = max(par1.geracao, par2.geracao) + 1
    individuo.resistencia_frio = [max(a, b) for a, b in zip(par1.resistencia_frio, par2.resistencia_frio)]
    individuo.velocidade_nado = [max(a, b) for a, b in zip(par1.velocidade_nado, par2.velocidade_nado)]
    individuo.mergulho_eficiente = [max(a, b) for a, b in zip(par1.mergulho_eficiente, par2.mergulho_eficiente)]
    return individuo


def mutacaoGenetica(individuo):
    atr_mutado = choice(["resistencia_frio", "velocidade_nado", "mergulho_eficiente"])
    lista = getattr(individuo, atr_mutado)
    i = randint(0, len(lista) - 1)
    valor_antigo = lista[i]
    lista[i] = randint(100, 1000)
    valor_novo = lista[i]

    esc_maquina(f"🔄 Mutação em  {individuo.cont_num} - {individuo.nome} ({individuo.sexo}):")
    esc_maquina(f"  Atributo: {atr_mutado.replace('_', ' ').title()}")
    esc_maquina(f"  Gene {i}: {valor_antigo} → {valor_novo}\n")
    return individuo


def mutacaoPopulacao(populacao, tx_mutacao=0.15):
    qtd_mutar = max(1, int(len(populacao) * tx_mutacao)) 
    individuos_mutar = sample(populacao, qtd_mutar)

    esc_maquina(f"\n🔄 {qtd_mutar} indivíduos sofrerão mutação genética nesta geração:\n")
    for individuo in individuos_mutar:
        mutacaoGenetica(individuo)
def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo.resistencia_frio) + sum(individuo.velocidade_nado) + sum(individuo.mergulho_eficiente)
        if somatorio > adaptado:
            adaptado = somatorio
    return adaptado * (valorTaxaSelecao / 100)

populacao = [geracaoIndividuo() for _ in range(0, tamanhoPopulacao)]
popnewage = []
for i in range(0, len(populacao) - 1, 2):
    par1 = populacao[i]
    par2 = populacao[i+1] if i+1 < len(populacao) else populacao[0]
    ind3 = reproducaoIndividuos(par1, par2)
    ind3 = mutacaoGenetica(ind3)
    fitness_do_ind3 = sum(ind3.resistencia_frio) + sum(ind3.velocidade_nado) + sum(ind3.mergulho_eficiente)
    if fitness_do_ind3 >= avaliacaoPopulacao(populacao):
        popnewage.append(ind3)
    if len(popnewage) >= tamanhoNovaPopulação:
        break

time.sleep(1)
esc_maquina("--- População Inicial ---")
for individuo in populacao:
    esc_maquina(f"{individuo.cont_num} - {individuo.nome} - {individuo.sexo} - Geração: {individuo.geracao}")
    esc_maquina(f"Resistência ao frio: {individuo.resistencia_frio}")
    esc_maquina(f"Velocidade de nado: {individuo.velocidade_nado}")
    esc_maquina(f"Eficiência de mergulho: {individuo.mergulho_eficiente}")
    individuo.apto_s_n()
print()

time.sleep(1)
esc_maquina("--- Nova População ---")
for individuo in popnewage:
    esc_maquina(f" {individuo.cont_num} - {individuo.nome} - {individuo.sexo} - Geração: {individuo.geracao}")
    esc_maquina(f"Resistência ao frio: {individuo.resistencia_frio}")
    esc_maquina(f"Velocidade de nado: {individuo.velocidade_nado}")
    esc_maquina(f"Eficiência de mergulho: {individuo.mergulho_eficiente}")
    individuo.apto_s_n()
print()

mais_apto = None
max_fitness = 0

for ind in popnewage:
    fitness_atual = sum(ind.resistencia_frio) + sum(ind.velocidade_nado) + sum (ind.mergulho_eficiente)
    if fitness_atual > max_fitness:
        max_fitness = fitness_atual
        mais_apto = ind

time.sleep(1)
esc_maquina(f"\n--- Indivíduo Mais Apto (Fitness: {max_fitness}) ---")

esc_maquina(f"Resistência: {mais_apto.resistencia_frio}, Nado: {mais_apto.velocidade_nado}, Mergulho: {mais_apto.mergulho_eficiente}\n")

time.sleep(1)
esc_maquina("--- Comparação da População ---")
for individuo in popnewage:
    esc_maquina(f"Indivíduo (Geração {individuo.geracao}):")
    #pra gnt comparar a resistência:
    if sum(individuo.resistencia_frio) >= sum(mais_apto.resistencia_frio):
        esc_maquina(f"  ❄ Resistência: {individuo.resistencia_frio} \033[1;32m (Ganha/Empata)\033[0m")
    else:
        esc_maquina(f"  ❄ Resistência: {individuo.resistencia_frio} \033[1;31m(Perde)\033[0m")
    #pra comparar nado:
    if sum(individuo.velocidade_nado) >= sum(mais_apto.velocidade_nado):
        esc_maquina(f"  🌊 Nado: {individuo.velocidade_nado} \033[1;32m (Ganha/Empata)\033[0m")
    else:
        esc_maquina(f"  🌊 Nado: {individuo.velocidade_nado} \033[1;31m(Perde)\033[0m")
    #pra comparar mergulho:
    if sum(individuo.mergulho_eficiente) >= sum(mais_apto.mergulho_eficiente):
        esc_maquina(f"  🤿 Mergulho: {individuo.mergulho_eficiente} \033[1;32m (Ganha/Empata)\033[0m")
    else:
        esc_maquina(f"  🤿 Mergulho: {individuo.mergulho_eficiente} \033[1;31m(Perde)\033[0m")
    print()
