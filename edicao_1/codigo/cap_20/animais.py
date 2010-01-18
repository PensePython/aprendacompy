#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Arvore: 

    def __init__(self, carga, esquerdo=None, direito=None): 
        self.carga = carga 
        self.esquerdo = direito 
        self.direito = direito 

    def __str__(self): 
        return str(self.carga)

def animal() :
    # começar com um animal
    raiz = Arvore("baleia")
    # repetir até que o usuário encerre
    while 1 :
        print
        if not sim("Você está pensando em um animal? ") : break

        # percorrer a arvore
        arvore = raiz
        while arvore.esquerdo != None:
            perg = arvore.carga + "? "
            if sim(perg):
                arvore = arvore.direito()
            else:
                arvore = arvore.esquerdo
        
        # chutar
        chute = arvore.carga
        perg = "O animal que tens em mente é: " + chute + "? "
        if sim(perg) :
            print "Sei tudo sobre animais!"
            continue

        # obter novas informações
        perg  = "Em que animal você pensou? "
        animal  = raw_input(perg)
        perg  = "Que pergunta posso fazer para distinguir '%s' de '%s'? "
        question = raw_input(perg % (animal,chute))

        # add new information to the arvore
        arvore.carga = question
        perg = "If the animal were %s the answer would be? "
        if sim(perg % animal) :
            arvore.setLeft(Arvore(chute))
            arvore.setRight(Arvore(animal))
        else :
            arvore.setLeft(Arvore(animal))
            arvore.setRight(Arvore(chute))

def sim(perg): 
    resp = ''
    while not resp: 
        resp = raw_input(perg).lower() 
    return resp.startswith('s')
    
def nao(perg):
    return not sim(perg)
