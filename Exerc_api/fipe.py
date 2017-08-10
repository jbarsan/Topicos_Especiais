#!/usr/bin/env python3

from argparse import ArgumentParser
import requests
import json

# TODO: Implementar o argparse para usar pela linha de comando
api_fipe = 'https://fipe-parallelum.rhcloud.com/api/v1'

# Listando todas as marcas cadastradas na FIPE
# https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas
# Entradas permitidas:
# carros, motos, caminhoes
def marcas(tipo):
    url = '{0}/{1}/marcas'.format(api_fipe, tipo)
    try:
        resposta = requests.get(url)
        resultado = resposta.json()
        retorno = []
        for k in resultado:
            texto = '{} --> {}'.format(k['nome'], k['codigo'])
            retorno.append(texto)
    except requests.exceptions.ConnectionError:
        texto = 'Erro de conexão, verifique se você está conectado.'
        return texto
    except:
        return 'Erro, procure o desenvolvedor.'
    return retorno


# Listando todos os modelos de uma marca
# https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas/59/modelos
def lista_modelos(tipo, cod_modelo):
    url = '{0}/{1}/marcas/{2}/modelos'.format(api_fipe, tipo, cod_modelo)
    try:
        resposta = requests.get(url)
        resultado = resposta.json()
        retorno = []
        for k in resultado.get('modelos'):
            texto = 'Nome: {0}   ||   Código: {1}'.format(k['nome'], k['codigo'])
            retorno.append(texto)
    except requests.exceptions.ConnectionError:
        return 'Erro de conexão, verifique se você está conectado.'
    except:
        return 'Erro, procure o desenvolvedor.'
    return retorno


# Listando todos os anos de um modelo
# https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas/59/modelos/5940/anos
def lista_anos(tipo, cod_modelo, codigo):
    url = '{0}/{1}/marcas/{2}/modelos/{3}/anos'.format(api_fipe, tipo, cod_modelo, codigo)
    try:
        resposta = requests.get(url)
        resultado = resposta.json()
        retorno = []
        for k in resultado:
            texto = 'Nome: {0}   ||   Código: {1}'.format(k['nome'], k['codigo'])
            retorno.append(texto)
    except requests.exceptions.ConnectionError:
        return 'Erro de conexão, verifique se você está conectado.'
    except:
        return 'Erro, procure o desenvolvedor.'
    return retorno

# Listando o valor do automóvel
# https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas/59/modelos/5940/anos/2014-3
def lista_valor(tipo, cod_modelo, codigo, ano):
    url = url = '{0}/{1}/marcas/{2}/modelos/{3}/anos/{4}'.format(api_fipe, tipo, cod_modelo, codigo, ano)
    try:
        resposta = requests.get(url)
        resultado = resposta.json()
        texto = '''
        Valor: {0}
        Marca: {1}
        Modelo: {2}
        Ano: {3}
        Combustível: {4}
        Cód. FIPE: {5}'''.format(resultado['Valor'],resultado['Marca'], resultado['Modelo'],
                         resultado['AnoModelo'], resultado['Combustivel'], resultado['CodigoFipe'])
    except requests.exceptions.ConnectionError:
        return 'Erro de conexão, verifique se você está conectado.'
    except:
        return 'Erro, procure o desenvolvedor.'
    return texto


def ajuda():
    texto = '''
    -h, --help = Exibe esta ajuda
    -t, --tipo = Exibe as marcas disponíveis na tabela FIPE. Opções aceitas 'carros', 'motos', 'caminhoes'
    -c, --cod_modelo = Exibe todos os modelos disponíveis da marca. Deve ser usado junto com -t, --tipo
    -C, --codigo = Exibe todos os modelos. Deve ser usado junto com -t e -c.
    -a, --ano = Exibe o ano do modelo especificado. Deve ser usado junto com -t, -c e -C.
    '''
    return texto

# Teste marcas()
''''
m = marcas('carros')
for i in m:
    print (i)
'''

# Teste lista_modelos()
''''
m = lista_modelos('carros', '17')
for i in m:
    print(m)
'''

# Teste lista_anos()
''''
m = lista_anos('carros', '17', '5238')
print(m)
'''


# Teste lista_valor()
m = lista_valor('carros', '17', '5238', '2011-1')
print(m)

