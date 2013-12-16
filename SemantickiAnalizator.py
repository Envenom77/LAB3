__author__ = 'Matko'

class PrijevodnaJedinica(object):

    def __init__(self):
        pass

    def glavnaMetoda(self):
        pass



def ucitajUlaz():
    ulaz = open("ulaz1.in","r")
    listaPrograma = ulaz.readlines()

    #makni LF
    for i in range(len(listaPrograma)):
        listaPrograma[i] = listaPrograma[i].rstrip()
    return listaPrograma

def main ():

    listaPrograma = ucitajUlaz()
    print listaPrograma

    if listaPrograma[0] != "<prijevodna_jedinica>":
        print "ERROR"

    #stvori početni objekt
    prijevodna_jedinica = PrijevodnaJedinica()
    rezultat = prijevodna_jedinica.glavnaMetoda()

    #je li došlo do greške
    if rezultat != 0:
        print rezultat







if __name__ == '__main__':
  main()
