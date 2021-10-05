# Exercício 1: Em um contexto de orientação a objetos, como podemos
#  definir o que são mensagens e qual a sua importância?
    # R: Forma com que objetos interagem - chamando funções uns dos outros.

# Exercício 2: Para exercitar nossa capacidade de abstração, vamos modelar algumas
# partes de um software de geometria. Como poderíamos modelar um paralelepipedo retangular?

class Paralelepipedo_Retangular:
    def __init__(self, A, B, C ):
        self.A = A
        self.B = B
        self.C = C

    def calcula_area_base(self):
      print(self.A*self.B)
      
    def calcula_volume(self):
      print(self.A*self.B*self.C)
      
meu_bloco = Paralelepipedo_Retangular(1,2,3)
meu_bloco.calcula_area_base()
meu_bloco.calcula_volume()



