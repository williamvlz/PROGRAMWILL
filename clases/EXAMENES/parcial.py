#......................PARCIAL 1......................#

#........................PUNTO 1......................#

#.................SUMA.............#
def sumar (a=0, b=0, c=0) :
    suma = a + b + c
    return suma

#.................RESTAR.............#
def restar (a=0, b=0, c=0) :
    resta = a - b - c
    return resta

#.................MULTIPLICAR.............#
def multiplicar (a=0, b=0, c=0) :
    multiplicacion = a * b * c
    return multiplicacion

#.................DIVIDIR.............#
def dividir (a=0, b=0, c=0) :
    division = a / b / c
    return division

#.................POTENCIA.............#
def potencia (base=0, a=1, b=1):
    potenciacion = base ** a ** b
    return potenciacion

def operaciones (operacion, a, b, c):
    print(operacion(a,b,c))

operaciones (sumar, 6,12,4)
operaciones (restar, 5,9,1)
operaciones (multiplicar, 9,3,4)
operaciones (dividir,34,47,23)
operaciones (potencia,4,6,8)
#.......................PUNTO 2.......................#
listaNumerosa = [1,2,3,4,5]
listaNumerosb = [10,20,30,40,50]
listaNumerosc = [100,200,300,400,500]

def lista1 ():
    for elemento in listaNumerosa:
         print (elemento)

lista1()

def lista2 ():
    for elemento in listaNumerosb:
      print (elemento)

lista2 ()

def lista3 ():
    for elemento in listaNumerosc:
        print (elemento)

lista3 ()

#......................PUNTO 3.......................#
def area (base,altura):
    area = (base * altura)/2
    return area

base = float (input ("ingrese el valor de la base : "))
altura = float (input ("ingrese el valor de la altura : "))

areas = area (base,altura)
print ("el resultado del area es :", areas)

#......................punto 4........................#

listanumeros = [1,10,100,1000,10000,100000,1000000,10000000]

def lista():
    print("MAYOR DE LA LISTA : ", max (listanumeros))
    print("MENOR DE LA LISTA : ", min (listanumeros))
    print("PROMEDIO DE LA LISTA : ", sum(listanumeros)/len(listanumeros))

lista()



