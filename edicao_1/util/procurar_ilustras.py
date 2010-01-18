#!/usr/bin/env python

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

BASE = 'http://www.greenteapress.com/thinkpython/html/'

index = urlopen(BASE)

sopa = BeautifulSoup(index)

nomes = [link['href'] for link in sopa.findAll('a',href=True)]

for nome in nomes:
    sopa = BeautifulSoup(urlopen(BASE+nome))
    imgs = [link['src'] for link in sopa.findAll('img') if link['src'].startswith(u'illustrations/')]
    cap = nome[4:6]
    n = 1
    for img in imgs:
        print 'mv', img, img.replace(u'illustrations/',u'illustrations/%s_%02d_'%(cap,n))
        n += 1
