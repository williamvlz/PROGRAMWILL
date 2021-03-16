#------------- TALLER #4 RECOPILATORIO -------------#

#-------------------- PREGUNTAS --------------------#
listaDolares = [20000, 30000, 4000, 2500, 1000, 7600]

pNumero = """INGRESE UNA DE LAS SIGUIENTES OPCIONES
1: Convertir dolares a pesos o euros
2: Mostrar lista de clasificacion de sus ingresos
3: Mostrar nivel de ingresos
4: salir
"""

pMoneda = """
C = MOSTRAR LISTA DE PESOS COLOMBIANOS
D = MOSTRAR LISTA ORIGINAL EN DOLARES
E = MOSTRAR LISTA EN EUROS
"""

PIngreso = " Cual es tu ingreso mensual en Dolares : "

#--------------------- CONVERSION ---------------------#

listaPesoscolombianos = []
for elemento in listaDolares:
    conversion = round (elemento * 3700)
    listaPesoscolombianos.append (conversion)

listaEuros = []
for elemento in listaDolares:
    conversion = round (elemento * 0.84)
    listaEuros.append(conversion)

#-------------------- ENTRADAS --------------------#

print (" BIENVENID@")

OPCION = int(input(pNumero))
while (OPCION != 4):
    if (OPCION == 1):
        opcionMoneda = (input(pMoneda))
        if (opcionMoneda == "D"):
            print ("NO SERA NECESARIA LA CONVERSION, LA LISTA SE ENCUETRA EN DOLARES")
            print(listaDolares)
        elif(opcionMoneda == "C"):
             print ("LISTA EN PESOS COLOMBIANOS")
             print (listaPesoscolombianos)
        elif (opcionMoneda == "E"):
            print ("LISTA EN EUROS")
            print (listaEuros)
        else:
            print("LA OPCION INGRESADA NO ES VALIDA")
    elif (OPCION == 2):
        ingresos = float(input(PIngreso))
        if (ingresos <= 1000):
            print ("INGRESOS BAJOS")
            print ("sus ingresos son :", ingresos)
        elif(ingresos > 1000 and ingresos < 7000):
            print ("INGRESOS MEDIOS")
            print ("sus ingresos son :", ingresos)
        else:
            print("INGRESOS ELEVADOS")
            print ("sus ingresos son :", ingresos)
    elif (OPCION == 3):
        print ("NUMERO MAYOR DE LA LISTA :", max ( listaDolares))
        print ("NUMERO MENOR DE LA LISTA :", min (listaDolares))
        print ("NUMERO PROMEDIO DE LA LISTA :", sum (listaDolares) / len (listaDolares))
    else:
        print ("OPCION NO VALIDA")
    OPCION = int (input(pNumero))

print ("GRACIAS")

