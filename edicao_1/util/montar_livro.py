#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
from urllib import urlopen

BASE='http://pensarpython.incubadora.fapesp.br/portal/livro/%s/quickdoc_rst'

#ARQS = ['apresentacao', 'prefacio']
ARQS = []
ARQS.extend(['capitulo_%02d'%i for i in range(1,21)])
ARQS.extend(['apendice_%s'%c for c in 'abcd'])


cont = '.. contents:: Topicos'

partes = [cont]

for arq in ARQS:
    print arq
    rst = file(arq+'.txt').read()
    rst = rst.replace(cont,'')
    partes.append(rst)

partes = '\n\n'.join(partes)
saida = file('livro-completo.txt','w')
saida.write(partes)
saida.close()


