__author__ = 'Matko'


class PrijevodnaJedinica(object):

    def __init__(self,listaPrograma,pozicijaUprogramu):
        self.listaPrograma = listaPrograma
        self.pozicijaUprogramu = pozicijaUprogramu

    def nadiBrojRazmaka(self,pozicija):
        tmp = self.listaPrograma[pozicija]
        list(tmp)
        br = 0
        for i in range(len(tmp)):
            if tmp[i] == ' ':
                br += 1
            else:
                break
        return br


    def nadiDesnuStranu(self,pozicija):
        brojRazmaka = self.nadiBrojRazmaka(pozicija)




    def glavnaMetoda(self):

        #nalazi svoju desnu stranu preko matode koja nalazi desnu stranu
        #poznavajuci samo indekst u listi programa
        #tako ce se metoda nadiDesnuStranu moci koristit od strane svih objekata koji ju naslijede
        desnaStrana = self.nadiDesnuStranu(self.pozicijaUprogramu)



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

    #stvori inicijalni objekt
    prijevodna_jedinica = PrijevodnaJedinica(listaPrograma,0)
    rezultat = prijevodna_jedinica.glavnaMetoda()

    #je li doslo do pogreske
    if rezultat != 0:
        print rezultat







if __name__ == '__main__':
  main()
