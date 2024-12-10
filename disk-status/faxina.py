#!/usr/bin/python


#--------------
# Fonte de pesquisa:
#
# Python list directory
# https://zetcode.com/python/listdirectory/
#
from pathlib import Path
import time
import datetime
from datetime import date

#------
#
# Variaveis de data
#

agora = datetime.datetime.now()
agora_ano = agora.year
agora_mes = agora.month
agora_dia = agora.day

dias_limite = 30
dias_passados = agora - datetime.timedelta(days=dias_limite)

path = Path('/home/wilson/processos/backup/logs')
###path = '/home/wilson/processos/backup/logs'
###for path in Path(path).iterdir():
###    print(path)

###for arquivo in path.glob('**/backup.sh.2021-08-17.00-05-01.log'):
for arquivo in path.glob('**/*'):
    print(arquivo)
    ###print(  arquivo.name, arquivo.suffix, time.ctime(arquivo.stat().st_ctime)    )  
    ###data_criacao_arquivo=time.ctime(arquivo.stat().st_ctime)
    ###print('data_criacao_arquivo:' + data_criacao_arquivo)
    ###print(time.ctime(dias_passados))
    ##print(time.ctime(arquivo.stat().st_ctime), arquivo.name)  
    ###print(arquivo.stat(), arquivo.name)
    criacao=datetime.datetime.fromtimestamp(arquivo.stat().st_ctime)
    criacao_ano = criacao.year
    criacao_mes = criacao.month
    criacao_dia = criacao.day

    print('criacao_ano:' + str(criacao_ano))
    print('criacao_mes:' + str(criacao_mes))
    print('criacao_dia:' + str(criacao_dia))

    print('agora        :' + str(agora))
    print('dias_passados:' + str(dias_passados))
    print('criacao      :' + str(criacao))

    dias_da_criacao = date(criacao_ano, criacao_mes, criacao_dia)
    dias_de_agora   = date(agora_ano, agora_mes, agora_dia)

    dias_diferenca = dias_de_agora - dias_da_criacao

    print('dias_diferenca:' + str(dias_diferenca.days))





