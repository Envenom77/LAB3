__author__ = 'Matko'

from itertools import repeat
import sys


listaPrograma = []

#tablicaFunkcija je dictionari oblika: IDN: [0/1,povratna vrijednosti(void,int,char), parametri], gdje je IDN ime funkcije, prvi clan vrijednosti
#je oznaka je li DEFINIRANA, a drugi clan je tip povratne vrijednosti funkcije, a treci clan su parametri, liste tipova_imena_nizova
tablicaFunkcija = {}

def nadiBrojRazmaka(pozicija):
    global listaPrograma
    tmp = listaPrograma[pozicija]
    list(tmp)
    br = 0
    for i in range(len(tmp)):
        if tmp[i] == ' ':
            br += 1
        else:
            break
    return br

def nadiDesnuStranu(pozicija):
    global listaPrograma
    desnaStrana = []
    element = []
    indeks = []

    brojRazmaka = nadiBrojRazmaka(pozicija)
    novaPozicija = pozicija + 1
    #while noviBrojRazmaka != brojRazmaka:
    while 1:
        #provjera kraja programa, jesmo li doli do kraja liste
        if novaPozicija < len(listaPrograma):
            noviBrojRazmaka = nadiBrojRazmaka(novaPozicija)
        else:
            break

        #provjeri jesmo li nasli sve elemente desne strane
        if noviBrojRazmaka <= brojRazmaka:
            break

        #provjeri je li to trazeni element
        elif noviBrojRazmaka == brojRazmaka + 1:
            tmp = listaPrograma[novaPozicija]
            tmp = tmp.strip()
            element.append(tmp)
            indeks.append(novaPozicija)

        #pomakni poziciju
        novaPozicija += 1

    desnaStrana = zip(element, indeks)
    return desnaStrana

