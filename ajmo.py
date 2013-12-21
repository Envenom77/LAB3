class Izraz(object):
    def __init__(self,pozicijaUprogramu):
                self.tip = 0
        self.l_izraz = 0
        self.pozicijaUprogramu = pozicijaUprogramu
 
    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
 
        if desnaStrana[0][0] = "<izraz_pridruzivanja>":
                       
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[0][1])
            tip = izraz_pridruzivanja.tip
            l_izraz = izraz_pridruzivanja.l_izraz
            rez = izraz_pridruzivanja.glavnaMetoda()
            if rez != 0:
                return rez
 
        elif desnaStrana[0][0] == "<izraz>":
            izraz = Izraz(desnaStrana[0][1])
            rez = izraz.glavnaMetoda()
            if rez != 0:
                return rez
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[1][1])
            tip = izraz_pridruzivanja.tip
            l_izraz = 0
           
            rez = izraz_pridruzivanja.glavnaMetoda()
            if rez != 0:
                return rez
 
        return 0
 
class PrimarniIzraz(Izraz):
    def __init__(self,pozicijaUprogramu):
        pass
        # Ako se ne varam, od nadklase nasljeđuje konstruktor, dakle
        # bilježi poziciju i svojstva "tip" i "l-izraz"
 
    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
               
                # Priprema str 51. Dakle, generiraju se završni znakovi.
                # Trebalo bi regexom provjeravati desnu stranu (čini mi se)
                # http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
        # Ako je u obliku broja zapisan
        if re.match(r"[-+]?\d+$", desnaStrana[0][0]) is not None:
                        broj = (int)desnaStrana[0][0]
                        # Ako je u dozvoljenom rasponu
                        if broj > -2147483648 and broj < 2147483647:
                                tip = 'int'
                                l_izraz = 0
                               
                                # Ova dva atributa prolaskom kroz stablo bi se trebala
                                # slati dalje, odnosno svi objekti koji nasljeđuju ovaj
                                # imat će pristup spremljenim atributima
                               
                                return "BROJ" # Ili šta već treba vratiti ukoliko je
                                # ispravan
                       
                        # Treba implementirati tablicuZnakova i izvršiti provjere
                # Ostale provjere: ako je ZNAK, ako je NIZ_ZNAKOVA itd.
               
                # Za provjeru IDN-a NUŽNO je napraviti tablicu znakova
                # Idealno bi bilo za IDN isto definirati objekt, kojem se onda lako
                # mogu dodavati atributi  itd.
 
        return "ERROR - očekujem primarni izraz"
