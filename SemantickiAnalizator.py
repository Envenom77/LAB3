__author__ = 'Matko'




def ucitajUlaz():
    ulaz = open("ulaz1.in","r")
    dict = {}

    for line in ulaz:
        trenutnaDubina = 0
        listLine = []
        listLine.extend(line)
        del listLine[-1]
        for item in listLine:
            if item == ' ':
                trenutnaDubina += 1
            else:
                break
        stringLine = ''.join(listLine)
        stringLine.strip()


def main ():

    stablo = ucitajUlaz()






if __name__ == '__main__':
  main()
