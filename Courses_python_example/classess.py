class Node_Curso:
    def __init__(self, nombre_curso: str = "Curso sin nombre", \
        capacidad_curso: int = 2, \
        next_node=None, prev_node=None):

        self.nombre_curso = nombre_curso
        self.capacidad_curso = capacidad_curso
        self.next = next_node
        self.prev = prev_node
        self.Lista_matriculados = Lista_estudiantes()
        self.Lista_espera = Lista_estudiantes()

    def __str__(self):
        return "nombre: "+self.nombre_curso + " y "+\
        "capacidad de: "+ str(self.capacidad_curso)

class LinkedList:
    
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self):
        return [[node.nombre_curso, node.capacidad_curso] for node in self]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            self.tail.next = Node_Curso(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            self.head = Node_Curso(value, self.head)
        return self.head


class Node_Estudiante:
    def __init__(self, nombre_estudiante: str = "sin nombre", \
        codigo: int = 30, \
        next_estudiante=None, prev_estudiante=None):

        self.nombre_estudiante = nombre_estudiante
        self.codigo = codigo
        self.next_estudiante = next_estudiante
        self.prev_estudiante = prev_estudiante

    def __str__(self):
        return "nombre: "+self.nombre_estudiante

class Lista_estudiantes:
    def __init__(self, values=None):
        self.head_estudiante = None
        self.tail_estudiante = None
        self.matriculados = 0
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head_estudiante
        while node:
            count += 1
            node = node.next_estudiante
        return count
    
    def __iter__(self):
        current = self.head_estudiante
        while current:
            yield current
            current = current.next_estudiante
            
    @property
    def values(self):
        return [node.nombre_estudiante for node in self]
    
    def check_if(self, value, curso : Node_Curso):
        if (self.matriculados < curso.capacidad_curso):
            self.matriculados = self.matriculados + 1
            self.add_node(value)
        else:
            curso.Lista_espera.add_node(value)

    def add_node(self, value: list):
        if self.head_estudiante is None:
            self.tail_estudiante = self.head_estudiante = Node_Estudiante(
                nombre_estudiante=value[0], codigo=value[1])
        else:
            self.tail_estudiante.next_estudiante = Node_Estudiante(
                nombre_estudiante=value[0], codigo=value[1])
            self.tail_estudiante = self.tail_estudiante.next_estudiante
        return self.tail_estudiante
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)