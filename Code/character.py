class Character:
    def __init__(self, nombre, fuerza, destreza, ki, carisma, pilotaje, jinchoneria, logica, copia, raza, clase, arma, vida, cki, zenis):
        self.nombre = nombre
        self.stats = {"fuerza" : fuerza,
            "destreza" : destreza,
            "ki" : ki,
            "carisma" : carisma,
            "pilotaje" : pilotaje,
            "jinchoneria" : jinchoneria,
            "logica" : logica,
            "copia" : copia
        }
        self.arma = arma
        self.raza = raza
        self.clase = clase
        self.salud = max(2*(fuerza+destreza+ki+carisma+pilotaje+jinchoneria+logica+copia), 20)
        self.salud_actual = vida
        self.cargas_ki = cki
        self.nofils = zenis
        self.items = {}
    def set_items(self, items):
        self.items = items
