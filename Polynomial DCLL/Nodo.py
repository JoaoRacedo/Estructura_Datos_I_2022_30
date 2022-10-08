class Nodo:
    def __init__(self, data):
        self.coef = data[0]
        self.exp = str(data[1])
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return str([self.coef, self.exp])