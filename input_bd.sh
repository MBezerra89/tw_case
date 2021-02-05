#!/bin/bash

while read line
do
#Declaração das variaveis para colunas
date=`echo $line| awk '{print $1}'`

time=`echo $line| awk '{print $2}'|cut -c1-2`

user=`echo $line|awk -F, '{print $2}'`

seguidores=`echo $line|awk -F, '{print $3}'`

localidade1=`echo $line|awk -F, '{print $4}'`

hashtag=`echo $line|awk -F# '{print $NF}'`

lang="None"
# Foi necessario uma trataiva, para casos de retorno vazio.
if [[ -z $localidade1 ]]
then
localidade="None"
else
localidade=$localidade1
fi
## input BD
#### etapa de conexao com DB em testes, abre a conexao dentro ou fora do laço ... obs. testar desempenho !
##conexão com BD. 
# conectando...
echo "conectando ao BD"
conn = mysql -u root -h 172.17.0.3
echo "conexão com BD OK"

use tweets;
INSERT INTO dados (date,time,user,followers,country,lang,hashtag)VALUES ('$date','$time','$user','$seguidores','$localidade','$lang','$hashtag');

done < /root/scripts/logs/coleta_tweets_`date +%d-%m-%Y`.txt

