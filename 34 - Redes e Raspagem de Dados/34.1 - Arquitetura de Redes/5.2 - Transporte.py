# Transporte

# A camada de transporte, como o próprio nome indica, 
# a camada responsável pela transferência de dados entre diferentes máquinas
# (seja um servidor ou um computador pessoal). Os principais protocolos dessa
# camada são o TCP e o UDP .

# Os protocolos possuem diferentes aplicabilidades.
# Por exemplo, para criarmos um servidor para servir uma página web não 
# podemos ter perda de informações, caso contrário a página não chegará 
# por completo a quem pediu. Da mesma forma que, ao construirmos uma API, 
# temos que garantir que os dados enviados, como o conteúdo de um formulário 
# de cadastro, chegue até o servidor, assim como garantir que os dados 
# respondidos em uma consulta feita ao servidor , por exemplo, sejam entregues
# por inteiro ao cliente que fez essa solicitação. Nesses casos o TCP é o protocolo mais adequado.
# Por outro lado, ao assistirmos uma live ou jogarmos algum jogo online, 
# alguns dados podem ser perdidos, por exemplo, parte da transmissão do vídeo,
# de maneira que perceberemos apenas uma oscilação na transmissão. 
# Nesse caso, o UDP é mais indicado, já que com TCP, caso essa perda de 
# pacote ocorra, será necessário aguardar o reenvio para então ser dado 
# continuidade no processo. Além disso o UDP permitirá uma maior velocidade
# na transmissão e também que o conteúdo seja transmitido para diversos
# clientes ao mesmo tempo, permitindo que diversas pessoas assistam àquele
# conteúdo em tempo real.
