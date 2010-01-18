#!/usr/bin/env python

''' colocar titulos e remover links de navegacao '''

def lerNomesTitulos():
    nomes = []
    titulos = {}
    for lin in file('1ed-titulos-caps.txt').readlines():
        try:
            nome, titulo = lin.strip().split('\t')
        except ValueError:
            continue
        nome = nome.strip()
        nomes.append(nome)
        titulos[nome] = titulo.strip()
    return nomes, titulos

nomes, titulos = lerNomesTitulos()

for nome in nomes:
    entrada = file('iso/%s.txt' % nome)
    linhas = entrada.readlines()
    entrada.close()
    for i in reversed(range(len(linhas))):
        if linhas[i].strip().startswith('<< `anterior'):
            linhas[i] = ''
            break
    rst = ''.join(linhas)
    rst = rst.strip()
    titulo = titulos[nome].decode('utf-8').encode('iso-8859-1')
    decoracao = '=' * len(titulo) + '\n'
    cabecalho = decoracao + titulo + '\n' + decoracao + '\n'
    rst = cabecalho + rst + '\n'
    saida = file('iso2/%s.txt' % nome,'w')
    saida.write(rst)
    saida.close()
