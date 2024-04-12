
#1. Crea un diccionario vacío llamado perro

perro = {}
print("1) Diccionario perro creado")

#2. Añade color raza patas y edad al diccionario perro

perro = {
    "color": "marrón",
    "raza": "labrador",
    "patas": 4,
    "edad": 5
}

print("\n2) Diccionario perro actualizado", perro)

#3. Crea un diccionario de estudiante y añade nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves de diccionario

estudiante = {
    "nombre": "Juan",
    "apellido": "Gómez",
    "sexo": "masculino",
    "edad": 20,
    "estado civil": "soltero",
    "habilidades": ["programación", "matemáticas", "comunicación"],
    "país": "España",
    "ciudad": "Madrid",
    "dirección": "Calle Principal 123"
}

print("\n3) Diccionario estudiante creado y con claves añadidas")

#4. Obtén la longitud del diccionario del alumno

longitud = len(estudiante)
print("\n4) La longitud del diccionario del alumno es:", longitud)

#5. Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista

habilidades = estudiante["habilidades"]
tipo = type(habilidades)

print("\n5) Las habilidades del estudiante son:", habilidades)
print("   El tipo de datos de las habilidades es:", tipo)

#6. Modifique el valor de las habilidades añadiendo una o mas habilidades

nhabilidades = ["resolución de problemas", "creatividad"]# Agregar una o más habilidades al diccionario de estudiante
estudiante["habilidades"].extend(nhabilidades)
print("\n6) Las habilidades actualizadas del estudiante son:\n", estudiante["habilidades"])# Imprimir las habilidades actualizadas

#7. obten las claves del diccionario como una lista

claves = list(estudiante.keys())
print("\n7) Las claves del diccionario del estudiante son:\n", claves)

#8. obtener los valores del diccionario como una lista

valores = list(estudiante.values())
print("\n8) Los valores del diccionario del estudiante son:\n", valores)

#9. cambie el diccionario de una lista de tuplas utilizando el metodo items()

lista_tuplas = list(estudiante.items())
print("\n9) El diccionario del estudiante como una lista de tuplas es:")
print(lista_tuplas)

#10. eliminar uno de los elementos de diccionario

valor_eliminado = estudiante.pop("edad")
print("\n10) El valor eliminado es:", valor_eliminado)
print("Después de eliminar 'edad', el diccionario del estudiante es:")
print(estudiante)

#11. elimina uno de los diccionarios

#demostracion

try:
  del estudiante
  print(estudiante)
except:
  print("\n11) El diccionario estudiante ha sido eliminado o no existe.")