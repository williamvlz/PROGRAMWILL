#............................QUIZ PAREJAS......................................#
#.........................CLASES Y OBJETOS.....................................#
#..................integrantes: WILLIAM VELEZ Y SERGIO GOMEZ.................#

#...........................PUNTO 1............................................#

class ElementosDigitales():
    def _init_ (self, Nombre, Creador, FechaPublicacion):
        self.Nombre = Nombre
        self.Creador = Creador
        self.FechaPublicacion = FechaPublicacion
    def MostrarAtributos (self):
        print(f"HOLA MI NOMBRE ES {self.Nombre}, soy el creador de {self.creador} Y FUE PUBLICADO EN {self.FechaPublicacion")
