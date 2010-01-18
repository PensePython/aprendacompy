#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen

BASE='http://pensarpython.incubadora.fapesp.br/portal/livro/%s/quickdoc_rst'

ARQS = ['conteudo', 'apresentacao', 'prefacio']
ARQS.extend(['capitulo_%02d'%i for i in range(1,21)])
ARQS.extend(['apendice_%s'%c for c in 'abcd'])

for arq in ARQS:
    print arq
    rst = urlopen(BASE%arq).read()
    saida = file(arq+'.txt','w')
    saida.write(rst)
    saida.close()


