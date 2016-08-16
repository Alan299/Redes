import csv

mydict = dict()


def suma_cinco(x):
    """ por cada caracter de x se tomara su valor ascii y se le sumara 5 unidades """
    nueva_x = ""
    for char in x:
        nueva_x += chr((ord(char)+ 5) % 128)
        
    return nueva_x
            
def ingresar(usuario,contrasena):
    with open('Code\input.txt', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    try:
        cont = mydict[usuario]
        contrasena = suma_cinco(contrasena)
        print cont
        print  cont == contrasena
        if  cont == contrasena:
            print "Logeado"
            return True
        return False    
            
    except KeyError, e:
        print ' KeyError - razon "%s"' % str(e)
        return False

