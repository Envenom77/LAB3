__author__ = 'Matko'


class PrijevodnaJedinica(object):

    def __init__(self,listaPrograma,pozicijaUprogramu):
        self.listaPrograma = listaPrograma
        self.pozicijaUprogramu = pozicijaUprogramu

    def nadiBrojRazmaka(self,lista,pozicija):
        tmp = lista[pozicija]
        list(tmp)
        br = 0
        for i in range(len(tmp)):
            if tmp[i] == ' ':
                br += 1
            else:
                break
        return br

    def nadiDesnuStranu(self,lista,pozicija):

        desnaStrana = []
        element = []
        indeks = []

        brojRazmaka = self.nadiBrojRazmaka(lista,pozicija)
        novaPozicija = pozicija + 1
        #while noviBrojRazmaka != brojRazmaka:
        while 1:
            #provjera kraja programa, jesmo li doli do kraja liste
            if novaPozicija < len(lista):
                noviBrojRazmaka = self.nadiBrojRazmaka(lista,novaPozicija)
            else:
                break

            #provjeri jesmo li nasli sve elemente desne strane
            if noviBrojRazmaka <= brojRazmaka:
                break

            #provjeri je li to trazeni element
            elif noviBrojRazmaka == brojRazmaka + 1:
                tmp =lista[novaPozicija]
                tmp = tmp.strip()
                element.append(tmp)
                indeks.append(novaPozicija)

            #pomakni poziciju
            novaPozicija += 1

        desnaStrana = zip(element,indeks)
        return desnaStrana

    def glavnaMetoda(self):

        #nalazi svoju desnu stranu preko matode koja nalazi desnu stranu
        #poznavajuci samo indeks u listi programa
        #tako ce se metoda nadiDesnuStranu moci koristit od strane svih objekata koji ju naslijede

        #desna strana dobija listu stvorenu od elemenata od dva clana, prvi je element, a drugi pozicija u listi
        desnaStrana = self.nadiDesnuStranu(self.listaPrograma,self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<vanjska_deklaracija>":
            vanjska_deklaracija = VanjskaDeklaracija(desnaStrana[0][1])
            rezultat = vanjska_deklaracija.glavnaMetoda()
            if rezultat != 0:
                return rezultat

        elif desnaStrana[0][0] == "<prijevodna_jedinica>":
            prijevodna_jedinica = PrijevodnaJedinica(self.listaPrograma,desnaStrana[0][1])
            rezultat = prijevodna_jedinica.glavnaMetoda()
            if rezultat != 0:
                return rezultat
            vanjska_deklaracija = VanjskaDeklaracija(desnaStrana[1][1])
            rezultat = vanjska_deklaracija.glavnaMetoda()
            if rezultat != 0:
                return rezultat
        else:
            return "ERROR - losa desna strana prijevodne jedinice"

        #ako sve u redu vrati 0
        return 0

class VanjskaDeklaracija(PrijevodnaJedinica):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        desnaStrana = super(VanjskaDeklaracija,self).nadiDesnuStranu(PrijevodnaJedinica.listaPrograma,self.pozicijaUprogramu)
        print desnaStrana

        return 0


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
        print "ERROR - nema prijevodne jedinice"

    #stvori inicijalni objekt
    prijevodna_jedinica = PrijevodnaJedinica(listaPrograma,0)
    rezultat = prijevodna_jedinica.glavnaMetoda()

    #je li doslo do pogreske, ako je 0 => sve u redu
    if rezultat != 0:
        print rezultat

if __name__ == '__main__':
  main()
