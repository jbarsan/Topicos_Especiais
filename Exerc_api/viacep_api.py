#!/usr/bin/env python3

import requests
import json

#TODO Implementar a opção de linha de comando
api_viacep = 'http://www.viacep.com.br/ws/'

def end_completo(cep):
    url = '{0}{1}/json'.format(api_viacep, cep)
    try:
        resposta = requests.get(url)
        resultado = resposta.json()
        
        if 'erro' in resultado.keys():
            texto = 'CEP INEXISTENTE'
        else:
            texto ='''
            CEP: {0}
            Logradouro: {1}
            Complemento: {2}
            Bairro: {3}
            Cidade: {4}
            UF: {5}
            Cód. IBGE: {6}
            '''.format(resultado['cep'],
                    resultado['logradouro'],
                    resultado['complemento'],
                    resultado['bairro'],
                    resultado['localidade'],
                    resultado['uf'],
                    resultado['ibge'])
    except requests.exceptions.ConnectionError:
        return 'Erro de conexão, verifique se você está conectado.'
    except:
        return 'Erro, procure o desenvolvedor.'
    return texto

# Teste para cep inexistente
#m = end_completo(64015000)
#print(m)

n = end_completo(64015470)
print(n)
