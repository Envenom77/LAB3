class IzrazPridruzivanja(Inicijalizator):
    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        mark = 0
        
        if desnaStrana[0][0] == "<log_ili_izraz>":
            log_ili_izraz = LogIliIzraz(desnaStrana[0][1])
            rez = log_ili_izraz.glavnaMetoda()
            return rez

        elif desnaStrana[0][0] =="<postfiks_izraz>":
            print "nasao postfiks."
            postfiks_izraz = PostfiksIzraz(desnaStrana[0][1])
            rez = postfiks_izraz.glavnaMetoda()
           
            izraz_pridruzivanja = IzrazPridruzivanja(desnaStrana[0][1] - 1)
            rez1 = izraz_pridruzivanja.glavnaMetoda()
            if rez[1] == 1 and rez1[1] == rez[1]:
                tmp = []
                tmp.append(rez1[1])
                tmp.append(0)
                return tmp

        return 0

class LogIliIzraz(IzrazPridruzivanja):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<log_i_izraz>":
            log_i_izraz = LogIIzraz(desnaStrana[0][1])
            rez = log_i_izraz.glavnaMetoda()
            return rez
                
        elif desnaStrana[0][0] == "<log_ili_izraz>":
            log_ili_izraz = LogIliIzraz(desnaStrana[0][1])
            rez1 = log_ili_izraz.glavnaMetoda()
            
            log_i_izraz = LogIIzraz(desnaStrana[0][1])
            rez2 = log_i_izraz.glavnaMetoda()
            
            if rez1[1] == 0 and rez2[1] == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp

        return 0

    def tip(self):

        return 0
        
class LogIIzraz(LogIliIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        tmp = []
        tmp.append(0)
        tmp.append(0)
        return tmp

class BinIliIzraz(LogIIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        tmp = []
        tmp.append(0)
        tmp.append(0)
        return 0

class BinIIzraz(BinIliIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        tmp = []
        tmp.append(0)
        tmp.append(0)
        return 0

class JednakosniIzraz(BinIIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<odnosni_izraz>":
            odnosni_izraz = OdnosniIzraz(desnaStrana[0][1])
            rez = odnosni_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[0][0] == "<jednakosni_izraz>":
            jednakosni_izraz = JednakosniIzraz(desnaStrana[0][1])
            rez = jednakosni_izraz.glavnaMetoda()
            
            odnosni_izraz = OdnosniIzraz(desnaStrana[0][1])
            rez1 = odnosni_izraz.glavnaMetoda()
            
            if rez[0] == 0 and rez1[0]  == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp
        return 0
        
class AditivniIzraz(JednakosniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        tmp = []
        tmp.append(0)
        tmp.append(0)

        return 0

class MultiplikativniIzraz(AditivniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<cast_izraz>":
            cast_izraz = CastIzraz(desnaStrana[0][1])
            rez = cast_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[0][0] == "<multiplikativni_izraz>":
            multiplikativni_izraz = MultiplikativniIzraz(desnaStrana[0][1])
            rez = multiplikativni_izraz.glavnaMetoda()
            
            cast_izraz = CastIzraz(desnaStrana[0][1])
            rez1 = cast_izraz.glavnaMetoda()
            
            if rez[0] == 0 and rez1[0]  == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp

        return 0

class CastIzraz(MultiplikativniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<unarni_izraz>":
            unarni_izraz = UnarniIzraz(desnaStrana[0][1])
            rez = unarni_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[0][0] == "L_ZAGRADA" and desnaStrana[1][0] == "<ime_tipa>" and desnaStrana[3][0] == "<cast_izraz>":
            ime_tipa = ImeTipa(desnaStrana[0][1])
            rez = ime_tipa.glavnaMetoda()
            
            cast_izraz = CastIzraz(desnaStrana[0][1])
            rez1 = cast_izraz.glavnaMetoda()
            # Nije dobro, treba prepraviti.
            # 3. <cast_izraz>.tip se moze pretvoriti u <ime_tipa>.tip po poglavlju 4.3.1
            tmp = []
            tmp.append(0)
            tmp.append(0)
            return tmp
        return 0

class UnarniIzraz(CastIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<postfiks_izraz>":
            postfiks_izraz = PostfiksIzraz(desnaStrana[0][1])
            rez = postfiks_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[1][0] == "<unarni_izraz>":
            unarni_izraz = UnarniIzraz(desnaStrana[0][1])
            rez = unarni_izraz.glavnaMetoda()
            
            if rez[1] == 1 and rez[0] == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp
                
        elif desnaStrana[0][0] == "<unarni_operator>" and desnaStrana[1][0] == "<cast_izraz>":
            cast_izraz = CastIzraz(desnaStrana[0][1])
            rez = cast_izraz.glavnaMetoda()
            
            if rez[0] == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp

        return 0

class OdnosniIzraz(JednakosniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        
        if desnaStrana[0][0] == "<aditivni_izraz>":
            aditivni_izraz = AditivniIzraz(desnaStrana[0][1])
            rez = aditivni_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[0][0] == "<odnosni_izraz>":
            odnosni_izraz = OdnosniIzraz(desnaStrana[0][1])
            rez = odnosni_izraz.glavnaMetoda()
            
            aditivni_izraz = AditivniIzraz(desnaStrana[0][1])
            rez1 = aditivni_izraz.glavnaMetoda()
            
            if rez[0] == 0 and rez1[0]  == 0:
                tmp = []
                tmp.append(0)
                tmp.append(0)
                return tmp

        return 0

class PostfiksIzraz(UnarniIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)

        if desnaStrana[0][0] == "<primarni_izraz>":
            primarni_izraz = PrimarniIzraz(desnaStrana[0][1])
            rez = primarni_izraz.glavnaMetoda()
            return rez
            
        elif desnaStrana[0][0] == "<postfiks_izraz>" and desnaStrana[1][0] == "L_UGL_ZAGRADA":
            postfiks_izraz = PostfiksIzraz(desnaStrana[0][1])
            rez1 = postfiks_izraz.glavnaMetoda()
            
            izraz = Izraz(desnaStrana[0][1])
            rez2 = izraz.glavnaMetoda()
            
            #tip <- X
            #l-izraz <- X != const(T)
            #postfiks_izraz.tip = niz(X)
            
        elif desnaStrana[0][0] == "<postfiks_izraz>" and desnaStrana[1][0] == "L_ZAGRADA":
            postfiks_izraz = PostfiksIzraz(desnaStrana[0][1])
            rez = postfiks_izraz.glavnaMetoda
            
            #tip <- pov
            #l-izraz <- 0
            #<postfiks_izraz>.tip = funkcija(void -> pov)

        return 0

class PrimarniIzraz(PostfiksIzraz):

    def __init__(self,pozicijaUprogramu):
        self.pozicijaUprogramu = pozicijaUprogramu

    def glavnaMetoda(self):
        desnaStrana = nadiDesnuStranu(self.pozicijaUprogramu)
        # Neznam sta znaci IDN/BROJ/ZNAK/NIZ_ZNAKOVA, tj kako je to realizirano?
        tmp = []
        tmp.append(0)
        tmp.append(0)

        return 0