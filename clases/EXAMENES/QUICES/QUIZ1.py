#.....perfil lipidico.....#

#......constantes......#
mensaje_de_bienvenida = "este es el analisis de resultado de su examen"
mensaje_triglicerido = "ingrese valor de trigliceridos : "
mensaje_homosisteina = "ingrese valor de homosisteina : "
mensaje_despedida = "este es el resultado de tu examen"

#......codigo trigliceridos......#
print(mensaje_de_bienvenida)
trigliceridos = float(input(mensaje_triglicerido))
isOptimo = trigliceridos < 150
isSobrelimite = trigliceridos >= 150 and trigliceridos<= 199
isAalto = trigliceridos >= 200 and trigliceridos <= 499
isMuyalto = trigliceridos >= 500

if(isOptimo):
    print("los trigliceridos estan en buen estado")
elif(isSobrelimite):
    print( "los trigliceridos se encuentran sobre el limite")
elif(isAalto):
    print( "los trigliceridos estan altos")
else:
    print( "cuidad, los trigliceridos estan muy altos")

#......codigo homosisteina......#
print(mensaje_de_bienvenida)
homosisteina = float(input(mensaje_homosisteina))
isOptimohomosisteina = homosisteina >= 2 and homosisteina < 15
isSobrelimitehomosisteina = homosisteina >= 15 and homosisteina<= 30
isAaltohomosisteina = homosisteina >= 30 and homosisteina <= 100
isMuyaltohomosisteina = homosisteina >= 100

if(isOptimohomosisteina):
    print( "la homosisteina estan en buen estado")
elif(isSobrelimitehomosisteina):
    print( "la homosisteina se encuentran sobre el limite")
elif(isAaltohomosisteina):
    print( "la homosisteina se encuentra alta")
else:
    print( "cuidad, la homosisteina esta muy alta")
print(mensaje_despedida)
