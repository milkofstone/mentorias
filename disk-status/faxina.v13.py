#!/usr/bin/python
#--------------------------------------------------------------------------------#
#  __  __   _   _   _               __      _____   _                            #
# |  \/  | (_) | | | |             / _|    / ____| | |                           #
# | \  / |  _  | | | | __     ___ | |_    | (___   | |_    ___    _ __     ___   #
# | |\/| | | | | | | |/ /    / _ \|  _|    \___ \  | __|  / _ \  | '_ \   / _ \  #
# | |  | | | | | | |   <    | (_) | |      ____) | | |_  | (_) | | | | | |  __/  #
# |_|  |_| |_| |_| |_|\_\    \___/|_|     |_____/   \__|  \___/  |_| |_|  \___|  #
#                                                                                #
#--------------------------------------------------------------------------------#
#                                                                                #
#          MilkofStone Prospecção de Dados e Tecnologia Ltda                     #
#                                                                                #
#                         milkofstone.com                                        #
#                                                                                #
#--------------------------------------------------------------------------------#
# Versão:                                                                        #
#     1.0.0                                                                      #
#                                                                                #
# Infraestrutura:                                                                #
#     Python 3.8.10                                                              #
#                                                                                #
# Descrição:                                                                     #
#    Esse programa executa um GET solicitando as informações dos pedidos_bling na#
#  conta do bling.                                                               #
#                                                                                #
# Dependencias:                                                                  #
#     import sys                                                                 #
#        └── Nativo Python 3.8.10                                                #
#     import os                                                                  #
#         └── Nativo Python 3.8.10                                               #
#     import requests                                                            #
#         └── Nativo Python 3.8.10                                               #
#     import json                                                                #
#         └── Nativo Python 3.8.10                                               #
#     import logging                                                             #
#         └── Nativo Python 3.8.10                                               #
#     import datetime, timedelta                                                 #
#         └── Nativo Python 3.8.10                                               #
#     import gspread                                                             #
#         └── pip3 install gspread                                               #
#     from oauth2client.service_account import ServiceAccountCredentials         #
#         └── pip3 install oauth2client                                          #
#                                                                                #
#     [ARGV]:                                                                    #
#          [Sem argumentos]                                                      #
#                                                                                #
# Observaçoes de uso:                                                            #
#     Todas as vezes que o programa for executado o arquivo é reescrito.         #
#     Se a quantidade de pedidos passar de 10 mil, vai no for da linha 175 e tro #
# ca 100 para um número maior. Cada Página são 100 pedidos.                      #
#                                                                                #
# Execução:                                                                      #
#     /usr/bin/python3 [Programa]                                                #
#--------------------------------------------------------------------------------#
# Autor: Wilson Nunes - wilson@milkofstone.com                                   #
# Data criação: 29/11/2023                                                       #
#--------------------------------------------------------------------------------#


#--------------
# Fonte de pesquisa:
#
# Python list directory
# https://zetcode.com/python/listdirectory/
#
import os
from pathlib import Path
import time
import datetime
from datetime import date

import os
import sys

# ----------------------------------------------
#   Nome do programa
#
nome_programa = os.path.basename(sys.argv[0])

#------
# Nome do caminho a ser pesquisado

try:
    nome_do_caminho = sys.argv[1]
    print(f'nome_do_caminho:{nome_do_caminho}')
    
    nome_do_caminho_editado = nome_do_caminho.replace('\\', '\\\\')
    print(f'nome_do_caminho_editado:{nome_do_caminho_editado}')

except:
    print(f'Falta o nome do caminho')
    exit(9)




#------
#
# Variaveis de data
#

agora = datetime.datetime.now()
agora_ano = agora.year
agora_mes = agora.month
agora_dia = agora.day

dias_limite = 30

###path = Path('/home/wilson/processos')
###path = Path('/home/wilson')
###path = Path("C:\\milkofstone\\projetos\\util_arquivos_faxina")
path = Path(nome_do_caminho_editado)
###path = Path("")
###path = Path("\\\\fs\\ti\\TESTEREN")
print(f'path:{path}')
###\\fs\ti\TESTEREN

arquivo_saida_cabecalho = f'Tipo;Nome_full;nome_full_tam;Basename;basename_tam;Qtd_bytes;Idade_em_dias;Mensagem\n'

arquivo_saida = 'arquivo_saida.csv'
arquivo_saida_open = open(arquivo_saida, 'w', encoding='UTF-8')
###arquivo_saida_open = open(arquivo_saida, 'w')


arquivo_saida_open.write(arquivo_saida_cabecalho)


for nome_full in path.glob('**/*'):
    ###print(nome_full)

    if os.path.exists(nome_full):

        if os.path.isdir(nome_full):
            tipo = 'Diretorio'
        else:
            tipo = 'Arquivo'

        nome_basename = os.path.basename(nome_full)

        nome_full_tam = len(str(nome_full))
        nome_basename_tam = len(str(nome_basename))

        try:
            criacao=datetime.datetime.fromtimestamp(nome_full.stat().st_ctime)
            criacao_ano = criacao.year
            criacao_mes = criacao.month
            criacao_dia = criacao.day
            mensagem = 'OK'
            dias_da_criacao = date(criacao_ano, criacao_mes, criacao_dia)
            dias_de_agora   = date(agora_ano, agora_mes, agora_dia)

            dias_diferenca = dias_de_agora - dias_da_criacao

        except Exception as err:
            criacao_ano = 0
            criacao_mes = 0
            criacao_dia = 0
            mensagem = 'NOK' + f"Unexpected {err=}, {type(err)=}"

            dias_da_criacao = 0
            dias_de_agora   = 0

            dias_diferenca  = 0


        print_tipo = str(tipo)
        print_nome_full = str(nome_full)
        print_nome_full_tam = str(nome_full_tam)
        print_basename = str(nome_basename)
        print_basename_tam = str(nome_basename_tam)
        print_qtd_bytes = str(nome_full.stat().st_size)
        print_dias_diferenca_days = str(dias_diferenca.days)
        print_mensagem = mensagem

        
        arquivo_saida_linha = f'{print_tipo};{print_nome_full};{print_nome_full_tam};{print_basename};{print_basename_tam};{print_qtd_bytes};{print_dias_diferenca_days};{print_mensagem}'

        try:
        	arquivo_saida_open.write(str(arquivo_saida_linha + '\n'))    
        except Exception as e:
        	print(f'Falha:{e}')
        	print(f'Linha:{arquivo_saida_linha}')


arquivo_saida_open.close()



