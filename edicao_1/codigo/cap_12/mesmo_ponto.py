#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa subsidia a discussão sobre o sentido de "mesmo" (sameness)
da seção 12.4 da 1a-edição (p.129-131)
"""

class Ponto:
    def igualdade(self, p2):
        return self.x==p2.x and self.y==p2.y

p1 = Ponto()
p1.x = 3
p1.y = 4
p2 = Ponto()
p2.x = 3
p2.y = 4

print 'p1 == p2 ->', repr(p1 == p2)
print 'p1 is p2 ->', repr(p1 is p2)

# note que a semântica default não é essa
l1 = [1,2,3]
l2 = [1,2,3]
print 'l1 == l2 ->', repr(l1 == l2)
print 'l1 is l2 ->', repr(l1 is l2)

# agora sobrecarregamos o operador == para fazer a coisa certa
Ponto.__eq__ = Ponto.igualdade
print 'p1 == p2 ->', repr(p1 == p2)
print 'p1 is p2 ->', repr(p1 is p2)




