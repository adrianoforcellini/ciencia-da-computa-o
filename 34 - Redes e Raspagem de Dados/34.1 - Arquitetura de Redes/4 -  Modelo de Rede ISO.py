# Modelo de Rede
# Existem diversos protocolos, cada um responsável por definir as regras 
# para um objetivo específico. Por exemplo, temos protocolos que definem
# como o dado será trafegado, outros para definir como traduzir os dados
# recebidos no pacote.
# Essa separação é feita para permitir a modularização, de modo que cada 
# protocolo defina regras específicas para a parte pela qual ele é responsável
# e para que seja possível utilizar combinações de protocolos de acordo com a
# nossa necessidade.
# Dividimos então os protocolos em grupos, agrupando cada tipo no que chamamos 
# de camadas. Por exemplo, precisamos de uma camada para identificar quem está
# enviando a informação e pra quem ela se destina, precisamos de outra camada
# para traduzir os dados a serem trafegados, etc.
# Um conjunto dessas camadas forma o que chamamos de modelo, que basicamente
# define quais as camadas necessárias para a montagem de um pacote.

# Modelo ISO/OSI
# O modelo ISO/OSI (em inglês Open Systems Interconnection ), 
# foi lançado com o objetivo de ser um padrão entre os diversos dispositivos 
# de comunicação. Esse modelo divide as redes de computadores em 7 camadas:
# 1. Física: Estabelece a comunicação entre os dispositivos no sentido físico.
#    Responsável pelo cabeamento, pelas características elétricas como tensão,
#    ópticas (quando se der por meio óptico) ou eletromagnéticas em uma rede sem 
#    fio. Tudo isso garantindo que ocorra a transmissão dos dados pelos meios 
#    físicos (hardware), sem perder 0 s e 1 s.

# 2. Enlace: Também chamada de "link de dados", essa camada é responsável
#    pela detecção e eventualmente pela correção de erros que tenham ocorrido 
#    no nível físico. Ela também realiza o controle do fluxo da transmissão 
#    entre um dispositivo e outro.

# 3. Rede: Responsável pelo endereçamento dos dispositivos na rede, assim como pela 
#    rota (caminho) que os pacotes deverão percorrer para chegarem da origem até destino.

# 4. Transporte: Responsável pela detecção e correção de erros que tenham ocorrido nas
#    camadas anteriores, assim como pela ordenação, garantindo que os dados saídos da
#    origem sejam os mesmos no destino. Além disso, ela define a conexão que será usada 
#    e como estabelecê-la, assim como controla o fluxo e congestionamento de dados.

# 5. Sessão: Responsável pela comunicação entre dois processos que estão em máquinas
#    diferentes, controlando o status, definindo quando deve começar, terminar ou  
#    reiniciar a comunicação entre origem e destino.

# 6. Apresentação: Responsável pela conversão entre os formatos de caracteres para que
#    possam ser utilizados na transmissão, também responsável pela compressão e 
#    criptografia desses dados.

# 7. Aplicação: Essa camada é responsável pelo controle da sintaxe e da semântica
#    da mensagem, traduzindo de fato as informações trafegadas.