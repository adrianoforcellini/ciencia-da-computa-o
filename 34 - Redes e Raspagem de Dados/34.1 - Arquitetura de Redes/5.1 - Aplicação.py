# Aplicação
# A camada de aplicação contém os protocolos responsáveis por dar 
# significado às informações, sendo a primeira camada passada para a mensagem.
# Como exemplos de protocolos dessa camada temos o SMTP 
# ( Simple Mail Transfer Protocol - Transmissão de e-mails),
# FTP ( File Transfer Protocol - Transferência de arquivos) 
# e o nosso velho amigo HTTP ( Hypertext Transfer Protocol - Comunicação WEB).
# Tomando como exemplo o HTTP, quando subimos um front-end e temos um servidor
# capaz de servir páginas web, esse processo é realizado utilizando HTTP.
# Ao subirmos o servidor, o mesmo ficará aguardando por um pedido,
# por requisições. Quando acessamos aquele serviço pelo navegador,
# por exemplo, o navegador está fazendo uma chamada HTTP ao servidor,
# ou seja: o pedido é feito seguindo os padrões desse protocolo, de modo
# que o servidor saberá como interpretá-lo, processá-lo e devolver a devida
# resposta. Essa resposta também seguirá as regras do protocolo, 
# de modo que o navegador ( client ) também saiba entender o que foi
# retornado e, além do conteúdo das páginas (o html , css e o js ),
# também são entregues na resposta outros dados do protocolo, como os headers .
# Dessa mesma forma, outros protocolos podem ser utilizados nesssa camada, 
# SMTP, FTP, DHCP, entre outros. Cada um terá suas regras e padrões de modo 
# que, ambos os lados, cliente e servidor, saibam interpretar as informações.
