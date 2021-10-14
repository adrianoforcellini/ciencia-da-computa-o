# Pacotes
# Se uma rede de computadores conecta dois ou mais computadores de forma a 
# possibilitar a troca de mensagens, as primeiras perguntas que podem surgir são: quais mensagens são enviadas? quais informações estão contidas nestas mensagens? o que mais é enviado além da informação da aplicação? como é a estrutura da mensagem? como todos os dados são empacotados? Estas perguntas são respondidas com o conceito de pacotes .
# Para trafegar uma informação em uma rede, essa informação é convertida para
# binários e então dividida em diversos pedaços, e esses pedaços são os 
# chamados "pacotes" que são enviados pela rede. Os pacotes possuem diversos 
# dados, além da informação em si, como quem está enviando aquele pacote,
# qual o seu destino e indicações para que o destinatário saiba se alguma parte 
# da informação se perdeu no caminho e se é necessário solicitar um reenvio, 
# dentre outras funções.
# Mas há a pergunta: como devemos adicionar esse monte de informação para 
# enviar os pacotes? E como o outro lado irá saber entender essas informações? 
# Como o outro lado irá juntar cada pedacinho para formar uma coisa só?
# Para isso existem os protocolos .