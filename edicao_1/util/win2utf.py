#!/usr/bin/env python

from sys import argv

if len(argv) < 3:
    print 'Conversor de MS Windows codepage 1252 para UTF-8'
    print '  Modo de usar:'
    print '  %s <arquivo_iso_1> <arquivo_iso_2> ... <dir_saida>' % argv[0]
else:
    assert argv[-1] != '.'
    dirSai = argv[-1]
    if not dirSai.endswith('/'):
        dirSai += '/'
    for arq in argv[1:-1]:
        print dirSai+arq
        arq2 = file(dirSai+arq,'w')
        for lin in file(arq).readlines():
            uLin = lin.decode('cp1252')
            try:
                iLin = uLin.encode('utf-8')
            except UnicodeEncodeError, e:
                print e
                print repr(uLin)
                break
            arq2.write(iLin)
        arq2.close()
    

    
    
