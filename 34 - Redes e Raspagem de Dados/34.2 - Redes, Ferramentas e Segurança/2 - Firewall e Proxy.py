#DoS / DDoS
# Imagine que temos uma aplicação publicada. 
# Estamos utilizando as melhores práticas de desenvolvimento e também
# já estamos utilizando um certificado e o protocolo HTTPS.
# Nosso site está hospedado em um servidor, um computador com memória,
# processador, disco, enfim. Esses recursos, como sabemos, são limitados,
# como com qualquer máquina. Nossa aplicação, porém, recebe relativamente poucos
# acessos por dia e esses recursos são o suficiente para ela funcionar normalmente.
# Entretanto, nossa aplicação está publicada na internet e, dessa forma,
# exposta ao mundo inteiro. Então vamos imaginar que mais uma vez uma pessoa
# mal intencionada resolva "bombardear" nossa aplicação com diversos acessos
# simultâneos. Isso pode ser feito de diversas maneiras, e esse ataque é 
# chamado de DDoS ( Distributed Denial of Service ), ou ataque distribuído 
# de negação de serviço. Esse ataque tem como objetivo tirar o serviço do ar,
# tornando-o temporariamente indisponível.

# Brute Force
# Um outro ataque ao qual podemos estar vulneráveis é o conhecido como 
# "brute force", ou ataque de "força bruta", onde indivíduos, robôs ou 
# scripts maliciosos que tentam diversas combinações de usuário e senha, 
# por exemplo, com o objetivo de encontrar as corretas e acessar indevidamente
# um sistema. Existem diversos métodos de tornar esse ataque mais efetivo.
# Por exemplo, o uso de listas de palavras com senhas e usuários comuns, 
# tal como usuário "admin" e senha "123456" (por incrível que pareça as 
# pessoas utilizam esse tipo de senha fraca até hoje).
# Além de sempre utilizarmos senhas fortes e outros métodos de segurança 
# pessoais com os nossos logins (uso de segundo fator de autenticação e outros
# cuidados com as senhas), podemos também configurar camadas de proteção 
# extra em nossos servidores para mitigar essas vulnerabilidades.
# Agora que já entendemos um pouco dos riscos e a importância da nossa atenção
# para isso, vamos ver como podemos proteger nossa aplicação contra esses 
# ataques. É aqui que entram os firewalls!

# O que são firewalls?
# Firewall, em uma tradução mais livre, significa muro de fogo, ou porta 
# corta fogo, aquelas portas "de escada", utilizadas para evitar a passagem de
# fogo em caso de incêndios. De maneira semelhante, os firewalls são 
# responsáveis por impedir ou permitir a passagem de determinados tráfegos em 
# uma rede, seja de entrada ou saída.

# Iptables e Netfilter
# Na maioria dos sistemas operacionais existem subsistemas de filtragem de
# pacotes e ferramentas para gerenciamento de firewall. O sistema padrão para
# filtragem de pacotes do linux é o Netfilter . Existe uma ferramenta 
# utilizada para configurar o Netfilter chamada Iptables , que opera nas 
# camadas 2 e 3 do modelo OSI. O Iptables é, então, o firewall padrão do 
# linux e está presente na maioria das distros.

# Como funciona o Iptables?
# Ele compara o tráfego de rede que recebe ou envia com um conjunto de regras
# pré estabelecidas. Essas regras definem as características que um pacote deve
# possuir e a ação que deve ser tomada para esse tipo de pacote. Podemos criar 
# regras por protocolo, porta de origem/destino, endereço IP, entre outros. 
# Quando ocorre a correspondência de um pacote a uma característica estabelecida
# em uma regra é então tomada a ação, que pode ser, por exemplo, se aquele 
# pacote será aceito, rejeitado ou registrado em um arquivo de log.
# Como diz o próprio nome, a arquitetura do Iptables é formada por "tabelas".
# Essas tabelas também são conhecidas como cadeias e cada uma possui tipos 
# de regras específicas. Por exemplo, a cadeia "filter" que possui todas 
# políticas (regras) responsáveis por controlar o tráfego que entra ou sai do
# computador.

# Fail2ban
# O fail2ban é um IPS 
# ( Intrusion Prevention System - Sistema de Prevenção de intrusos). 
# Essa ferramenta, de maneira simples, monitora os logs da rede e, de maneira
# proativa, ao detectar comportamento suspeito, como diversas requisições de
# um mesmo IP ou diversas tentativas de login SSH, ele criar regras noiptables,
# de modo a rejeitar aquele endereço de IP específico por determinado tempo.