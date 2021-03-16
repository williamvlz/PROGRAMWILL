#------------------------------------- QUIZ #2 ---------------------------------------#

temperatura_Corporal = [36, 37, 38, 35, 36, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.3, 33]

pOpcion = """ INGRESE UNA DE LAS SIGUIENTES OPCIONES
1. SI DESEA CONVERTIR LA TEMPERATURA DE CELSIUS A FARENHEIT
2. ESTADO DEL PACIENTE SEGUN TEMPERATURA
3. SI DESEA MOSTRAR LA TEMPERATURA MAS ALTA, MAS BAJA Y EL PROMEDIO DE LAS MISMAS
4. SALIR
""" 

pTemperatura = """
C. MOSTRAR EN CELSIUS 
K. MOSTRAR EN KELVIN
F. MOSTRAR EN FARENHEIT
"""

pBienvenida = "INGRESE LA TEMPERATURA DEL PACIENTE"

#----------------------------- CONVERSION ------------------------------#

lKelvin = []
for elemento in temperatura_Corporal :
    conversion = round (elemento + 273.15)
    lKelvin.append (conversion)
lFarenheit = []
for elemento in temperatura_Corporal :
    conversion = round ((elemento * 1.8)+32)
    lFarenheit.append (conversion)

#-------------------------------- ENTRADAS --------------------------------#

print ("BIENVENID@ AL CENTRO DE TEMPERATURAS")

opcionEscogida = int (input(pOpcion))
while (opcionEscogida != 4):
    if (opcionEscogida == 1):
        opcionTemperatura = (input(pTemperatura))
        if (opcionTemperatura == "C"):
            print ("LA LISTA SE ENCUENTRA EN  GRADOS CELSIUS, NO ES NECESARIA SU CONVERSION")
            print (temperatura_Corporal)
        elif (opcionTemperatura == "K"):
            print ("A CONTINUACION LISTA EN GRADOS KELVIN:")
            print (lKelvin)
        elif (opcionTemperatura == "F"):
            print ("A CONTINUACION LISTA EN GRADOS FARENHEIT")
            print (lFarenheit)
        else:
            print ("LA OPCION INGRESADA NO ES VALIDA")
    elif (opcionEscogida == 2):
        temperatura = float (input(pTemperatura))
        if (temperatura < 36):
            print ("CUIDADO, PACIENTE CON HIPOTERMIA")
            print ("su temperatura es:", temperatura)
        elif (temperatura>= 36 and temperatura <37.5):
            print ("PUEDE ESTAR TRANQUILO, SU TEMPERATURA SE ENCUENTRA EN ESTADO NORMAL")
            print ("su temperatura es:", temperatura)
        else:
            print ("ALERTA, PACIENTE CON FIEBRE")
            print ("su temperatura es:", temperatura)
    elif (opcionEscogida == 3):
        print ("TEMPERATURA MAYOR DE LOS DATOS TOMADOS: ", max (temperatura_Corporal))
        print ("TEMPERATURA MENOR DE LOS DATOS TOMADOS: ", min (temperatura_Corporal))
        print ("LA TEMPERATURA ES TOMADA CADA :", len (temperatura_Corporal)/24, "HORAS")
    else:
        print ("OPCION INGRESADA ES INVALIDA")
        opcionEscogida = int (input(pOpcion))

print ("GRACIAS")