#!/usr/bin/env python

from sys import argv

conversoes = [
    (u'\u2018',u"'"),(u'\u2019',u"'"), # aspas simples
    (u'\u201c',u'"'),(u'\u201d',u'"'), # aspas duplas
    (u'\u2013', u'--'), # travessao
    (u'\u2026', u'...'), # ellipsis
    (u'\ufeff', u''), # BOM (byte order mark)
]

if len(argv) != 3:
    print 'Conversor de UTF-8 para ISO-8859-1'
    print '  Modo de usar:'
    print '    %s <arquivo_UTF_8> <arquivo_ISO_8859_1>' % argv[0]
else:
    assert argv[1]!=argv[2]
    arq2 = file(argv[2],'w')
    for lin in file(argv[1]).readlines():
        uLin = lin.decode('utf-8')
        try:
            iLin = uLin.encode('iso8859-1')
        except UnicodeEncodeError, e:
            for gremlin, seq in conversoes:
                uLin = uLin.replace(gremlin, seq)
            try:
                iLin = uLin.encode('iso8859-1')
            except UnicodeEncodeError, e:
                print e
                print repr(uLin)
                break
        arq2.write(iLin)
    arq2.close()
    

    
    
