#........................TALLER 6.......................#

#.......................PUNTO 1.........................#
#.......................CLASE TORTA.....................#

class Torta():
    def _init_ (self,FormaEntrada, SaborEntrada, AlturaEntrada):
        self.Forfa = FormaEntrada
        self.Sabor = SaborEntrada
        self.Altura = AlturaEntrada
        print("""
            La forma es {self.Forfa}
            El sabor es {self.Sabor}
            El alto es {self.Altura} en centimentros
        """)

print ("#"*6, "LA TORTA", "#"*6)
La_Torta = Torta("cilindro", "chocolate",60)

#...................PUNTO 2..............................#
#.........................CLASE ESTUDIANTE................#

class Estudiante():
    def __init__(self,Edad, Nombre, ID, Carrera, Semestre):
        self.Edad=Edad
        self.Nombre=Nombre
        self.ID=ID
        self.Carrera=Carrera
        self.Semestre=Semestre
    def TiempoEstudio (self, Materia, Tiempo):
        print (f"ESTUDIARE {Materia} en {Tiempo} HORAS")

print ("#"*6, "HORAS DE ESTUDIO", "#"*6)
Estudiante1 = Estudiante (21, "WILLIAM", 1037670235, "ING.BIOMEDICA", "QUINTO")
Estudiante1.TiempoEstudio("QUIMICA",4)


#...........................PUNTO 3......................................#
#...........................CLASE NUTRICIONISTA...........................#

class Nutricionista():
    def _init_ (self, Edad,Nombre,Universidad):
        self.Edad=Edad
        self.Nombre=Nombre
        self.Universidad=Universidad
    def IMC(self,peso,estatura):
        imc = peso/(estatura**2)
        print(f"EL IMC ES...  {imc}")

print("#"*6, "IMC", "#"*6)
Nutricionista1 = Nutricionista (27, "LUIS", "UNIVERSIDAD CES")
Nutricionista1.IMC (87,1.68)

#...............................PUNTO 4.................................#
#...........................CLASE CANGURO...............................#

class Canguro():
    def _init_(self, Edad, ID, Nombre):
        self.Edad=Edad
        self.ID = ID
        self.Nombre = Nombre
    def SaltosCanguro (self, NumeroSaltos):
        for Saltos in range (NumeroSaltos):
            if (Saltos == 0):
                veces = "vez"
            else:
                veces = "veces"
            print(f"EL CANGURO {self.Nombre} HA SALTADO {Saltos + 1} {veces}")

print ("#"*6,  "SALTOS DEL CANGURO", "#"*6)
Canguro1 = Canguro (28, 119845367, "RAMON")
Canguro1.SaltosCanguro (8)

#..................................PUNTO 5.......................................#
#............................CLASE INSTRUMENTO...................................#
#...................................VIOLIN.......................................#

class Violin ():
    def __init__ (self, TipoViolin, ColorViolin, AñosViolin):
        self.TipoViolin = TipoViolin
        self.ColorViolin= ColorViolin
        self.AñosViolin= AñosViolin
    def TocarViolin (self, Melodia):
        print (f"WILLIAM TOCA UN VIOLIN TIPO {self.TipoViolin} QUE ES DE COLOR {self.ColorViolin} Y TIENE {self.AñosViolin} AÑOS Y SUENA ESTA MELODIA {Melodia}")  

Violin1 = Violin("VIOLIN DE CONCIERTO", "CAFE", 3)
Violin1.TipoViolin("MOZART")

