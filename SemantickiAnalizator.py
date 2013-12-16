__author__ = 'Matko'




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






if __name__ == '__main__':
  main()
