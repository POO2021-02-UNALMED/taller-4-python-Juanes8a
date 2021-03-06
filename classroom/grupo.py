from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    
    def __str__(self):
        fresa='Grupo de estudiantes: '+self._grupo
        return fresa


    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            self._asignaturas.append(kwargs[x])

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista+[alumno]


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
