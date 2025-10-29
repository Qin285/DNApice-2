from random import choice 
from random import randint
import time,sys

def esc_maquina(texto, atraso=0.01):
    for letra in texto:
        sys.stdout.write(letra)  
        sys.stdout.flush()       
        time.sleep(atraso)       
    print() 

class Especie:
    cont_num = 1
    def __init__(self, nome, tamanhoCaracteristica=5):
        self.id = Especie.cont_num
        Especie.cont_num +=1
        self.nome = nome
        self.sexo = choice(["M","F"])
        self.tamanhoCaracteristica = tamanhoCaracteristica
        self.resistencia_frio = [randint(100, 1000) for _ in range(self.tamanhoCaracteristica)]
        self.velocidade_nado =   [randint(100, 1000) for _ in range(self.tamanhoCaracteristica)]
        self.mergulho_eficiente =  [randint(100, 1000) for _ in range(self.tamanhoCaracteristica)]
        self.geracao = 0

    def fitness(self, limites):
        resistencia_media = sum(self.resistencia_frio) / len(self.resistencia_frio)
        velocidade_media = sum(self.velocidade_nado) / len(self.velocidade_nado)
        mergulho_medio = sum(self.mergulho_eficiente) / len(self.mergulho_eficiente)

      
        if limites:
            return (resistencia_media >= limites['resistencia_frio'] and
                    velocidade_media >= limites['velocidade_nado'] and
                    mergulho_medio >= limites['mergulho_eficiente'])
        else:
            return (resistencia_media + velocidade_media + mergulho_medio) / 3
    def apto_s_n(self):
        esc_maquina(f"  🐧{self.nome} ({self.sexo})")
        esc_maquina(f"  ❄ Resistência ao frio: {self.resistencia_frio}")
        esc_maquina(f"  🌊 Velocidade de nado: {self.velocidade_nado}")
        esc_maquina(f"  🤿 Eficiência de mergulho: {self.mergulho_eficiente}")
        esc_maquina(f"  💪 Fitness: {'Apto' if self.geracao else 'Não apto'}\n")
        
limites = {'resistencia_frio': 400, 'velocidade_nado': 300, 'mergulho_eficiente': 200}

pinguim = Especie("Pinguim-Real")
pinguim.sobreviventes= pinguim.fitness(limites)
pinguim.apto_s_n()
