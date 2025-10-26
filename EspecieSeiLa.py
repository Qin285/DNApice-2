from random import choice 
from random import randint
class Especie:
    def __init__(self, nome,sexo=choice(["M","F"])):
        self.nome = nome
        self.sexo = sexo
        self.resistencia_frio = randint(100,1000)
        self.velocidade_nado =  randint(100,1000)
        self.mergulho_eficiente = randint(100,1000)
        self.sobreviventes = 0

    def fitness(self, limites):
        if limites:
            return(self.resistencia_frio >= limites['resistencia_frio'] and
                    self.velocidade_nado >= limites['velocidade_nado'] and
                    self.mergulho_eficiente >= limites['mergulho_eficiente'])
        else:
            return (self.resistencia_frio + self.velocidade_nado + self.mergulho_eficiente)/3
        
    def apto_s_n(self):
        print(f"  🐧{self.nome} ({self.sexo})")
        print(f"  ❄ Resistência ao frio: {self.resistencia_frio}")
        print(f"  🌊 Velocidade de nado: {self.velocidade_nado}")
        print(f"  🤿 Eficiência de mergulho: {self.mergulho_eficiente}")
        print(f"  💪 Fitness: {'Apto' if self.sobreviventes else 'Não apto'}\n")
        
limites = {'resistencia_frio': 400, 'velocidade_nado': 300, 'mergulho_eficiente': 200}

pinguim = Especie("Pinguim-Real")
pinguim.sobreviventes= pinguim.fitness(limites)
pinguim.apto_s_n()
