#!/usr/bin/env python

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def yes(ques):
    from string import lower
    ans = lower(raw_input(ques))
    return (ans[0] == 'y')
              
def animal():
    # start with a singleton
    root = Tree("bird")

    # loop until the user quits
    while True:
        print
        if not yes("Are you thinking of an animal? "): break

        # walk the tree
        tree = root
        while tree.left != None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print "I rule!"
            continue

        # get new information
        prompt  = "What is the animal's name? "
        animal  = raw_input(prompt)
        prompt  = "What question would distinguish a %s from a %s? "
        question = raw_input(prompt % (animal,guess))

        # add new information to the tree
        tree.cargo = question
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % animal):
            tree.left =  Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left =  Tree(animal)
            tree.right = Tree(guess)
            
if __name__ == '__main__':
    animal()