class PrijevodnaJedinica(object):

    def __init__(self, pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        #nalazi svoju desnu stranu preko matode koja nalazi desnu stranu
        #poznavajuci samo indeks u listi programa
        #tako ce se metoda nadiDesnuStranu moci koristit od strane svih objekata koji ju naslijede

        #desna strana dobija listu stvorenu od elemenata od dva clana, prvi je element, a drugi pozicija u listi
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<vanjska_deklaracija>":
            vanjska_deklaracija = VanjskaDeklaracija(desnaStrana[0][1])
            rezultat = vanjska_deklaracija.glavnaMetoda()
            if rezultat != 0:
                return rezultat

        elif desnaStrana[0][0] == "<prijevodna_jedinica>":
            prijevodna_jedinica = PrijevodnaJedinica(desnaStrana[0][1])
            rezultat = prijevodna_jedinica.glavnaMetoda()
            if rezultat != 0:
                return rezultat
            vanjska_deklaracija = VanjskaDeklaracija(desnaStrana[1][1])
            rezultat = vanjska_deklaracija.glavnaMetoda()
            if rezultat != 0:
                return rezultat

        #ako sve u redu vrati 0
        return 0

class VanjskaDeklaracija(PrijevodnaJedinica):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<definicija_funkcije>":
            definicija_funkcije = DefinicijaFunkcije(desnaStrana[0][1])
            rezultat = definicija_funkcije.glavnaMetoda()
            if rezultat != 0:
                return rezultat
        elif desnaStrana[0][0] == "<deklaracija>":
            deklaracija = Deklaracija(desnaStrana[0][1])
            rezultat = deklaracija.glavnaMetoda()
            if rezultat != 0:
                return rezultat

        return 0

class DefinicijaFunkcije(VanjskaDeklaracija):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        global tablicaFunkcija
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        #print desnaStrana
        if desnaStrana[2][0] == "<lista_parametara>":
            ime_tipa = ImeTipa(desnaStrana[0][1])
            tip = ime_tipa.glavnaMetoda()
            #print tip
            if tip[0][1] == 1:
                return "ERROR - ne smije biti konstanta"

            #izluci IDN
            idn = desnaStrana[1][0]
            idn = list(idn)
            for i in reversed(range(len(idn))):
                if idn[i] == ' ':
                    del idn[:i+1]
                    break
            idn = ''.join(idn)

            #pogledaj postoji li vec definicija f-je u globalnom djelokrugu, ako da ispisi gresku
            #je li deklarirana
            if idn in tablicaFunkcija:
                #je li definirana
                if tablicaFunkcija[idn][0] == 1:
                    return "ERROR - redefinicija funkcije"

            lista_parametara = ListaParametara(desnaStrana[2][1])
            tipovi_imena = lista_parametara.glavnaMetoda()
            #jos je dodatno tu je li niz
            #[[tip,ime,niz],[tip,ime,niz]...]

            #definicija
            tablicaFunkcija[idn][0] = 1
            #povratni tip
            tablicaFunkcija[idn][1] = tip[0][0]
            #parametri - tip, ime, niz - da/ne
            tablicaFunkcija[idn][2] = tipovi_imena

            #tu ide jos koda

        else:
            ime_tipa = ImeTipa(desnaStrana[0][1])
            tip = ime_tipa.glavnaMetoda()
            if tip[0][1] == 1:
                return "ERROR - ne smije biti konstanta"

            #izluci IDN
            idn = desnaStrana[1][0]
            idn = list(idn)
            for i in reversed(range(len(idn))):
                if idn[i] == ' ':
                    del idn[:i+1]
                    break
            idn = ''.join(idn)

            #pogledaj postoji li vec definicija f-je u globalnom djelokrugu, ako da ispisi gresku
            #je li deklarirana
            if idn in tablicaFunkcija:
                #je li definirana
                if tablicaFunkcija[idn][0] == 1:
                    return "ERROR - redefinicija funkcije"

            #zatim pogledaj postoji li vec deklaracija f-je te je li povratni tip isti
            #postoji li, odnosno ako postoji sigurno je deklarirana
            if idn in tablicaFunkcija:
                #je li tip isti
                if tablicaFunkcija[idn][1] != tip[0][0]:
                    return "ERROR - tip vec deklarirane funkcije niji isti"

            #zabiljezi definiciju i deklaraciju funkcije
            zabiljeska = []
            zabiljeska.append(1)
            zabiljeska.append(tip[0][0])
            tablicaFunkcija[idn] = zabiljeska

            slozena_naredba = SlozenaNaredba(desnaStrana[5][1])
            rez = slozena_naredba.glavnaMetoda()

            return 0

        return 0

class Deklaracija(VanjskaDeklaracija):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class ImeTipa(DefinicijaFunkcije):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<specifikator_tipa>":
            specifikator_tipa = SpecifikatorTipa(desnaStrana[0][1])
            tip = specifikator_tipa.glavnaMetoda()

            if tip != "void" and tip != "char" and tip != "int":
                return "ERROR - nema tipa"
            else:
                rezultat = [[] for i in repeat(None, 1)]

                rezultat[0].append(tip)
                rezultat[0].append(0)
        else:
            specifikator_tipa = SpecifikatorTipa(desnaStrana[0][1])
            tip = specifikator_tipa.glavnaMetoda()

            if tip == "void":
                return "ERROR - konstanta ne moze biti void"
            else:
                rezultat = [[] for i in repeat(None, 1)]

                rezultat[0].append(tip)
                rezultat[0].append(1)
        #rezultat je u obliku [tip,0/1] gdje je 1 oznaka da je tip konstanta
        return rezultat

class ListaParametara(DefinicijaFunkcije):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<deklaracija_parametra>":
            deklaracija_parametara = DeklaracijaParametra(desnaStrana[0][1])
            tip_ime_niz = deklaracija_parametara.glavnaMetoda()
            #tip_ime_niz[0] = tip, tip_ime_niz[1] = ime, tip_ime_niz[2] = je li niz ili nije, 0/1
            tipovi_imena = []
            tipovi_imena.append(tip_ime_niz)
            return tipovi_imena


        else:
            lista_parametara = ListaParametara(desnaStrana[0][1])
            tipovi_imena = lista_parametara.glavnaMetoda()

            deklaracija_parametara = DeklaracijaParametra(desnaStrana[2][1])
            tip_ime_niz = deklaracija_parametara.glavnaMetoda()

            tipovi_imena.append(tip_ime_niz)
            return tipovi_imena


        return 0

class SpecifikatorTipa(ImeTipa):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        tmp = desnaStrana[0][0]
        tmp = list(tmp)

        for i in range(len(tmp)):
            if tmp[i] == ' ':
                kraj = i
                break

        del tmp[kraj:]
        tip = ''.join(tmp)

        if tip == 'KR_VOID':
            return "void"
        elif tip == 'KR_CHAR':
            return "char"
        elif tip == 'KR_INT':
            return "int"

class SlozenaNaredba(DefinicijaFunkcije):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        #print desnaStrana
        return 0

class DeklaracijaParametra(ListaParametara):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        ime_tipa = ImeTipa(desnaStrana[0][1])
        tip = ime_tipa.glavnaMetoda()
        if tip[0][0] == "void":
            return "ERROR - parametar ne smije biti void"

        tip_ime_niz = []
        tip_ime_niz.append(tip[0][0])

        #izluci IDN
        idn = desnaStrana[1][0]
        idn = list(idn)
        for i in reversed(range(len(idn))):
            if idn[i] == ' ':
                del idn[:i+1]
                break
        idn = ''.join(idn)

        tip_ime_niz.append(idn)

        #ako je niz oznaci tako u povratnoj vrijednosti
        if desnaStrana[2][0] == "L_UGL_ZAGRADA":
            tip_ime_niz.append(1)
        else:
            tip_ime_niz.append(0)

        return tip_ime_niz

#od ovdje       
class ListaInitDeklaratora(Deklaracija):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0
        
class InitDeklarator(ListaInitDeklaratora):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0
        
class Inicijalizator(InitDeklarator):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0
#do ovdje. radi naslijedjivanja

class IzrazPridruzivanja(Inicijalizator):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu
        self.desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

    def glavnaMetoda(self):
        print self.desnaStrana
        if self.desnaStrana[0][0] == "<log_ili_izraz>":
            log_ili_izraz = LogIliIzraz(self.desnaStrana[0][1])
            tip = log_ili_izraz.tip()
            rez = log_ili_izraz.glavnaMetoda()
            if rez != 0:
                return rez

        elif self.desnaStrana[0][0] =="<postfiks_izraz>":
            postfiks_izraz = PostfiksIzraz(self.desnaStrana[0][1])
            tip1 = postfiks_izraz.tip()
            rez1 = postfiks_izraz.glavnaMetoda()
            if rez1 != 1:
                return "Error."
                
            izraz_pridruzivanja = IzrazPridruzivanja(self.desnaStrana[1][1])
            tip2 = izraz_pridruzivanja.tip()
            rez2 = izraz_pridruzivanja.glavnaMetoda()
            if rez1 != rez2:
                return "Error."

        return 0

class LogIliIzraz(IzrazPridruzivanja):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class LogIIzraz(LogIliIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class BinIliIzraz(LogIIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class BinIIzraz(BinIliIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class JednakosniIzraz(BinIIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0
        
class AditivniIzraz(JednakosniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class MultiplikativniIzraz(AditivniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class CastIzraz(MultiplikativniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class UnarniIzraz(CastIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class PostfiksIzraz(UnarniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

class PrimarniIzraz(PostfiksIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):

        return 0

def ucitajUlaz():
    ulaz = open("ulaz1.in","r")
    listaPrograma = ulaz.readlines()

    #makni LF
    for i in range(len(listaPrograma)):
        listaPrograma[i] = listaPrograma[i].rstrip()
    return listaPrograma

def main ():

    global listaPrograma

    listaPrograma = ucitajUlaz()

    #stvori inicijalni objekt
    prijevodna_jedinica = PrijevodnaJedinica(0)
    rezultat = prijevodna_jedinica.glavnaMetoda()

    #je li doslo do pogreske, ako je 0 => sve u redu
    #if rezultat != 0:
        #print rezultat

if __name__ == '__main__':
  main()
