class Barrio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []
    
    def agrega_a_lista(self, atri):
        self.lista.append(atri)