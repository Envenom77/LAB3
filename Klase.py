class IzrazPridruzivanja(Izraz):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] = "<log_ili_izraz>":
            log_ili_izraz = LogIliIzraz(desnaStrana[0][1])
            rez = log_ili_izraz.glvanaMetoda()
            if rez != 0:
                return rez

        elif desnaStrana[0][0] = "<postfiks_izraz>":
            postfiks_izraz = PostfiksIzraz(desnaStrana[0][1])
            rez = postfiks_izraz.glavnaMetoda()
            if rez != 0:
                return rez
           izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[1][1])
            rez = izraz_pridruzivanja.glavnaMetoda()
            if rez != 0:
                return rez

        return 0


class Izraz(???):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] = "<izraz_pridruzivanja>":
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[0][1])
            rez = izraz_pridruzivanja.glavnaMetoda()
            if rez != 0:
                return rez

        elif desnaStrana[0][0] == "<izraz>":
            izraz = Izraz(desnaStrana[0][1])
            rez = izraz.glavnaMetoda()
            if rez != 0:
                return rez
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[1][1])
            rez = izraz_pridruzivanja.glavnaMetoda()
            if rez != 0:
                return rez

        return 0

class ListaIzrazaPridruživanja(???):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<izraz_pridruzivanja>":
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[0][1])
            rez = izraz_pridruzivanja.glavnaMetoda()

        elif desnaStrana[0][0] == "<lista_izraza_pridruzivanja>":
            lista_izraza_pridruzivanja = ListaIzrazaPridruzivanja(desnaStrana[0][1])
            rez = lista_naredbi.glavnaMetoda()

            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[1][1])
            rez = izraz_pridruzivanja.glavnaMetoda()

        return 0


class JednakonsniIzraz(BinIIzraz):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<odnosni_izraz>":
            odnosni_izraz = OdnosniIzraz(desnaStrana[0][1])
            rez = odnosni_izraz.glavnaMetoda()

        elif desnaStrana[0][0] == "<jednakonsni_izraz>":
            jednakonsni_izraz = JednakonsniIzraz(desnaStrana[0][1])
            rez = jednakonsni_izraz.glavnaMetoda()

            odnosni_izraz = OdnosniIzraz(desnaStrana[1][1])
            rez = odnosni_izraz.glavnaMetoda()

        return 0


class OdnosniIzraz (JednakosniIzraz):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<aditivni_izraz>":
            aditivni_izraz = AditivniIzraz(desnaStrana[0][1])
            rez = aditivni_izraz.glavnaMetoda()

        elif desnaStrana[0][0] == "<odnosni_izraz>":
            odnosni_izraz = OdnosniIzraz(desnaStrana[0][1])
            rez = odnosni_izraz.glavnaMetoda()

            aditivni_izraz = AditivniIzraz(desnaStrana[1][1])
            rez = aditivni_izraz.glavnaMetoda()

        return 0


class IzrazNaredba(???):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

#nemam blage koji k treba s ovim kad ima samo TOCKAZAREZ s desne strane i općenito s operatorima