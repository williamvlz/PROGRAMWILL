#..............................PARCIAL FINAL......................#
#....................WILLIAM VELEZ MESA...........................#

#...."MUCHAS GRACIAS POR TODO LO ENSEÑADO PROFESOR, POR HACER QUE LA CLASE NO FUERA UNA MAS DEL MONTON"...#

#.......................PUNTO 1.....................#
import matplotlib.pyplot as plt
import pandas as pd 

comida1 = input ("ingresa tu comida preferida : ")
precio1 = int(input("ingresa el precio del alimeto : "))
comida2 = input ("ingresa tu comida preferida : ")
precio2 = int(input("ingresa el precio del alimeto : "))
comida3 = input ("ingresa tu comida preferida : ")
precio3 = int(input("ingresa el precio del alimeto : "))
comida4 = input ("ingresa tu comida preferida : ")
precio4 = int(input("ingresa el precio del alimeto : "))
comida5 = input ("ingresa tu comida preferida : ")
precio5 = int(input("ingresa el precio del alimeto : "))
comida6 = input ("ingresa tu comida preferida : ")
precio6 = int(input("ingresa el precio del alimeto : "))
comida7 = input ("ingresa tu comida preferida : ")
precio7 = int(input("ingresa el precio del alimeto : "))
comida8 = input ("ingresa tu comida preferida : ")
precio8 = int(input("ingresa el precio del alimeto : "))

listaComidas = [comida1,comida2, comida3, comida4, comida5,comida6,comida7,comida8]
listaPrecio = [precio1, precio2, precio3, precio4, precio5, precio6, precio7, precio8]

plt.bar(listaComidas,listaPrecio)
plt.xlabel("comida")
plt.ylabel("precio")
plt.title("grafico barras")
plt.savefig ("barras.png")
plt.show()

#............................PUNTO 2..................................#
class Humano ():
    def init(self, Nombre, Sexo, Edad):
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Edad = Edad
    def Hablar (self, Mensaje):
        print (Mensaje)

Humano1 = Humano ( "WILLIAM", "Masculino", 21)
Humano1.Hablar ("soy adicto al deporte, llevo una vida fitness, todo lo llevo bajo control.")

class Doctor (Humano):
    def  _init_ ( self , nombreEntrada , edadEntrada , estaturaEntrada, pesoEntrada ):
        self . estatura = estaturaEntrada
        self . peso = pesoEntrada
    
    def IMC (peso,estatura):
        imc = peso/(estatura**2)
        return imc

peso = float(input("ingrese su peso : "))
estatura = float(input("ingrese su estaura : "))

tu_imc = peso/(estatura**2)
print ("su imc es : ", tu_imc)

#....................PUNTO 3...........................#
def ConversorDolares ():
    iscorrecto = False
    while(isCorrecto == false):
        try:
            nombre = input ("porfavor ingrese su nombre :")
            assert (nombre.isalpha () )
            isCorrecto = True
        except AssertionError:
            print ("no son validos los datos ingresados")
    iscorrecto = False
    while (iscorrecto == false):
        try:
            dinero = float (input("ingrese la cantidad de dinero en dolares : "))
            iscorrecto = True
            except ValueError:
                print("no son validos los datos ingresados")

#.......................PUNTO 4.................#
import sys
Nombre = input ("CUAL ES SU NOMBRE :")
Enfermedad = input ("CUAL ES SU ENFERMEDAD :")
Precio = int (input("VALOR DE LA CONSULTA :"))

NombreArchivo = "Paciente.txt"
try:
    Archivo = open (NombreArchivo)
    print("1")
except FileNotFoundError:
    Archivo = open (NombreArchivo, "w", encoding="UTF-8")
    Descripcion = "Archivo de pacientes"
    print("2")
    Archivo.writelines (Descripcion)
    sys.exit(1)

Archivo = open (NombreArchivo, "a")
Linea = " \nombre: " + " Enfermedad: " + str(Enfermedad) + " Precio: " + str(Precio)
Archivo.writelines(Linea)
Archivo.close()



