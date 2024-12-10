from platypus import Platypus

if __name__ == '__main__':

    perry = Platypus("Perry", "platypus", "green", 0)
    perry.eat('salad')
    perry.sleep()
    #gives memory adress of this platypus instance
    print(str(perry))
