#clase persona
class Persona:
    nombre = ""
    edad = 1
    altura = 0
    genero = ""

    def __init__(self, att_nombre, att_edad, att_altura, att_genero):
        self.nombre = att_nombre
        self.edad = att_edad
        self.altura = att_altura
        self.genero = att_genero

    def caminar(self):
        return f"Hola soy {self.nombre} y Estoy caminando..."
    def hablar(self):
        return f"Hola soy {self.nombre} y Estoy hablando..."

personas_encuentadas = []
while True:
    op = int(input("""Escoge
             1. Ingresar datos
             2. Ver listado de personas
             0. Salir
             : """))
    if op == 0:
        break
    if op == 1:
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        altura = float(input("Ingrese altura: "))
        genero = input("Ingrese genero: ")

        persona = Persona(nombre, edad, altura, genero)
        personas_encuentadas.append(persona)
    else:
        for persona in personas_encuentadas:
            print(persona.nombre)