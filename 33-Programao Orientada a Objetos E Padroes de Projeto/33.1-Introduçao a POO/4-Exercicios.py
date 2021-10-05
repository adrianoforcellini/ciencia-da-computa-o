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
      base = self.A*self.B 
      print(base, 'cm²')

    def calcula_volume(self):
      volume = self.A*self.B*self.C
      print(volume, 'cm³')
      
meu_bloco = Paralelepipedo_Retangular(1,2,3)
meu_bloco.calcula_area_base()
meu_bloco.calcula_volume()

# Exercício 3: E como poderíamos definir um círculo? 
# Qual seu nome, atributos e comportamentos?

class Circulo:
  def __init__(self, r, PI):
    self.r = r
    self.PI = PI

  def perimetro(self):
    p = self.r * self.PI * 2
    print(p, 'cm')  

  def area(self):
    a = self.r ** 2 * self.PI
    print(a, 'cm²')

meu_circulo = Circulo(1,3.14)
meu_circulo.perimetro()   
meu_circulo.area()   

# Exercício 4: Vamos mudar um pouco nosso contexto para um sistema de vendas de 
# uma cafeteria. Como podemos abstrair um pedido composto por vários itens? 
# Qual seu nome, atributos e comportamentos?

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco


class Pedido:
    def __init__(self, cliente, itens_consumidos, forma_de_pagar):
        self.cliente = cliente
        self.itens_consumidos = itens_consumidos
        self.forma_de_pagar = forma_de_pagar

    def calcular_total(self):
        total = 0
        for item in self.itens_consumidos:
            total = total + item.preco

        return total

    def adicionar_item(self, item):
        self.itens_consumidos.append(item)


sanduba = Item('X-tudo', 16.9)
guarana = Item('Guarana', 5.9)
fritas = Item('Fritas crocantes', 10.9)

pedido_mesa_1 = Pedido('Cristiano', [], 'Cartao')
pedido_mesa_1.adicionar_item(fritas)
pedido_mesa_1.adicionar_item(sanduba)
pedido_mesa_1.adicionar_item(guarana)
pedido_mesa_1.adicionar_item(guarana)


print(pedido_mesa_1.calcular_total())


# Exercício 5: Notou que os pilares da orientação a objetos começam a 
# manifestar a medida que fizemos nossos exercícios de modelagem? Que tal
# agora então modelarmos uma televisão?

class TV:
  def __init__(self, modelo, cor, ligado, volume):
    self.modelo = modelo
    self.cor = cor
    self.ligado = ligado
    self.volume = volume

  def ligar_desligar(self):
    self.ligado = not self.ligado
    print(self.ligado)
  
  def aumentar_volume(self):
    if(self.volume < 33 and self.ligado == True):
     self.volume += 1
     print(self.volume)
  
  def abaixar_volume(self):
    if(self.volume > 0 and self.ligado == True):
      self.volume -= 1
      print(self.volume)      

minha_tv = TV('X-35', 'Azul-Perolado', True, 32 )
minha_tv.ligar_desligar()
minha_tv.aumentar_volume()
minha_tv.ligar_desligar()
minha_tv.aumentar_volume()  
minha_tv.abaixar_volume()  



